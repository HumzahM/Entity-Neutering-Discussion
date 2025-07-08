# Entity-Neutering-Discussion
![NBER](https://github.com/HumzahM/Entity-Neutering-Discussion/blob/main/NBER.png)

By Bradford Levy and Humzah Merchant (UChicago '26) 

Shameless Plug: I'm applying for PhD programs in the fall related to Econometrics, ML, and Finance. 
I previously worked as an engineer at Apollo Global Management and with Dr. Larry Harris at USC Marshall. Please check me out / add me on [Linkedin](https://www.linkedin.com/in/humzahmerchant/)

## Overview
Everything was ran in Python 3.10.12, with the virtual enviroment in `requirements.txt` \
You may have noticed I used both the batch and async APIs redundantly. In my experience GPT-4o mini batches tend to take a long time (sometimes near the full 24 hours) to run. GPT-4o batches tend to be fairly fast, and Anthropic batches usually process within five minutes. When iterating or making changes to some experiments that involved GPT-4o mini, I would use the async API to get results faster.

### Slide 7: Entity Neutering
  - You can find the example in the slides `code/neuter_testing.py` file. Bradford presents a neutered version of prompt2, on Diamond Multimedia Systems Inc. 
  - Sometimes entity neutering outright fails. See `code/e_n_failing.py` where it misses "Biogen Inc." 
  - We neutered the mdas using `code/neuter_mdas.py` and they were saved to the parquet files in `data/inputs/`. 
### Slides 9 and 10: Does censorship work? 
```
You will receive a body of text which has been anonymized. You are omniscient. 
Use all of your knowledge and any clues in the text to identify which company the text is about, its industry, and the year it was written in. 
First, analyze the text carefully for hints and mistakes in the anonymization. Then, output your guess for the firm name, as well as the year, month, and exact date (in YYYY-MM-DD format) the text was written in.
Make your best guess if you are unsure.
```
  - See `code/guess_info.py` for the code that runs the guessing test. `code/guess_info_no_analysis.py` is almost identical except I use the OpenAI Async API and I remove the analysis step from the prompt. We tested four things: 
    1. Letting 4o neuter instead of 4o-mini. Samples neutered by 4o are much more difficult for 4o-mini to identify compared to samples neutered by 4o-mini.
    2. Variable token lengths. There seems to be the intuitive effect, though weak, that passing in more text makes it easier to identify the entity.
    3. Letting the model analyze before guessing or not. In general the analysis step seems to increase the firm identification rate by 50%. 
    4. If certain industries (such as pharma) would be more identifiable. It didn't appear so, or the effect was weak.
  - The outputs for this are in `data/guess_info_dump.csv`, `data/guess_info_table.csv`, and `data/guess_info_table_no_analysis.csv`. 
### Slides 16 and 17: Measuring Harmfulness
![Pharma50](https://github.com/HumzahM/Entity-Neutering-Discussion/blob/main/figures/pharma50.png)
![Random600](https://github.com/HumzahM/Entity-Neutering-Discussion/blob/main/figures/random600.png)
```
def read_prompts(obs):
    company = obs['conml']
    mda = obs['text_mda']
    neutered = obs['text_mda_neutered_gpt-4o-mini-2024-07-18']
    filing_date = obs['date_filed']
    fpe_year = int(obs['date_fpe'][0:4])
    mda_2000 = truncate_to_n_tokens(mda, 2000)
    neutered_2000 = truncate_to_n_tokens(neutered, 2000)

    prompt_1 = f"Using only information through {filing_date}, predict the main growth drivers for {company} in {fpe_year + 1}. Do not respond with saying you do not know."

    prompt_2 = f"""
The following is a summary of {company}'s performance during the year {fpe_year}.
```Summary```
{mda_2000}
```End of Summary```
The summary was publicly released on {filing_date}. Using only the information provided, predict the main growth drivers for {company} in {fpe_year+1}.""".strip()
    
    prompt_3 = f"""
The following is a summary of a company's performance during a financial year.
```Summary```
{neutered_2000}
```End of Summary```
Using only the information provided, predict the main growth drivers for the company the year after.""".strip()
    
    return [("baseline", prompt_1), ("context", prompt_2), ("e-n", prompt_3)]
``` 
   - These were ran using `code/anthropic_batched.py`, `code/openai_batched.py`, and `code/openai_fast.py`. All of the results for this are in `data/model_outputs/`. They are analyzed in `code/LAB_words_analysis.py`, using `LAB_words_analysis()` for random600 and `pharma50_analysis()` for that. Note, for pharma50, we ran each sample 8 times. 
   
### Slide 18: Measuring Helpfulness. 
![Judging](https://github.com/HumzahM/Entity-Neutering-Discussion/blob/main/figures/all_models_judging_results.png)
We presented the judging results on the samples created using random_sample_600.parquet. This is because that has both in and out of sample data, which is important to demonstrate that the effect is not a product of LAB.
  - See `code/response_judging.py`. We have three steps:
    1. `create_post_neutered_response`: This neuters the context responses so we can get a fair comparison.
    2. `judge_responses`: This uses GPT-4o to judge the responses, using the judging prompt. We then use GPT-4o Mini to parse the outputs. This may make it more unbiased towards A/B then forcing a structured output. 
    3. `plot_judging_results`: Plotting

```
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
```

The judging prompt is built on asking the judge to look for specificity and detail. Without this it actually favors the entity neutering responses because they just tend to start listing anything any company can do to grow (see the bad examples in the prompt) and the judging model accepts that. 

```
[User Question]
The following is a summary of a company's performance during a financial year.
Using only the information provided, predict the main growth drivers for the company the year after.

[The Start of Assistant A's Answer]
{first_response.strip()}
[The End of Assistant A's Answer]

[The Start of Assistant B's Answer]
{second_response.strip()}
[The End of Assistant B's Answer]
```