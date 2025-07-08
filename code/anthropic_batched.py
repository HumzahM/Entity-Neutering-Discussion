#This script is identical in logic to openai_batched.py, but uses the Anthropic API

from dotenv import load_dotenv
from anthropic import Anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request
import time
import json
import pandas as pd
from utils import read_prompts

# Setup
print("Starting Code")
load_dotenv()
client = Anthropic()
# Sonnet 10/22 tends to have much higher LAB then sonnet 6/20
LLMS = ["claude-3-5-haiku-20241022", "claude-3-5-sonnet-20241022"]
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

    data_file = f"data/model_outputs/{llm}_{sample}.json"

    # Load existing cache
    cache = {}
    try:
        with open(data_file, 'r') as f:
            cache = json.load(f)
    except FileNotFoundError:
        pass

    # Create batch entries
    batch_requests = []
    for _, obs in dataset.iterrows():
        for prompt_name, prompt in read_prompts(obs):
            for run in range(num_runs):
                #Anthropic doesn't let you put a period in the custom_id
                temp_key = str(temperature).replace('.', '_')
                if num_runs > 1:
                    unique_key = f"{obs['accession']}_{llm}_{prompt_name}_{temp_key}_{run}"
                else:
                    unique_key = f"{obs['accession']}_{llm}_{prompt_name}_{temp_key}"
                if unique_key in cache:
                    continue
                #Anthropic also doesn't allow setting the seed
                batch_requests.append(
                    Request(
                        custom_id=unique_key,
                        params=MessageCreateParamsNonStreaming(
                            model=llm,
                            messages=[{"role": "user", "content": prompt}],
                            temperature=temperature,
                            max_tokens=1024,
                        )
                    )
                )
    
    if len(batch_requests) == 0:
        progress[llm]["main_id"] = "already done"
        print(f"No new requests for {llm} - already done")
        continue
    
    # Push batch to Anthropic
    message_batch = client.messages.batches.create(requests=batch_requests)
    progress[llm]["main_id"] = message_batch.id
    print(f"Created and pushed main batch for {llm} with batch ID {message_batch.id}")

# Monitor batch completion
print("Batches pushed! Watching for completion...")
while not all(progress[llm]["main_done"] for llm in LLMS):
    time.sleep(10)
    for llm in LLMS:   
        if not progress[llm]["main_done"]:
            batch_id = progress[llm]["main_id"]
            
            if batch_id == "already done":
                progress[llm]["main_done"] = True
                print(f"Main batch {llm} already done")
                continue
            
            batch_status = client.messages.batches.retrieve(batch_id).processing_status
            
            if batch_status == "failed":
                raise Exception(f"Batch {batch_id} failed")
            
            if batch_status == "ended":
                # Download batch results
                data_file = f"data/{llm}_{sample}.json"
                cache = {}
                try:
                    with open(data_file, 'r') as f:
                        cache = json.load(f)
                except FileNotFoundError:
                    pass

                # Process and save results
                for result in client.messages.batches.results(batch_id):
                    key = result.custom_id
                    if key in cache:
                        continue
                    
                    if result.result.type == "succeeded":
                        cache[key] = {}
                        cache[key]['response'] = result.result.message.content[-1].text
                    elif result.result.type == "errored":
                        raise Exception(f"Batch {batch_id} failed for {result.custom_id}")

                with open(data_file, 'w') as f:
                    json.dump(cache, f)

                progress[llm]["main_done"] = True
                print(f"Main batch {llm} done")
        
print("All done!")