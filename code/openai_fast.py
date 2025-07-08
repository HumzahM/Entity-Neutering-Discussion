#Most of the time for most reasonable batch sizes, using the Anthropic batch API is nearly as fast as hitting requests at the rate limit.
#Sometimes this is true for OpenAI, but especially with gpt-4o-mini I've noticed it can be very slow. 
#This file does exactly the same thing as openai_batched, but uses direct API calls instead of the batch endpoint.

import asyncio
import json
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from openai import AsyncOpenAI
from utils import key_to_seed
from utils import read_prompts

# Setup
print("Starting Code")
load_dotenv()
async_client = AsyncOpenAI()
LLMS = ["gpt-4o-2024-11-20", "gpt-4o-mini-2024-07-18"]
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

async def make_api_call(llm, prompt, unique_key, semaphore):
    """Make a single API call with semaphore control"""
    async with semaphore:
        try:
            response = await async_client.chat.completions.create(
                model=llm,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                seed=key_to_seed(unique_key),
            )
            return {
                "custom_id": unique_key,
                "response": response.choices[0].message.content,
                "success": True
            }
        except Exception as e:
            print(f"Error for {unique_key}: {e}")
            return {
                "custom_id": unique_key,
                "error": str(e),
                "success": False
            }

async def process_model(llm, semaphore):
    """Process all requests for a single model"""
    print(f"Processing model: {llm}")
    
    # Load existing cache
    data_file = f"data/model_outputs/{llm}_pharma50.json"
    cache = {}
    try:
        with open(data_file, 'r') as f:
            cache = json.load(f)
    except FileNotFoundError:
        pass
    
    # Collect all tasks for this model
    tasks = []
    total_requests = 0
    cached_requests = 0
    
    for _, obs in dataset.iterrows():
        for prompt_name, prompt in read_prompts(obs):
            for run in range(num_runs):
                if num_runs > 1:
                    unique_key = f"{obs['accession']}_{llm}_{prompt_name}_{temperature}_{run}"
                else:
                    unique_key = f"{obs['accession']}_{llm}_{prompt_name}_{temperature}"
                total_requests += 1
                
                if unique_key in cache:
                    cached_requests += 1
                    continue
                
                # Create task for this request
                task = make_api_call(llm, prompt, unique_key, semaphore)
                tasks.append(task)
    
    print(f"Model {llm}: {total_requests} total requests, {cached_requests} cached, {len(tasks)} to process")
    
    if not tasks:
        print(f"All requests for {llm} were cached, skipping API calls")
        return
    
    # Execute all tasks concurrently
    print(f"Starting {len(tasks)} concurrent requests for {llm}")
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
    
    print(f"Model {llm}: {len(successful_results)} successful, {len(failed_results)} failed")
    
    # Update cache with successful results
    updated_cache = cache.copy()
    for result in successful_results:
        updated_cache[result["custom_id"]] = {
            "response": result["response"]
        }
    
    # Save updated cache
    with open(data_file, 'w') as f:
        json.dump(updated_cache, f, indent=2)
    
    print(f"Results saved to {data_file}")

async def main():
    """Main async function"""
    print("Starting async processing...")
    
    # Create semaphore for concurrency control
    # Adjust the number (50) based on your rate limits and desired concurrency
    semaphore = asyncio.Semaphore(50)
    
    # Create tasks for each model
    model_tasks = [process_model(llm, semaphore) for llm in LLMS]
    
    # Process all models concurrently
    await asyncio.gather(*model_tasks)
    
    print("All processing complete!")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())