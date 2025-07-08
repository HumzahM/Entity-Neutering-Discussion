from collections import Counter
from nltk.corpus import stopwords
import json
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import seaborn as sns
from utils import pharma50_lab_words

#This functions takes something like "Hi, my name is Humzah."
#And returns ["hi", "my", "name", "is", "humzah"]
def clean_and_split_text(text):
    """Removes specified characters from text."""
    chars_to_remove = ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '"', "'", "®", "™", "●", "•", "’", "\n\n", "*", "·", "◦", "▪", '\u200b', '|', '\uf0b7', '-', '&']
    for char in chars_to_remove:
        text = text.replace(char, ' ')

    text = text.lower().split()
    
    #remove any word with an underscore (neutered) to keep the comparison fair for % of words that indicate LAB
    text = [word for word in text if '_' not in word]

    return text

#This identifies LAB words based on an min frequency in the T+1 MDA and a minimum increase in frequency from T to T+1
#The exclude list is in data/inputs/exclude_list.yaml. It has only two words
#Also exclude any nltk stop words, numbers (the next year often gets flagged), and the company name
def identify_LAB_words(obs_t, min_frequency, increase_factor, exclude_list):
    words_t = clean_and_split_text(obs_t["text_mda"])
    words_tp1 = clean_and_split_text(obs_t["text_mda_next"])

    word_freq_t = Counter(words_t) 
    word_freq_tp1 = Counter(words_tp1) 

    lab_words = []
    for word, count in word_freq_tp1.items():
        if count >= min_frequency*len(words_tp1):
            if word in word_freq_t:
                if word_freq_tp1[word] >= increase_factor * word_freq_t[word]: #still keep it a constant multiplication
                    lab_words.append(word)
            else:
                lab_words.append(word)

    clean_lab_words = []

    #This needs to be done or it skews the data very heavily
    company_name = obs_t['conml']
    company_name_parts = clean_and_split_text(company_name)

    for word in lab_words:
        if word.isnumeric() or word in stopwords.words('english') or word in company_name_parts or word in exclude_list:
            continue
        else:
            clean_lab_words.append(word)

    return clean_lab_words

#Goes through all the samples and identifies the LAB words in the responses. Outputs a data array for plotting
def LAB_words_analysis(datadirs, mda_table, min_frequency=0.001, increase_factor=10):
    
    model_info = pd.read_excel("data/inputs/lab_model_details.xlsx")
    models_insample_cutoff = {} #everything this date or before
    model_outsample_cutoff = {} #everything this date or after
    for _, row in model_info.iterrows():
        if row['Key'] != "" and row['Key'] is not None:
            try: #One year back means that the T+1 MD&A is being used to assess the knowledge cutoff
                models_insample_cutoff[row['Key']] = pd.to_datetime(row['Pre-training Knowledge Cutoff']) - pd.DateOffset(years=1)
                model_outsample_cutoff[row['Key']] = pd.to_datetime(row['Model Weights Commit'])
            except:
                pass

    cache = {}
    for datadir in datadirs:
        with open(datadir, 'r') as f:
            additional_data = json.load(f)
            cache.update(additional_data)
    print(f"Total samples: {len(cache)}")
    
    with open("data/inputs/exclude_list.yaml", "r") as file:
        exclude_list_data = yaml.safe_load(file)
        exclude_list = [entry["word"] for entry in exclude_list_data["excluded_words"]]

    data_array = []
    
    LAB_words_cache = {}

    found_words = {}

    total_response_length_words = 0
    for key in cache.keys():

        parts = key.split('_')

        accession = parts[0]
        llm = parts[1]
        query = parts[2]
        if query == "e-n":
            query = "Entity Neutering"
        if query == "context":
            query = "Context"
        if query == "baseline":
            query = "Baseline"

        obs_t = mda_table[(mda_table['accession'] == accession)].iloc[0]
        temp = parts[3]
        
        #This is a little bit debatable because ideally we would want the T MD&A to also be out of sample, not just the T+1
        if pd.to_datetime(obs_t['date_filed']) < models_insample_cutoff[llm]:
            sample = "In Sample"
        else:
            sample = "Out of Sample"
        
        if accession in LAB_words_cache:
            LAB_words = LAB_words_cache[accession]
        else:
            LAB_words = identify_LAB_words(obs_t, min_frequency, increase_factor, exclude_list)
            LAB_words_cache[accession] = LAB_words

        response_text = cache[key]['response']

        response = clean_and_split_text(response_text)

        total_response_length_words += len(response)

        total_bad = 0
        total_all = len(response)
        if len(LAB_words) > 0:
            for word in response:
                if word in LAB_words:
                    total_bad += 1
                    # if sample == "Out of Sample":
                    #     print(f"Found LAB word: {word} in response for sample {sample} company {obs_t['conml']} date filed {obs_t['date_filed']} llm {llm} query {query}")
                    if sample not in found_words:
                        found_words[sample] = {}
                    if word in found_words[sample]:
                        found_words[sample][word] += 1
                    else:
                        found_words[sample][word] = 1

        append_value = {
            'LLM': llm,
            'Sample': sample,
            'Query': query,
            'Percent_Bad': 100*(total_bad / total_all),
            'Is_Bad': 1 if total_bad > 0 else 0,
        }
        data_array.append(append_value)
            
    for sample, words in found_words.items():
        print(f"sample: {sample}")
        sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
        print(sorted_words)

    return data_array

#Plotting for the LAB words analysis
def plot(data_array, col='Percent_Bad', title=None, filename="figures/LAB.png"):
    df = pd.DataFrame(data_array)
    df['Sample'] = pd.Categorical(df['Sample'], categories=["In Sample", "Out of Sample"], ordered=True)
    sns.set_context("talk")
    plt.figure(figsize=(12, 6))

    hue_order = ['Baseline', 'Context', 'Entity Neutering']
    ax = sns.barplot(
        data=df,
        x="Sample",
        y=col,
        hue="Query",
        hue_order=hue_order,
        errorbar=None,
        capsize=0.1,
    )

    ax.set_xlabel('')
    ax.set_ylabel('')

    #=== Dotted horizontal line at out-of-sample mean ===
    out_sample_mean = df[df['Sample'] == 'Out of Sample'][col].mean()
    ax.axhline(out_sample_mean, linestyle='--', color='black')

    ax.legend(loc='upper right')

    sns.despine(top=True, right=True)
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, ms=7)
    ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, ms=7)

    #ylim = (0, 0.14)
    yticks = [0, out_sample_mean, 0.05, 0.1]
    ylabels = ["0%", "$\mu_{OOS}$", "0.05%", "0.1%"]
    if col == 'Percent_Bad':
        plt.ylabel("Percent of Words Indicating LAB")
    elif col == 'Is_Bad':
        plt.ylabel("Percent of Responses Indicating LAB")
    if title is not None:
        plt.title(title)
    plt.yticks(yticks, ylabels)
    plt.tight_layout()
    plt.savefig(filename, dpi=600)

def pharma50_analysis(datadirs, keys):
    data = {}
    for datadir in datadirs:
        with open(datadir, 'r') as f:
            additional_data = json.load(f)
            data.update(additional_data)

    lab_words = pharma50_lab_words()

    # Second pass: analyze only the valid samples
    samples = []
    for key in keys:
        for accession in lab_words.keys():
            for run in range(8):
                lab = False
                response = data[f"{accession}_{key}_{run}"]["response"]
                for lab_word in lab_words[accession]:
                    if lab_word in response.lower():
                        # if "e-n" in key or "context" in key:
                        #     print(f"Found LAB word: {lab_word} in response for company {accession} llm {key} run {run}")
                        samples.append({
                            "key": key,
                            "accession": accession,
                            "run": run,
                            "bad": 1,
                        })
                        lab = True
                        break
                if not lab:
                    samples.append({
                        "key": key,
                        "accession": accession,
                        "run": run,
                        "bad": 0,
                    })

    return_data = samples.copy()

    samples = pd.DataFrame(samples)
    num_samples = int(len(samples) / len(keys) / 8)

    samples = samples.groupby(['key', 'accession']).agg(
        Is_Bad=('bad', 'max'),
        Mean_Bad=('bad', 'mean')
    ).reset_index()

    samples = samples.groupby('key').agg(
        Is_Bad=('Is_Bad', 'sum'),
        Mean_Bad=('Mean_Bad', 'mean'),
        Mean_Bad_Given_IsBad=('Mean_Bad', lambda x: x[samples['Is_Bad'] == 1].mean())
    ).reset_index()
    samples['Is_Bad'] = samples['Is_Bad'] / num_samples

    print(f"{num_samples}/50 Pharma Samples, Ran 8 Times Each, Temp 0.5")
    print(samples.sort_values(by='Mean_Bad', ascending=False).reset_index(drop=True))

    return return_data

def graph_pharma50(data):

    df = pd.DataFrame(data)
    df[['model', 'query']] = df['key'].str.split('_', n=1, expand=True)
    query_map = {
        "baseline_0_5": "Baseline",
        "context_0_5": "Context",
        "e-n_0_5": "Entity Neutering",
        "baseline_0.5": "Baseline",
        "context_0.5": "Context",
        "e-n_0.5": "Entity Neutering",
    }
    df['query'] = df['query'].map(query_map)
    model_map = {
        "claude-3-5-haiku-20241022": "Claude 3.5 Haiku",
        "claude-3-5-sonnet-20241022": "Claude 3.5 Sonnet",
        "gpt-4o-2024-11-20": "GPT-4o",
        "gpt-4o-mini-2024-07-18": "GPT-4o Mini",
    }
    df['model'] = df['model'].map(model_map)
    custom_order = ["GPT-4o", "Claude 3.5 Sonnet", "Claude 3.5 Haiku", "GPT-4o Mini"]
    hue_order = ['Baseline', 'Context', 'Entity Neutering']
    df['model'] = pd.Categorical(df['model'], categories=custom_order, ordered=True)
    df = df.sort_values(by=['model', 'query'])

    sns.set_context("talk")
    plt.figure(figsize=(12, 6))

    ax = sns.barplot(
        data=df,
        x="model",
        y="bad",
        hue="query",
        hue_order=hue_order,
        errorbar=('ci', 99),
    )

    ax.set_xlabel('')
    ax.set_ylabel('Percent of Responses With LAB')
    ax.legend(loc='upper right')
    plt.yticks([0, 0.25, 0.5], ["0%", "25%", "50%"])
    sns.despine(top=True, right=True)
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, ms=7)
    ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, ms=7)
    plt.tight_layout()
    plt.savefig(f"figures/pharma50.png", dpi=300)

if __name__ == "__main__":
    datadirs = [
        "data/model_outputs/claude-3-5-haiku-20241022_random600.json",
        "data/model_outputs/claude-3-5-sonnet-20241022_random600.json",
        "data/model_outputs/gpt-4o-2024-11-20_random600.json",
        "data/model_outputs/gpt-4o-mini-2024-07-18_random600.json"
    ]

    mda_table = pd.read_parquet("data/inputs/random_sample_600.parquet")
    data = LAB_words_analysis(datadirs, mda_table, min_frequency=0.001, increase_factor=10)  
    plot(data, col='Percent_Bad', filename="figures/random600.png")

    data = pharma50_analysis(
        ["data/model_outputs/claude-3-5-sonnet-20241022_pharma50.json",
        "data/model_outputs/claude-3-5-haiku-20241022_pharma50.json",
         "data/model_outputs/gpt-4o-2024-11-20_pharma50.json",
         "data/model_outputs/gpt-4o-mini-2024-07-18_pharma50.json"],
         ["claude-3-5-haiku-20241022_baseline_0_5", "claude-3-5-haiku-20241022_context_0_5", "claude-3-5-haiku-20241022_e-n_0_5", 
          "gpt-4o-2024-11-20_baseline_0.5", "gpt-4o-2024-11-20_context_0.5", "gpt-4o-2024-11-20_e-n_0.5",
          "gpt-4o-mini-2024-07-18_baseline_0.5", "gpt-4o-mini-2024-07-18_context_0.5", "gpt-4o-mini-2024-07-18_e-n_0.5",
          "claude-3-5-sonnet-20241022_baseline_0_5", "claude-3-5-sonnet-20241022_context_0_5", "claude-3-5-sonnet-20241022_e-n_0_5",
          ] 
    )
    graph_pharma50(data)