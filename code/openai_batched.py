#Same logic as anthropic_batched.py. Uses the growth factor prompts.

from dotenv import load_dotenv
from openai import OpenAI
import time
import json
import os
import pandas as pd
from utils import key_to_seed
from utils import read_prompts

print("Starting Code")
load_dotenv()
client = OpenAI()
LLMS = ["gpt-4o-2024-11-20", "gpt-4o-mini-2024-07-18"]
os.makedirs(f"batches", exist_ok=True)
temperature = 0.5
temperature = 0.5
sample = "pharma50"

if sample == "random600":
    dataset = pd.read_parquet("data/inputs/random_sample_600.parquet")
    num_runs = 1
elif sample == "pharma240":
    dataset = pd.read_parquet("data/inputs/pharma_sample_240.parquet")
    num_runs = 1
elif sample == "pharma50":
    dataset = pd.read_parquet("data/inputs/pharma_sample_50.parquet")
    num_runs = 8
else:
    raise ValueError("Invalid sample type. Choose 'random' or 'pharma'.")

# Create and push batches for each model
progress = {llm: {"main_id": None, "main_done": False} for llm in LLMS}
for llm in LLMS:
    # Create batch file
    if sample == "random600":
        data_file = f"data/{llm}_random600.json"
        batch_file = f"batches/{llm}_random600_batch.json"
    elif sample == "pharma50":
        data_file = f"data/{llm}_pharma50.json"
        batch_file = f"batches/{llm}_pharma50_batch.json"
    elif sample == "pharma240":
        data_file = f"data/{llm}_pharma240.json"
        batch_file = f"batches/{llm}_pharma240_batch.json"
    
    if os.path.exists(batch_file):
        os.remove(batch_file)

    # Load existing cache
    cache = {}
    try:
        with open(data_file, 'r') as f:
            cache = json.load(f)
    except FileNotFoundError:
        pass

    # Create batch entries
    with open(batch_file, 'w') as f:
        for _, obs in dataset.iterrows():
            for prompt_name, prompt in read_prompts(obs):
                for run in range(num_runs):
                    if num_runs > 1:
                        unique_key = f"{obs['accession']}_{llm}_{prompt_name}_{temperature}_{run}"
                    else:
                        unique_key = f"{obs['accession']}_{llm}_{prompt_name}_{temperature}"
                    if unique_key in cache:
                        continue
                    batch_entry = {
                        "custom_id": unique_key,
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": llm,
                            "messages": [{"role": "user", "content": prompt}],
                            "temperature": temperature,
                            "seed": key_to_seed(unique_key),
                        }
                    }
                    f.write(json.dumps(batch_entry) + "\n")
    
    print(f"Created main batch for {llm} at {batch_file}")

    # Push batch to OpenAI
    file = client.files.create(
        file=open(batch_file, 'rb'),
        purpose="batch"
    )
    batch = client.batches.create(
        input_file_id=file.id,
        endpoint="/v1/chat/completions",
        completion_window='24h',
    )
    progress[llm]["main_id"] = batch.id
    print(f"Pushed batch {batch.id}")

# Monitor batch completion
print("Batches pushed! Watching for completion...")
while not all(progress[llm]["main_done"] for llm in LLMS):
    time.sleep(10)
    for llm in LLMS:   
        if not progress[llm]["main_done"]:
            batch_id = progress[llm]["main_id"]
            batch_status = client.batches.retrieve(batch_id).status
            
            if batch_status == "failed":
                raise Exception(f"Batch {batch_id} failed")
            
            if batch_status == "completed":
                # Download batch results
                output_id = client.batches.retrieve(batch_id).output_file_id
                file_content = client.files.content(output_id).text
                
                batch_response_file = f"batches/{llm}_main_batch_response.json"
                if os.path.exists(batch_response_file):
                    os.remove(batch_response_file)

                with open(batch_response_file, 'wb') as f:
                    for line in file_content:
                        f.write(line.encode('utf-8'))
                print(f"Downloaded batch {batch_id} to {batch_response_file}")

                # Process and save results
                if sample == "random":
                    data_file = f"data/{llm}_random600.json"
                elif sample == "pharma50":
                    data_file = f"data/{llm}_pharma50.json"
                elif sample == "pharma240":
                    data_file = f"data/{llm}_pharma240.json"
                cache = {}
                try:
                    with open(data_file, 'r') as f:
                        cache = json.load(f)
                except FileNotFoundError:
                    pass

                for line in open(batch_response_file, 'r'):
                    line = json.loads(line)
                    key = line['custom_id']
                    if key in cache:
                        continue
                    cache[key] = {}
                    cache[key]['response'] = line['response']['body']['choices'][0]['message']['content']

                with open(data_file, 'w') as f:
                    json.dump(cache, f)

                progress[llm]["main_done"] = True
                print(f"Main batch {llm} done")
        
print("All done!")