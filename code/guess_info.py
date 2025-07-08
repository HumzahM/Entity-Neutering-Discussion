from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import json
import asyncio
import os
from utils import truncate_to_n_tokens, mention_detected

#Closely based off of the prompt found in the June 24, 2025 paper (Appendix B.2)
guessing_info_prompt = """
You will receive a body of text which has been anonymized. You are omniscient. 
Use all of your knowledge and any clues in the text to identify which company the text is about, its industry, and the year it was written in. 
First, analyze the text carefully for hints and mistakes in the anonymization. Then, output your guess for the firm name, as well as the year, month, and exact date (in YYYY-MM-DD format) the text was written in.
Make your best guess if you are unsure.
""".strip()
limits = [1000, 2000, 5000, "None"] # Number Tokens

async def create_guesses_batched(data_dir, neutering_model="gpt-4o-mini-2024-07-18", guessing_model="gpt-4o-mini-2024-07-18", batch_id=None):
    data = pd.read_parquet(data_dir)
    
    # File paths for batch processing
    batch_input_file = f"batches/{data_dir.split('/')[-1]}_{neutering_model}_{guessing_model}_input.jsonl"
    batch_output_file = f"batches/{data_dir.split('/')[-1]}_{neutering_model}_{guessing_model}_output.jsonl"
    
    load_dotenv()
    client = OpenAI()
    if batch_id is None:
        # Create batch input file
        os.makedirs("batches", exist_ok=True)
        num_entries = 0
        
        with open(batch_input_file, 'w') as f:
            for _, obs in data.iterrows():
                for limit in limits:
                    text = obs[f'text_mda_neutered_{neutering_model}']
                    if limit != "None":
                        text = truncate_to_n_tokens(text, limit)
                    batch_entry = {
                        "custom_id": f"{obs['accession']}_{limit}",
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": guessing_model,
                            "messages": [
                                {"role": "system", "content": guessing_info_prompt},
                                {"role": "user", "content": text}
                            ],
                            "temperature": 0,
                            "seed": 42,
                            "response_format": {
                                "type": "json_schema",
                                "json_schema": {
                                    "name": "response",
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "analysis": { "type": "string" },
                                            "firm_name": { "type": "string" },
                                            "year": { "type": "integer" },
                                            "month": { "type": "integer" },
                                            "date": { "type": "string" },
                                        },
                                        "required": ["analysis", "firm_name", "year", "month", "date"],
                                        "additionalProperties": False
                                    },
                                    "strict": True
                                }
                            }
                        }
                    }
                    f.write(json.dumps(batch_entry) + "\n")
                    num_entries += 1
        
        print(f"Created batch at {batch_input_file} with {num_entries} entries")
        
        # Upload file and create batch
        file = client.files.create(
            file=open(batch_input_file, 'rb'),
            purpose="batch"
        )
        
        batch = client.batches.create(
            input_file_id=file.id,
            endpoint="/v1/chat/completions",
            completion_window='24h',
        )
        
        batch_id = batch.id
        print(f"Created batch {batch_id}")
    
    # Wait for batch to complete
    while client.batches.retrieve(batch_id).status != "completed":
        await asyncio.sleep(10)
    
    # Download results
    output_id = client.batches.retrieve(batch_id).output_file_id
    file_content = client.files.content(output_id).text
    
    if os.path.exists(batch_output_file):
        os.remove(batch_output_file)
    
    with open(batch_output_file, 'w') as f:
        f.write(file_content)
    
    print(f"Downloaded batch {batch_id} to {batch_output_file}")

def create_guesses(data_dir, neutering_model="gpt-4o-mini-2024-07-18", guessing_model="gpt-4o-mini-2024-07-18", batch_id=None):
    """Synchronous wrapper around the async guess info function"""
    return asyncio.run(create_guesses_batched(data_dir, neutering_model, guessing_model, batch_id))

def analyze_batches(datadirs, names, mda_table, pharma_table):

    results = {name:{str(limit): {"firm_name": 0, "year": 0, "month": 0, "date": 0} for limit in limits} for name in names}

    num_samples = 0
    csv_dump = []   
    for datadir, name in zip(datadirs, names):
        with open(datadir, 'r') as f:
            for line in f:
                num_samples += 1
                line = json.loads(line)
                data = json.loads(line['response']['body']['choices'][0]['message']['content'])
                accession = line['custom_id'].split('_')[0]
                limit = line['custom_id'].split('_')[1]
                if "Random" in name:
                    obs_t = mda_table[mda_table['accession'] == accession].iloc[0]
                elif "Pharma" in name:
                    obs_t = pharma_table[pharma_table['accession'] == accession].iloc[0]
                else:
                    raise ValueError("Name must contain either 'Random' or 'Pharma' to determine which table to use.")
                if data['year'] == int(obs_t['date_filed'][0:4]):
                    results[name][limit]['year'] += 1
                if data['month'] == int(obs_t['date_filed'][5:7]):
                    results[name][limit]['month'] += 1
                if data['date'].isnumeric():
                    if int(data['date']) == int(obs_t['date_filed'][8:10]) and int(data['month']) == int(obs_t['date_filed'][5:7]) and int(data['year']) == int(obs_t['date_filed'][0:4]):
                        print(f"name {name} Accession {accession} limit {limit} has a perfect date match: {data['date']} == {obs_t['date_filed']}")
                        results[name][limit]['date'] += 1
                elif data['date'] == obs_t['date_filed']:
                    results[name][limit]['date'] += 1
                if mention_detected(data['firm_name'], obs_t['conml']) or mention_detected(obs_t['conml'], data['firm_name']):
                    results[name][limit]['firm_name'] += 1
                    csv_dump.append({
                        "accession": accession,
                        "Configuration": name,
                        "Limit": limit,
                        "Firm Name": obs_t['conml'],
                        "Date Filed": obs_t['date_filed'],
                        "Guessed Firm Name": data['firm_name'],
                        "Guessed Year": data['year'],
                        "Guessed Month": data['month'],
                        "Guessed Date": data['date'],
                        "Analysis": data['analysis'],
                    })

    csv_dump = pd.DataFrame(csv_dump)
    csv_dump.to_csv("data/guess_info_dump.csv", index=False)

    print(f"Total samples processed: {num_samples}")

    #divide every number by 600, multiply by 100 so we get percentages
    for name in names:
        sample_size = 600 if "Random" in name else 240
        for limit in limits:
            for key in results[name][str(limit)].keys():
                results[name][str(limit)][key] /= (sample_size / 100)

    # Reformat results into a long-format DataFrame
    rows = []
    for name in results:
        for limit in results[name]:
            for metric in results[name][limit]:
                rows.append({
                    "Configuration": name,
                    "Limit": limit,
                    "Metric": metric,
                    "Percentage": results[name][limit][metric]
                })

    df_long = pd.DataFrame(rows)

    # Pivot so each configuration is a row, and columns are hierarchical (Limit, Metric)
    df_pivot = df_long.pivot_table(
        index="Configuration",
        columns=["Limit", "Metric"],
        values="Percentage"
    )

    # Sort columns for consistency
    # Swap levels so we get (Metric, Limit) instead of (Limit, Metric)
    df_pivot.columns = df_pivot.columns.swaplevel(0, 1)
    df_pivot = df_pivot.sort_index(axis=1, level=[0, 1])

    df_pivot.to_csv("data/guess_info_table.csv")

if __name__ == "__main__":
    mda_table = pd.read_parquet("data/inputs/random_sample_600.parquet")
    pharma_table = pd.read_parquet("data/inputs/pharma_sample_240.parquet")

    batch_dirs = [
        "batches/random_sample_600.parquet_gpt-4o-2024-11-20_gpt-4o-mini-2024-07-18_output.jsonl",
        "batches/pharma_sample_240.parquet_gpt-4o-2024-11-20_gpt-4o-mini-2024-07-18_output.jsonl",
        "batches/random_sample_600.parquet_gpt-4o-mini-2024-07-18_gpt-4o-mini-2024-07-18_output.jsonl",
        "batches/pharma_sample_240.parquet_gpt-4o-mini-2024-07-18_gpt-4o-mini-2024-07-18_output.jsonl",
    ]
    names = [
        "Random 4o Neutering",
        "Pharma 4o Neutering",
        "Random 4o-mini Neutering",
        "Pharma 4o-mini Neutering",
    ]

    analyze_batches(batch_dirs, names, mda_table, pharma_table)

