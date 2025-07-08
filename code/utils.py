import hashlib
import tiktoken
import re
from linearmodels import PanelOLS

# This is a good function to detect mentions of a company in a text
# Company names often include some kind of suffix in formal writing that the LLM may not include
# This function does its best to remove these suffixes and match on the core name
def mention_detected(text, target_name):
    suffixes_to_remove = [
        'inc', 'corp', 'corporation', 'ltd', 'co', 'llc', 'group', 'plc', 'intl', 'incorporated',
        'holdings', 'limited', 'sa', 'nv', 'bv', 'ag', 'kg', 'gmbh', 'sarl', 'holding', 'international'
    ]
    target_name = target_name.lower()
    if "\"" in target_name:
        target_name = target_name.replace("\"", "")
    for suffix in suffixes_to_remove:
        target_name = target_name.replace(suffix, '').strip()
    
    option2 = target_name
    if "-" in target_name:
        option2 = option2.replace("-", " ")
    
    # Use word boundaries to match complete words only
    def has_word_match(text_lower, pattern):
        return bool(re.search(r'\b' + re.escape(pattern) + r'\b', text_lower))
    
    text_lower = text.lower()

    return (has_word_match(text_lower, target_name) or 
            (option2 != target_name and has_word_match(text_lower, option2)))

#This is a deterministic way to convert a string key into a seed for random number generation
def key_to_seed(key):
    seed = int(hashlib.md5(key.encode()).hexdigest(), 16) % 2 ** (32 - 1)
    return seed

#This converts text to a set token length for a given model
def truncate_to_n_tokens(text: str, n: int, model: str = "gpt-4o") -> str:
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    truncated_tokens = tokens[:n]
    truncated_text = enc.decode(truncated_tokens)
    return truncated_text

#This function creates the prompts for the growth factors based on an observation in one of the parquet file datasets. 
# dataset = pd.read_parquet("data/inputs/pharma_sample_50.parquet")
# for _, obs in dataset.iterrows():
#     for prompt_name, prompt in read_prompts(obs):

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

#When creating the pharma50 sample, I manually reviewed the LAB words identified by my text method. 
#This function reads the markdown file and returns the filtered LAB words. 
def pharma50_lab_words(file_path="data/inputs/pharma50.md"):
    output_lab_words = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into sections by company headers (##)
    sections = re.split(r'^## ', content, flags=re.MULTILINE)
    
    for section in sections[1:]:  # Skip the first section (header info)
        # Check if this section has "Strong LAB" verdict
        if "### Verdict: Strong LAB" in section or "### Verdict: Weak LAB (take)" in section:
            # Extract the accession number (first part before —)
            accession_match = re.search(r'^([^\s—]+)', section)
            if accession_match:
                accession_number = accession_match.group(1).strip()
                
                # Extract LAB words (words after '-' in the LAB Words section). 
                lab_words = []
                lab_words_match = re.search(r'### LAB Words:\s*\n(.*?)(?=\n###|$)', section, re.DOTALL)
                if lab_words_match:
                    lab_words_content = lab_words_match.group(1)
                    # Find all lines with '- word,' pattern and extract just the word. If I wanted to cancel a LAB word I made it -!word instead of - word
                    word_matches = re.findall(r'^- ([^,\s]+)', lab_words_content, re.MULTILINE)
                    lab_words = word_matches
                
                output_lab_words[accession_number] = lab_words
    
    return output_lab_words