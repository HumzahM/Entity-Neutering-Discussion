#Identical in logic to guess_info.py, except this uses the Async API and it removes the analysis step from the output.

from openai import AsyncOpenAI
import pandas as pd
from dotenv import load_dotenv
import json
import asyncio
from utils import truncate_to_n_tokens, mention_detected
from pydantic import BaseModel

# Pydantic model for structured output
class GuessResponse(BaseModel):
    firm_name: str
    year: int
    month: int
    date: str

# Closely based off of the prompt found in the June 24, 2025 paper (Appendix B.2)
guessing_info_prompt = """
You will receive a body of text which has been anonymized. You are omniscient. 
Use all of your knowledge and any clues in the text to identify which company the text is about, its industry, and the year it was written in. 
Output your guess for the firm name, as well as the year, month, and exact date (in YYYY-MM-DD format) the text was written in.
Make your best guess if you are unsure.
""".strip()

limits = [1000, 2000, 5000, "None"]

async def make_api_call(client, text, unique_key, guessing_model, semaphore):
    """Make a single API call with semaphore control"""
    async with semaphore:
        try: #Unfortunately you cannot set a seed with this endpoint
            response = await client.responses.parse(
                model=guessing_model,
                input=[
                    {"role": "system", "content": guessing_info_prompt},
                    {"role": "user", "content": text}
                ],
                text_format=GuessResponse,
                temperature=0,
            )
            return {
                "custom_id": unique_key,
                "response": response.output_parsed.model_dump(),
                "success": True
            }
        except Exception as e:
            print(f"Error for {unique_key}: {e}")
            return {
                "custom_id": unique_key,
                "error": str(e),
                "success": False
            }

async def create_guesses_async(data_dir, neutering_model="gpt-4o-mini-2024-07-18", guessing_model="gpt-4o-mini-2024-07-18"):
    """Async version using direct API calls instead of batch processing"""
    data = pd.read_parquet(data_dir)
    
    # Output file for results
    output_file = f"batches/{data_dir.split('/')[-1]}_{neutering_model}_{guessing_model}_output_no_analysis.jsonl"
    
    load_dotenv()
    client = AsyncOpenAI()
    
    # Load existing cache
    cache = {}
    try:
        with open(output_file, 'r') as f:
            for line in f:
                result = json.loads(line)
                cache[result["custom_id"]] = result
    except FileNotFoundError:
        pass
    
    # Create semaphore for concurrency control (adjust based on rate limits)
    semaphore = asyncio.Semaphore(50)
    
    # Collect all tasks
    tasks = []
    total_requests = 0
    cached_requests = 0
    
    for _, obs in data.iterrows():
        for limit in limits:
            text = obs[f'text_mda_neutered_{neutering_model}']
            if limit != "None":
                text = truncate_to_n_tokens(text, limit)
            
            unique_key = f"{obs['accession']}_{limit}"
            total_requests += 1
            
            if unique_key in cache:
                cached_requests += 1
                continue
            
            # Create task for this request
            task = make_api_call(client, text, unique_key, guessing_model, semaphore)
            tasks.append(task)
    
    print(f"Total requests: {total_requests}, Cached: {cached_requests}, To process: {len(tasks)}")
    
    if not tasks:
        print("All requests were cached, skipping API calls")
        return
    
    # Execute all tasks concurrently
    print(f"Starting {len(tasks)} concurrent requests")
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Process results
    successful_results = []
    failed_results = []
    
    for result in results:
        if isinstance(result, Exception):
            print(f"Task failed with exception: {result}")
            failed_results.append(result)
        elif result["success"]:
            successful_results.append(result)
        else:
            failed_results.append(result)
    
    print(f"Successful: {len(successful_results)}, Failed: {len(failed_results)}")
    
    # Append new results to output file
    with open(output_file, 'a') as f:
        for result in successful_results:
            # Format result to match the expected batch output format
            formatted_result = {
                "custom_id": result["custom_id"],
                "response": {
                    "body": {
                        "choices": [
                            {
                                "message": {
                                    "content": json.dumps(result["response"])
                                }
                            }
                        ]
                    }
                }
            }
            f.write(json.dumps(formatted_result) + "\n")
    
    print(f"Results saved to {output_file}")

def create_guesses(data_dir, neutering_model="gpt-4o-mini-2024-07-18", guessing_model="gpt-4o-mini-2024-07-18"):
    """Synchronous wrapper around the async guess info function"""
    return asyncio.run(create_guesses_async(data_dir, neutering_model, guessing_model))

def analyze_batches(datadirs, names, mda_table, pharma_table):
    """Analysis function remains the same"""
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
                    })

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

    df_pivot.to_csv("data/guess_info_table_no_analysis.csv")

if __name__ == "__main__":
    mda_table = pd.read_parquet("data/inputs/random_sample_600.parquet")
    pharma_table = pd.read_parquet("data/inputs/pharma_sample_240.parquet")

    create_guesses("data/inputs/random_sample_600.parquet", "gpt-4o-mini-2024-07-18", "gpt-4o-mini-2024-07-18")
    
    # For analysis, use the async output files
    batch_dirs = [
        "batches/random_sample_600.parquet_gpt-4o-mini-2024-07-18_gpt-4o-mini-2024-07-18_output_no_analysis.jsonl",
    ]
    names = [
        "Random 4o-mini Neutering",
    ]

    analyze_batches(batch_dirs, names, mda_table, pharma_table)