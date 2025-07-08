from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import asyncio
from utils import key_to_seed
from neuter_mdas import entity_neutering_prompt
import numpy as np
import seaborn as sns

judging_prompt = """
'''Task'''
Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. 
These responses were anonymized after generation. 
Define quality as how company specific and detailed the original response likely was before anonymization.
You should penalize responses that are generic and vague and have statements that could apply to many firms in many different years. 
An ideal response is one that could only apply to one specific company even after the anonymization. 
If a response could apply to many companies, it is likely a bad response.

'''Examples'''

[Examples of ideal responses]
1. "The company experienced significant growth in year_x, with a number_a% increase in product_type_1 revenues and a number_b% increase in product_type_2 revenues."
2. "The proposed reorganization to change the jurisdiction of incorporation from location_x to location_y, expected to be completed by date_x, might provide strategic and operational benefits"
3. "The company's proved reserves increased by number_b% in year_a, indicating successful drilling and completion activities. Continued efforts in these areas could further enhance reserves and production capacity in year_b."
4. "The company is aware of the seasonal trends affecting its business, particularly the lower volumes and revenue in the first quarter due to weather conditions and high deductible health plans."
[End examples of ideal responses]

[Examples of bad responses]
1. "Improvements in operational efficiency and performance can reduce costs and enhance profitability"
2. "The company is focused on innovation and expansion to drive shareholder value."
3. "Effective risk management strategies, including managing credit risk, interest rate risk, and liquidity risk, will be crucial for sustaining growth"
4. "Changes in laws, regulations, fiscal, monetary, and regulatory policies could create new opportunities for growth"
[End examples of bad responses]

The length of the response is not important and should not be used as a metric for quality.

'''Task'''

Begin your evaluation by comparing and constrating the two responses. 
Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. 
Be as objective as possible and focus on the content and specificity of the responses.
After providing your analysis, output your verdict about which assistant is better.  
""".strip()

parsing_prompt = """
You are given a judge's evaluation of two AI responses. Your job is to parse the judge's evaluation. Return just "A" or "B" based on the judge's evaluation.
""".strip()

#Neuter the context responses using the batch API
#In order to get a fair comparison
async def create_post_neutered_responses_indiv(datadir, name):
    batchdir_create = f"batches/{name}_create_responses_input.jsonl"
    batchdir_download = f"batches/{name}_download_responses_output.jsonl"
    load_dotenv()
    client = OpenAI()
    cache = {}
    with open(datadir, 'r') as f:
        additional_data = json.load(f)
        cache.update(additional_data)
    num_entries = 0
    with open(batchdir_create, 'w') as f:
        for key, item in cache.items():
            if "context" in key:
                new_key_name = key.replace("context", "context-post-neutered")
                num_entries += 1
                batch_entry = {
                    "custom_id": new_key_name,
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": "gpt-4o-mini",
                        "messages": [{"role": "system", "content": entity_neutering_prompt}, {"role": "user", "content": item['response']}],
                        "temperature": 0, 
                        "seed": key_to_seed(new_key_name)
                        }
                }
                f.write(json.dumps(batch_entry) + "\n")
    print(f"Created neutering batch at {batchdir_create} with len {num_entries}")

    file = client.files.create(
        file=open(batchdir_create, 'rb'),
        purpose="batch"
    )
    batch = client.batches.create(
        input_file_id=file.id,
        endpoint="/v1/chat/completions",
        completion_window='24h',
    )

    #wait for the batch to finish
    while (client.batches.retrieve(batch.id).status != "completed"):
        await asyncio.sleep(10)
    
    output_id = client.batches.retrieve(batch.id).output_file_id
    file = client.files.content(output_id).text
    
    if os.path.exists(batchdir_download):
        os.remove(batchdir_download)

    with open(batchdir_download, 'wb') as f:
        for line in file:
            f.write(line.encode('utf-8'))
    print(f"Downloaded batch {batch.id} to {batchdir_download}")

    for line in open(batchdir_download, 'r'):
        line = json.loads(line)
        response = line['response']['body']['choices'][0]['message']['content']
        new_key = line['custom_id']
        cache[new_key] = {"response": response}

    #save data
    with open(datadir, 'w') as f:
        json.dump(cache, f)
    
    print(f"All done with {name}")

#Wrapper to run the above function in parallel
def create_post_neutered_responses_batched(datadirs, names):
    async def create_post_neutered_responses_async(datadirs, names):
        tasks = [
            asyncio.create_task(create_post_neutered_responses_indiv(datadir, name))
            for datadir, name in zip(datadirs, names)
        ]

        await asyncio.gather(*tasks)
    asyncio.run(create_post_neutered_responses_async(datadirs, names))    

#Around 5% of the responses on the first pass failed. I think it was just the OpenAI batch API having issues the day I ran this. 
#So I just wrote a function to fill in the missing responses using the standard API.
def fill_missing_post_neutered_responses(datadir):
    """
    Check a single datadir for missing post-neutered responses and generate them
    using the standard OpenAI API with the same settings as the batch version.
    """
    load_dotenv()
    client = OpenAI()
    
    # Load existing data
    with open(datadir, 'r') as f:
        cache = json.load(f)
    
    # Find missing post-neutered responses
    missing_keys = []
    context_keys = [key for key in cache.keys() if "context" in key and "post-neutered" not in key]
    
    for context_key in context_keys:
        post_neutered_key = context_key.replace("context", "context-post-neutered")
        if post_neutered_key not in cache:
            missing_keys.append((context_key, post_neutered_key))
    
    print(f"Found {len(missing_keys)} missing post-neutered responses in {datadir}")
    
    if len(missing_keys) == 0:
        print("No missing responses found!")
        return
    
    # Generate missing responses one by one
    for i, (context_key, post_neutered_key) in enumerate(missing_keys):
        print(f"Processing {i+1}/{len(missing_keys)}: {post_neutered_key}")
        
        try:
            # Get the original response
            original_response = cache[context_key]['response']
            
            # Generate post-neutered response using same settings as batch
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": entity_neutering_prompt},
                    {"role": "user", "content": original_response}
                ],
                temperature=0,
                seed=key_to_seed(post_neutered_key)
            )
            
            # Extract the response content
            neutered_response = response.choices[0].message.content
            
            # Add to cache
            cache[post_neutered_key] = {"response": neutered_response}
            
            print(f"✓ Successfully generated response for {post_neutered_key}")
            
        except Exception as e:
            print(f"✗ Error generating response for {post_neutered_key}: {str(e)}")
            continue
    
    # Save updated cache
    with open(datadir, 'w') as f:
        json.dump(cache, f)
    
    print(f"✓ Saved updated data to {datadir}")
    print(f"Successfully filled {len([k for k in missing_keys if cache.get(k[1])])} missing responses")

#Judge responses comparing context vs e-n approaches.
def judge_responses(datadirs, output_name, mda_table, skip_judging=False):

    batchdir_create_judging = f"batches/judging_responses_input_{output_name}.jsonl"
    batchdir_download_judging = f"batches/judging_responses_output_{output_name}.jsonl"
    parsed_cache_file = f"batches/parsed_responses_cache_{output_name}.json"
    
    load_dotenv()
    client = OpenAI()
    
    # Setup model cutoffs for in/out-of-sample analysis
    model_info = pd.read_excel("data/lab_model_details.xlsx")
    models_insample_cutoff = {}  # everything this date or before
    model_outsample_cutoff = {}  # everything this date or after
    for _, row in model_info.iterrows():
        if row['Key'] != "" and row['Key'] is not None:
            try:
                models_insample_cutoff[row['Key']] = pd.to_datetime(row['Pre-training Knowledge Cutoff']) - pd.DateOffset(years=1)
                model_outsample_cutoff[row['Key']] = pd.to_datetime(row['Model Weights Commit'])
            except:
                pass
    
    # Step 1: Create and run judging batch (free-form responses)
    if not skip_judging:
        print(f"Creating judging batch for {output_name}")
        cache = {}

        # Load all responses from all models
        for datadir in datadirs:
            with open(datadir, 'r') as f:
                data = json.load(f)
                for key, item in data.items():
                    if "context-post-neutered" in key or "e-n" in key:
                        # Parse key: {accession}_{model}_{query_name}_{temp}
                        parts = key.split('_')
                        accession = parts[0]
                        model_name = parts[1]
                        query_type = parts[2]
                        temp = parts[3]
                        
                        # Create generalized key for grouping
                        generalized_key = f"{accession}_{model_name}_{temp}"
                        
                        if generalized_key not in cache:
                            cache[generalized_key] = {}
                        
                        # Store by query type
                        if "context-post-neutered" in query_type:
                            cache[generalized_key]['context-post-neutered'] = item['response']
                        elif query_type == "e-n":
                            cache[generalized_key]['e-n'] = item['response']

        # Create judging batch (free-form responses)
        num_entries = 0
        with open(batchdir_create_judging, 'w') as f:
            for key, responses in cache.items():
                if 'context-post-neutered' not in responses or 'e-n' not in responses:
                    raise ValueError(f"Missing responses for key {key}")
                
                # Parse key components
                parts = key.split('_')
                accession = parts[0]
                model_name = parts[1]
                temp = parts[2]
                
                # Determine A/B assignment based on run number
                # This way it is shuffled perfectly evenly and randomly
                context_is_A = (num_entries % 2 == 0)
                
                if context_is_A:
                    custom_id = f"{key}_A"
                    first_response = responses['context-post-neutered']
                    second_response = responses['e-n']
                else:
                    custom_id = f"{key}_B"
                    first_response = responses['e-n']
                    second_response = responses['context-post-neutered']
                
                user_prompt = f"""
[User Question]
The following is a summary of a company's performance during a financial year.
Using only the information provided, predict the main growth drivers for the company the year after.

[The Start of Assistant A's Answer]
{first_response.strip()}
[The End of Assistant A's Answer]

[The Start of Assistant B's Answer]
{second_response.strip()}
[The End of Assistant B's Answer]""".strip()
                
                num_entries += 1
                batch_entry = {
                    "custom_id": custom_id,
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": "gpt-4o",
                        "messages": [
                            {"role": "system", "content": judging_prompt}, 
                            {"role": "user", "content": user_prompt}
                        ],
                        "temperature": 0, 
                        "seed": key_to_seed(custom_id),
                        "logprobs": True
                    }
                }
                f.write(json.dumps(batch_entry) + "\n")
        
        print(f"Created judging batch at {batchdir_create_judging} with {num_entries} entries")

        # Upload and process judging batch
        file = client.files.create(
            file=open(batchdir_create_judging, 'rb'),
            purpose="batch"
        )
        batch = client.batches.create(
            input_file_id=file.id,
            endpoint="/v1/chat/completions",
            completion_window='24h',
        )

        # Wait for completion
        while client.batches.retrieve(batch.id).status != "completed":
            time.sleep(10)
        
        # Download results
        output_id = client.batches.retrieve(batch.id).output_file_id
        file_content = client.files.content(output_id).text
        
        if os.path.exists(batchdir_download_judging):
            os.remove(batchdir_download_judging)

        with open(batchdir_download_judging, 'w') as f:
            f.write(file_content)
        
        print(f"Downloaded judging batch {batch.id} to {batchdir_download_judging}")

    # Step 2: Parse responses using async OpenAI API with concurrency control
    print(f"Parsing judging responses for {output_name} using async API")
        
    # Check if cache exists and load it
    cached_parsed_responses = {}
    if os.path.exists(parsed_cache_file):
        print(f"Loading existing parsed response cache from {parsed_cache_file}")
        try:
            with open(parsed_cache_file, 'r') as f:
                cached_parsed_responses = json.load(f)
            print(f"Loaded {len(cached_parsed_responses)} cached parsed responses")
        except Exception as e:
            print(f"Error loading cache: {e}, proceeding without cache")
            cached_parsed_responses = {}
    
    async def parse_single_response(session, judging_response, custom_id):
        """Parse a single judging response using the async OpenAI API"""
        try:
            response = await session.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": parsing_prompt}, 
                    {"role": "user", "content": judging_response}
                ],
                temperature=0,
                seed=key_to_seed(judging_response)
            )
            
            parsed_result = response.choices[0].message.content.strip()
            return {
                "custom_id": custom_id,
                "parsed_response": parsed_result,
                "judging_response": judging_response
            }
        except Exception as e:
            print(f"Error parsing response for {custom_id}: {str(e)}")
            return {
                "custom_id": custom_id,
                "parsed_response": "ERROR",
                "judging_response": judging_response
            }
        
    async def parse_all_responses():
        """Parse all judging responses with concurrency control"""
        from openai import AsyncOpenAI
        async_client = AsyncOpenAI()
        
        # Read all judging responses
        judging_data = []
        for line in open(batchdir_download_judging, 'r'):
            line_data = json.loads(line)
            judging_response = line_data['response']['body']['choices'][0]['message']['content']
            custom_id = line_data['custom_id']
            judging_data.append((judging_response, custom_id))
        
        # Filter out responses that are already cached
        uncached_data = []
        cached_results = []
        
        for judging_response, custom_id in judging_data:
            if custom_id in cached_parsed_responses:
                # Use cached result
                cached_results.append({
                    "custom_id": custom_id,
                    "parsed_response": cached_parsed_responses[custom_id]["parsed_response"],
                    "judging_response": judging_response
                })
            else:
                # Need to parse this one
                uncached_data.append((judging_response, custom_id))
        
        print(f"Found {len(cached_results)} cached responses")
        print(f"Processing {len(uncached_data)} new judging responses with async API")
        
        if uncached_data:
            # Create semaphore for concurrency control (10 concurrent requests)
            semaphore = asyncio.Semaphore(10)
            
            async def parse_with_semaphore(judging_response, custom_id):
                async with semaphore:
                    return await parse_single_response(async_client, judging_response, custom_id)
            
            # Create tasks for uncached responses
            tasks = [
                parse_with_semaphore(judging_response, custom_id) 
                for judging_response, custom_id in uncached_data
            ]
            
            # Execute all tasks concurrently
            new_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Filter out exceptions and return successful results
            successful_new_results = []
            for result in new_results:
                if isinstance(result, Exception):
                    print(f"Task failed with exception: {result}")
                else:
                    successful_new_results.append(result)
            
            # Update cache with new results
            updated_cache = cached_parsed_responses.copy()
            for result in successful_new_results:
                updated_cache[result["custom_id"]] = {
                    "parsed_response": result["parsed_response"],
                    "judging_response": result["judging_response"]
                }
            
            # Save updated cache
            with open(parsed_cache_file, 'w') as f:
                json.dump(updated_cache, f, indent=2)
            print(f"Updated cache saved to {parsed_cache_file}")
            
            # Combine cached and new results
            all_results = cached_results + successful_new_results
        else:
            print("All responses were found in cache, no new parsing needed")
            all_results = cached_results
        
        return all_results
    
    # Run the async parsing
    parsing_results = asyncio.run(parse_all_responses())
    print(f"Total parsed responses: {len(parsing_results)}")

    # Step 3: Process results with detailed tracking and in/out-of-sample analysis
    print(f"Processing results for {output_name}")
    detailed_results = []
    
    # Create mapping from custom_id to parsed response
    parsed_responses = {}
    judging_responses = {}
    
    # Load from cache if it exists
    if os.path.exists(parsed_cache_file):
        print(f"Loading parsed responses from cache: {parsed_cache_file}")
        with open(parsed_cache_file, 'r') as f:
            cached_data = json.load(f)
        
        for custom_id, data in cached_data.items():
            parsed_responses[custom_id] = data["parsed_response"]
            judging_responses[custom_id] = data["judging_response"]
        
        print(f"Loaded {len(parsed_responses)} parsed responses from cache")
    
    for custom_id, parsed_response in parsed_responses.items():
        if parsed_response == "ERROR":
            print(f"Skipping failed parsing for {custom_id}")
            continue
            
        # Parse custom_id: {accession}_{model}_{temp}_{A/B}
        parts = custom_id.split('_')
        accession = parts[0]
        model_name = parts[1]
        temp = parts[2]
        context_position = parts[3]  # A or B
        
        # Skip invalid verdicts
        if parsed_response not in ["A", "B"]:
            print(f"Invalid verdict for {custom_id}: {parsed_response}")
            continue
        
        # Determine sample type (in-sample vs out-of-sample)
        sample_type = "Unknown"
        if model_name in models_insample_cutoff:
            try:
                obs_t = mda_table[mda_table['accession'] == accession].iloc[0]
                if pd.to_datetime(obs_t['date_filed']) < models_insample_cutoff[model_name]:
                    sample_type = "In Sample"
                else:
                    sample_type = "Out of Sample"
            except:
                print(f"Could not determine sample type for {custom_id}")
                sample_type = "Unknown"
        
        # Determine winner
        context_is_A = (context_position == "A")
        
        context_won = (context_is_A and parsed_response == "A") or (not context_is_A and parsed_response == "B")
        
        detailed_results.append({
            "custom_id": custom_id,
            "accession": accession,
            "model": model_name,
            "sample_type": sample_type,
            "Context": context_won,
            "Entity Neutering": not context_won,
            "parsed_verdict": parsed_response,
        })

    return detailed_results

def plot_judging_results(detailed_results, output_name):
    """
    Create vertical barplot showing Context win rates only:
    - In-Sample vs Out-of-Sample win rates
    - Y-axis starts at 45% with horizontal dashed line at 50% (No Pref)
    - Y-axis max set to minimize crowding of error bars
    """
    sns.set_context("talk")

    # Create DataFrame
    df = pd.DataFrame(detailed_results)

    # Melt to long format for seaborn
    df_long = df.melt(
        id_vars=['model', 'sample_type'],
        value_vars=['Context', 'Entity Neutering'],
        var_name='Prompt',
        value_name='Won'
    )
   
    # Single plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
   
    # Vertical barplot with sample type as x-axis
    colors = ["#e1812c", "#3a923a"]
    sns.barplot(
        data=df_long,
        x='sample_type',
        y='Won',
        hue='Prompt',
        hue_order=['Context', 'Entity Neutering'],
        errorbar=('ci', 99),
        ax=ax,
        saturation=1, #set saturation to 1 when using pre picked colors
        palette=colors,
    )
   
    # Set y-axis limits and add horizontal line at 50%
    plt.ylim(0.25, 0.75)
    plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7], ["30%", "40%", "No\nPref.", "60%", "70%"])
    ax.axhline(y=0.5, color='black', linestyle='--')
   
    ax.set_ylabel('Win Rate')
    ax.set_xlabel('')
    ax.legend(title='')
    
    sns.despine(top=True, right=True)
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, ms=7)
    ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, ms=7)
   
    plt.tight_layout()
    plt.savefig(f'figures/{output_name}_judging_results.png', dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    mda_table = pd.read_parquet("data/inputs/random_sample_600.parquet")
    datadirs = [
        "data/claude-3-5-haiku-20241022.json",
        "data/claude-3-5-sonnet-20241022.json",
        "data/gpt-4o-2024-11-20.json",
        "data/gpt-4o-mini-2024-07-18.json"
    ]

    detailed_results = judge_responses(
        datadirs,
        output_name="all_models",
        mda_table=mda_table,
        skip_judging=True
    )
    plot_judging_results(detailed_results, output_name="all_models")
    print("All done!")