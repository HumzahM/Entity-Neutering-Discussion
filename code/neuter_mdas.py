#This file has code to neuter the mdas both with the batch API and the OpenAI Async API.

from openai import OpenAI, AsyncOpenAI
import pandas as pd
from dotenv import load_dotenv
import json
import asyncio
import os

#This was pulled from the June 24, 2025 version of the paper. 
entity_neutering_prompt = """
Your role is to ANONYMIZE all text that is provided by the user. 
After you have anonymized a text, NOBODY, not even an expert financial analyst, should be able to use the text to identify the company or the industry the company operates in. 
For example, if the text is: The country's largest phone producer Apple had great phone-related earnings but Google did not in 2024, likely because of Apple's slogan Think Different, then you should ANONYMIZE it to: 
The country's largest product_type_1 producer Company_1 had great product_type_1 related earnings but Company_2 did not in time_1 likely because of Company_1's slogan slogan_1.
You should also ANONYMIZE any other information which one could use to identify the company or to make an educated guess about its identity.
Stock tickers are identifiers, are usually four or fewer capitalized letters (consider TIKR as a stand-in for an arbitrary ticker), and can be referenced in the text in the following formats; SYMBOL:TIKR, $TIKR, >TIKR, $ TIKR, SYMBOL TIKR, SYMBOL: TIKR, > TIKR. 
Make sure you ANONYMIZE TIKR to ticker_x. 
Also ANONYMIZE any other identifiers related to companies including the names of individuals, locations, industries, sectors, product names and types and generic product lines, services, times, years, dates and all numbers and percentages in the text, including units.
These should be replaced with name_x, location_x, industry_x, sector_x, product_x, product_type_x, product_line_x, service_x, time_x, year_x, date_x and number a, b, c, respectively. 
Also replace any website or internet links with link_x. 
You should never just delete an identifier; instead, always replace it with an anonymized analog. 
After you read and ANONYMIZE the text, you should output the anonymized text and nothing else.
""".strip()

async def neuter_texts_batch(data_dir, model, batch_id=None):
    data = pd.read_parquet(data_dir)
    
    if f'text_mda_neutered_{model}' in data.columns:
        print(f"{data_dir} already neutered with model {model}. Exiting.")
        return
    
    # File paths for batch processing
    batch_input_file = f"batches/{data_dir.split('/')[-1]}_{model}_input.jsonl"
    batch_output_file = f"batches/{data_dir.split('/')[-1]}_{model}_output.jsonl"
    
    load_dotenv()
    client = OpenAI()
    
    if batch_id is None:
        # Create batch input file
        os.makedirs("batches", exist_ok=True)
        num_entries = 0
        
        with open(batch_input_file, 'w') as f:
            for idx, text in enumerate(data['text_mda']):
                batch_entry = {
                    "custom_id": f"neuter_{idx}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": model,
                        "messages": [
                            {"role": "system", "content": entity_neutering_prompt},
                            {"role": "user", "content": text}
                        ],
                        "temperature": 0,
                        "seed": 42 
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
    
    # Parse results and update dataframe
    results = {}
    with open(batch_output_file, 'r') as f:
        for line in f:
            result = json.loads(line.strip())
            custom_id = result['custom_id']
            idx = int(custom_id.split('_')[1])
            neutered_text = result['response']['body']['choices'][0]['message']['content']
            results[idx] = neutered_text
    
    # Add neutered texts to dataframe in correct order
    neutered_texts = [results[i] for i in range(len(data))]
    data[f'text_mda_neutered_{model}'] = neutered_texts
    data.to_parquet(data_dir)
    
    print(f"Updated {data_dir} with neutered texts")

def neuter_texts_batched(data_dir, model, batch_id=None):
    """Synchronous wrapper around the async batch neutering function"""
    return asyncio.run(neuter_texts_batch(data_dir, model, batch_id))

async def neuter_single_text(client, text, idx, semaphore, model):
    """Process a single text with semaphore control"""
    async with semaphore:
        try:
            response = await client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": entity_neutering_prompt},
                    {"role": "user", "content": text}
                ],
                temperature=0,
                seed=42
            )
            return {
                "idx": idx,
                "response": response.choices[0].message.content,
                "success": True
            }
        except Exception as e:
            print(f"Error processing text {idx}: {e}")
            return {
                "idx": idx,
                "error": str(e),
                "success": False
            }

async def neuter_texts_async(data_dir, model, max_concurrent=50):
    """
    Asynchronously neuter texts using OpenAI API
    
    Args:
        data_dir: Path to parquet file containing the data
        model: OpenAI model to use (e.g., "gpt-4o-mini-2024-07-18")
        max_concurrent: Maximum number of concurrent requests
    """
    # Load data
    data = pd.read_parquet(data_dir)
    
    # Check if already processed
    if f'text_mda_neutered_{model}' in data.columns:
        print(f"{data_dir} already neutered with model {model}. Exiting.")
        return
    
    # Setup client
    load_dotenv()
    client = AsyncOpenAI()
    
    # Create semaphore for concurrency control
    semaphore = asyncio.Semaphore(max_concurrent)
    
    print(f"Starting async processing of {len(data)} texts with model {model}")
    
    # Create tasks for all texts
    tasks = []
    for idx, text in enumerate(data['text_mda']):
        task = neuter_single_text(client, text, idx, semaphore, model)
        tasks.append(task)
    
    # Execute all tasks concurrently
    print(f"Processing {len(tasks)} texts concurrently (max {max_concurrent} at once)")
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
    
    print(f"Completed: {len(successful_results)} successful, {len(failed_results)} failed")
    
    # Create results dictionary ordered by index
    results_dict = {}
    for result in successful_results:
        results_dict[result["idx"]] = result["response"]
    
    # Handle failed results (you might want to retry these or handle differently)
    for result in failed_results:
        if isinstance(result, dict) and "idx" in result:
            print(f"Failed to process text {result['idx']}: {result.get('error', 'Unknown error')}")
            # For now, we'll use the original text for failed cases
            results_dict[result["idx"]] = data.iloc[result["idx"]]['text_mda']
    
    # Create neutered texts list in correct order
    neutered_texts = []
    for i in range(len(data)):
        if i in results_dict:
            neutered_texts.append(results_dict[i])
        else:
            # Fallback to original text if somehow missing
            neutered_texts.append(data.iloc[i]['text_mda'])
    
    # Add neutered texts to dataframe and save
    data[f'text_mda_neutered_{model}'] = neutered_texts
    data.to_parquet(data_dir)
    
    print(f"Updated {data_dir} with neutered texts")

def neuter_texts_async_wrapper(data_dir, model, max_concurrent=50):
    """Synchronous wrapper around the async neutering function"""
    return asyncio.run(neuter_texts_async(data_dir, model, max_concurrent))

if __name__ == "__main__":
    neuter_texts_async_wrapper("data/inputs/pharma_sample_50.parquet", "gpt-4o-mini-2024-07-18")
    