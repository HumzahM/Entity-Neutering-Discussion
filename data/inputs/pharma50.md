# LAB Examples

These samples were initially identified by setting the Min Frequency in T+1 to 0.002 and setting them to be not present in T (9999x increase) \
We then tested on Llama 3.1 8B and 70B to find which samples had LAB. \
I then went through and did some in depth research into each sample to see if it was actually LAB or not. \
In general: 
- Dumb Noise: Noise
- The model using the unrevealed retail name of a drug that was well known in development and likely to be approved: Weak LAB
- The model hallucinating and/or pulling future information about doing well in late stage trials and FDA approvals: Strong LAB
- The model leaking information about partnerships between companies: Strong LAB
- Covid/Pandemic: Strong LAB

I took the Strong LAB examples, and then the Weak LAB that I believed were the strongest, to create a sample of 50. 

## 0000875045-21-000010 — BIOGEN INC. (2021)
### # Words: T MDA: 15344, T+1 MDA: 16070
### LAB Words:
- aduhelm, Count in T: 0, Count in T+1: 49
### Explanation:
Aduhelm was announced by the FDA on June 7, 2021. The announcement was very controversial. In February 2021 it was unlikely to have been approved, only after April 7 or April 28 it was under consideration. 
https://www.newyorker.com/news/daily-comment/the-fdas-extraordinary-approval-of-a-questionable-treatment-for-alzheimers?utm_source=chatgpt.com
Ctrl F November 6th in Here: 
https://oversightdemocrats.house.gov/sites/evo-subsites/democrats-oversight.house.gov/files/2022-12-29.COR%20%26%20E%26C%20Joint%20Staff%20Report%20re.%20Aduhelm.pdf?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2021-02-03, predict the main growth drivers for BIOGEN INC. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0025 (1/399)
Based on Biogen Inc.'s historical performance and industry trends up to 2021-02-03, here are some potential main growth drivers for the company in 2021:

1. **Tecfidera (Dimethyl Fumarate) Sales Growth**: Biogen's multiple sclerosis (MS) treatment Tecfidera is expected to continue its strong sales growth in 2021, driven by its market-leading position and increasing adoption in the MS market.
2. **Aducanumab (```Aduhelm```) Launch**: The launch of Aducanumab, a potential treatment for early Alzheimer's disease, is expected to be a significant growth driver for Biogen in 2021. Although the FDA approval was met with controversy, the company is likely to benefit from the treatment's potential to address a large and growing market.
3. **Vumerity (Diroximab) Sales Growth**: Vumerity, a treatment for relapsing forms of multiple sclerosis, is expected to continue its growth trajectory in 2021, driven by its strong efficacy and safety profile.
4. **Expansion of Biogen's Biosimilar Portfolio**: Biogen's biosimilar pipeline, including its partnerships with Samsung Bioepis and Mylan, is expected to contribute to the company's growth in 2021. The company's biosimilars are likely to gain traction in the market, particularly in the US and Europe.
5. **Increasing Adoption of Biosimilars in the US**: The US biosimilar market is expected to grow significantly in 2021, driven by the increasing adoption of biosimilars in the US market. Biogen's biosimilars, such as its partnership with Samsung Bioepis, are well-positioned to benefit from this trend.
6. **Growing Demand for MS Treatments**: The multiple sclerosis market is expected to continue growing in 2021, driven by an increasing prevalence of the disease and the introduction of new treatments. Biogen's MS portfolio, including Tecfidera and Vumerity, is well-positioned to benefit from this trend.
7. **Expansion of Biogen's Global Presence**: Biogen's global presence is expected to expand in 2021, driven by its partnerships and collaborations in emerging markets. The company's ability to establish a strong presence in these markets is likely to drive growth and increase its market share.

These growth drivers are based on historical trends and industry developments up to 2021-02-03. However, the actual performance of Biogen Inc. in 2021 may differ due to various factors, including changes in market conditions, regulatory developments, and competitive dynamics.

## 0000882095-20-000006 — GILEAD SCIENCES INC (2020)
### # Words: T MDA: 8458, T+1 MDA: 8924
### LAB Words:
- veklury, Count in T: 0, Count in T+1: 22
- covid-19, Count in T: 0, Count in T+1: 20
### Explanation:
The first press release referencing Remdesivir for COVID-19 was in February 26th 2020 (the day after the 10-K):
https://www.gilead.com/news/news-details/2020/gilead-sciences-initiates-two-phase-3-studies-of-investigational-antiviral-remdesivir-for-the-treatment-of-covid-19

The name Veklury was first used in May 2020. Emergency authorization was given on May 1st 2020. 
https://www.gilead.com/news/news-details/2020/gileads-investigational-antiviral-remdesivir-receives-us-food-and-drug-administration-emergency-use-authorization-for-the-treatment-of-covid-19

Humzah's Comment: Weak LAB
Bradford's Comment: Very few people thought Covid was a big deal in late February 2020. Strong LAB 
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-25, predict the main growth drivers for GILEAD SCIENCES INC in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0084 (3/358)
Based on publicly available information up to 2020-02-25, here are the main growth drivers for Gilead Sciences Inc. in 2020:

1. **HIV Treatment Market Growth**: Gilead Sciences is a leading player in the HIV treatment market, and the company's antiretroviral therapies (ARTs) are expected to continue driving growth in 2020. The global HIV treatment market is expected to grow at a CAGR of 4-5% from 2020 to 2025, driven by increasing demand for effective and affordable treatments.
2. **```COVID-19``` Treatment and Prevention**: Gilead Sciences' antiviral medication, remdesivir (```Veklury```), has shown promise in treating ```COVID-19```, a disease caused by the SARS-CoV-2 virus. The company has received emergency use authorization (EUA) from the US FDA for remdesivir, and it is expected to be a significant contributor to the company's growth in 2020.
3. **Epclusa and Harvoni Sales**: Gilead Sciences' hepatitis C virus (HCV) treatments, Epclusa and Harvoni, are expected to continue driving growth in 2020. The global HCV market is expected to grow at a CAGR of 10-15% from 2020 to 2025, driven by increasing demand for effective and curative treatments.
4. **Yescarta and Tecartus Sales**: Gilead Sciences' CAR-T cell therapies, Yescarta and Tecartus, are expected to drive growth in the company's oncology business in 2020. The global CAR-T cell therapy market is expected to grow at a CAGR of 20-25% from 2020 to 2025, driven by increasing demand for targeted cancer therapies.
5. **Incyte Collaboration**: Gilead Sciences' collaboration with Incyte Corporation on the development of selumetinib, a treatment for certain types of cancer, is expected to contribute to the company's growth in 2020.
6. **Expansion into Emerging Markets**: Gilead Sciences is expanding its presence in emerging markets, such as China, India, and Latin America, which is expected to drive growth in 2020.

These growth drivers are expected to contribute to Gilead Sciences' revenue growth in 2020, driven by the company's strong portfolio of HIV, HCV, and oncology treatments, as well as its expanding presence in emerging markets.

## 0000950170-22-002555 — Kodiak Sciences Inc. (2022)
### # Words: T MDA: 5142, T+1 MDA: 5134
### LAB Words:
- tarcocimab, Count in T: 0, Count in T+1: 22
### Explanation:
The first results of the DAZZLE study, as referenced, are from late April 2022. However, Tarcocimab was known to be in trial from 2019 or 2020. 
https://sigma.larvol.com/product.php?e1=747179&tab=newstrac&page=1
### Verdict: Weak LAB
### Input:
Using only information through 2022-03-01, predict the main growth drivers for Kodiak Sciences Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0033 (1/307)
Based on information available up to 2022-03-01, Kodiak Sciences Inc. is a clinical-stage biopharmaceutical company focused on developing novel therapeutics to treat retinal diseases. The main growth drivers for Kodiak Sciences Inc. in 2022 are predicted to be:

1. **Advancements in KSI-301 (```Tarcocimab``` Tedromer) Development**: KSI-301 is Kodiak's lead product candidate, an anti-VEGF antibody biopolymer conjugate for the treatment of age-related macular degeneration (AMD), diabetic macular edema (DME), and retinal vein occlusion (RVO). Positive results from ongoing clinical trials, such as the DAZZLE study, are expected to drive growth and investor interest.

2. **Expansion of Clinical Trials**: Kodiak Sciences plans to initiate additional clinical trials for KSI-301, including a Phase 3 study in DME and a Phase 2 study in RVO. The expansion of clinical trials will increase the company's visibility and credibility in the market, driving growth and attracting potential partners.

3. **Strategic Partnerships and Collaborations**: Kodiak Sciences may explore strategic partnerships and collaborations with other biopharmaceutical companies to accelerate the development and commercialization of KSI-301. Such partnerships could provide significant funding and expertise, driving growth and increasing the company's market value.

4. **Growing Demand for Retinal Disease Treatments**: The prevalence of retinal diseases, such as AMD and DME, is increasing globally, driven by aging populations and rising rates of diabetes. Kodiak Sciences is well-positioned to capitalize on this growing demand with its innovative treatment options, driving growth and revenue.

5. **Increased Investor Interest**: Kodiak Sciences' innovative approach to treating retinal diseases, combined with positive clinical trial results, is expected to attract increased investor interest and funding. This will provide the necessary resources to drive growth and advance the company's pipeline of product candidates.

These growth drivers are expected to contribute to Kodiak Sciences' growth and success in 2022, as the company continues to advance its pipeline of innovative retinal disease treatments.

## 0000950170-22-004842 — IGM Biosciences, Inc. (2022)
### # Words: T MDA: 6480, T+1 MDA: 5671
### LAB Words:
- sanofi, Count in T: 0, Count in T+1: 19
### Explanation:
Sanofi and IGM Biosciences announced their partnership on day of the 10-K release, March 29th 2022. 
https://www.sanofi.com/en/media-room/press-releases/2022/2022-03-29-05-00-00-2411497?utm_source=chatgpt.com

Sanofi is heavily mentioned in Item 1 and Special Introduction for the 10-K, but not the MD&A. 
https://www.sec.gov/ix?doc=/Archives/edgar/data/0001496323/000095017022004842/igms-20211231.htm

It officially began on May 6th, 2022
https://www.globenewswire.com/news-release/2022/05/06/2437701/0/en/IGM-Biosciences-Announces-Closing-of-Global-Collaboration-Agreement-with-Sanofi.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2022-03-29, predict the main growth drivers for IGM Biosciences, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0033 (1/306)
Based on information available up to 2022-03-29, IGM Biosciences, Inc. is a biotechnology company focused on developing IgM antibodies for the treatment of various diseases, including cancer and infectious diseases. The main growth drivers for IGM Biosciences, Inc. in 2022 are likely to be:

1. **Advancements in the pipeline**: IGM Biosciences has a robust pipeline of IgM antibody candidates in various stages of development. Progress in these programs, particularly the lead candidate IGM-2323, a CD20 x CD3 bispecific IgM antibody for the treatment of B-cell non-Hodgkin's lymphoma, is expected to drive growth.
2. **Partnerships and collaborations**: IGM Biosciences has established partnerships with major pharmaceutical companies, such as ```Sanofi```, to develop and commercialize its IgM antibody candidates. These collaborations are likely to provide significant funding and expertise, driving growth and expansion.
3. **Increased adoption of IgM antibodies**: As the company's IgM antibody candidates advance through clinical trials, there is a growing recognition of the potential benefits of IgM antibodies over traditional IgG antibodies. This increasing adoption is expected to drive growth and interest in IGM Biosciences' technology.
4. **Expansion of the company's platform**: IGM Biosciences is continuously expanding its platform to include new technologies and capabilities, such as its IgM antibody-drug conjugate (ADC) platform. This expansion is likely to drive growth by enabling the company to develop new and innovative therapies.
5. **Growing demand for cancer treatments**: The global cancer treatment market is growing rapidly, driven by an increasing incidence of cancer and a growing demand for effective treatments. IGM Biosciences' focus on developing cancer therapies, particularly its lead candidate IGM-2323, positions the company to capitalize on this growing demand.

Overall, IGM Biosciences' growth in 2022 is expected to be driven by advancements in its pipeline, partnerships and collaborations, increasing adoption of IgM antibodies, expansion of its platform, and growing demand for cancer treatments.

## 0000950170-23-005713 — Verve Therapeutics, Inc. (2023)
### # Words: T MDA: 8824, T+1 MDA: 7391
### LAB Words:
- lilly, Count in T: 0, Count in T+1: 16
### Explanation:
Verve and Lilly announced their partnership on June 15, 2023. 
https://www.globenewswire.com/news-release/2023/06/15/2688718/0/en/Verve-Establishes-Global-Collaboration-with-Lilly-to-Advance-Verve-s-In-Vivo-Gene-Editing-Program-Targeting-Lp-a-for-the-Treatment-of-Atherosclerotic-Cardiovascular-Disease.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2023-03-02, predict the main growth drivers for Verve Therapeutics, Inc. in 2023. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0033 (1/303)
Based on information available up to 2023-03-02, the main growth drivers for Verve Therapeutics, Inc. in 2023 are expected to be:

1. **Advancements in Gene Editing Technologies**: Verve Therapeutics is a biotechnology company focused on developing gene editing therapies for cardiovascular diseases. The company's growth is likely to be driven by advancements in its proprietary gene editing technologies, including its CRISPR-Cas9 and base editing platforms.

2. **Progress in Clinical Trials**: Verve's lead program, VERVE-101, is a gene editing therapy designed to treat heterozygous familial hypercholesterolemia (HeFH), a genetic disorder that causes high cholesterol. The company's growth is expected to be driven by progress in clinical trials for VERVE-101, including the initiation of Phase 1 clinical trials and the presentation of data from these trials.

3. **Expansion of Pipeline**: Verve Therapeutics is also expected to expand its pipeline of gene editing therapies for cardiovascular diseases, including programs targeting other genetic disorders that cause high cholesterol and cardiovascular disease. The company's growth is likely to be driven by the advancement of these programs into preclinical and clinical development.

4. **Strategic Partnerships and Collaborations**: Verve Therapeutics has established partnerships with leading biotechnology and pharmaceutical companies, including Beam Therapeutics and Eli ```Lilly```. The company's growth is expected to be driven by the expansion of these partnerships and the establishment of new collaborations to accelerate the development of its gene editing therapies.

5. **Increased Investment in Gene Editing Research**: The gene editing market is rapidly growing, with increasing investment in research and development. Verve Therapeutics is well-positioned to benefit from this trend, with its focus on developing gene editing therapies for cardiovascular diseases. The company's growth is likely to be driven by increased investment in gene editing research and the growing recognition of the potential of gene editing to treat genetic diseases.

## 0000950170-23-008440 — Monte Rosa Therapeutics, Inc. (2023)
### # Words: T MDA: 4491, T+1 MDA: 3929
### LAB Words:
- roche, Count in T: 0, Count in T+1: 8
### Explanation:
Monte Rosa and Roche announced their partnership on October 17, 2023.
https://www.globenewswire.com/news-release/2023/10/17/2761334/0/en/Monte-Rosa-Therapeutics-Announces-Strategic-Collaboration-with-Roche-to-Discover-Novel-Molecular-Glue-Degraders-Targeting-Cancer-and-Neurological-Diseases.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2023-03-16, predict the main growth drivers for Monte Rosa Therapeutics, Inc. in 2023. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0033 (1/307)
Based on information available up to 2023-03-16, Monte Rosa Therapeutics, Inc. is a biotechnology company focused on developing novel therapies for the treatment of cancer and other diseases. The main growth drivers for Monte Rosa Therapeutics, Inc. in 2023 are likely to be:

1. **Advancements in its lead program, GSPT1 inhibitor**: Monte Rosa's lead program is focused on developing a GSPT1 inhibitor, which has shown promise in preclinical studies for the treatment of cancer. Progress in this program, including the initiation of clinical trials, is expected to drive growth and investor interest.

2. **Expansion of its pipeline**: Monte Rosa has a pipeline of programs targeting various molecular glue targets. The advancement of these programs into preclinical and clinical development is expected to drive growth and increase the company's chances of success.

3. **Strategic partnerships and collaborations**: Monte Rosa has established partnerships with leading pharmaceutical companies, including ```Roche```, to develop its molecular glue platform. The expansion of these partnerships or the establishment of new collaborations is expected to drive growth and provide access to additional resources and expertise.

4. **Increased investment in research and development**: Monte Rosa is expected to continue investing in research and development to advance its pipeline and expand its molecular glue platform. This investment is expected to drive growth and increase the company's chances of success.

5. **Growing interest in molecular glue therapeutics**: Molecular glue therapeutics is a rapidly growing field, and Monte Rosa is one of the leading companies in this space. Growing interest in this field is expected to drive growth and increase investor interest in the company.

Overall, Monte Rosa Therapeutics, Inc.'s growth in 2023 is expected to be driven by advancements in its lead program, expansion of its pipeline, strategic partnerships and collaborations, increased investment in research and development, and growing interest in molecular glue therapeutics.

## 0001047469-19-000725 — MADRIGAL PHARMACEUTICALS, INC. (2019)
### # Words: T MDA: 3678, T+1 MDA: 4487
### LAB Words:
- resmetirom, Count in T: 0, Count in T+1: 21
### Explanation:
Strong Phase 2 trials were announced in 2017
https://www.globenewswire.com/news-release/2017/12/06/1233905/0/en/Madrigal-s-MGL-3196-Achieves-Primary-Endpoint-in-Patients-with-Biopsy-proven-Non-alcoholic-Steatohepatitis-NASH-in-Phase-2-Clinical-Trial.html?utm_source=chatgpt.com

Phase 3 trials were not announced until March 28th 2019
https://www.globenewswire.com/news-release/2019/03/28/1781097/0/en/Madrigal-Pharmaceuticals-Initiates-Phase-3-Multinational-Double-Blind-Randomized-Placebo-Controlled-Study-of-MGL-3196-resmetirom-in-Patients-With-Non-Alcoholic-Steatohepatitis-NASH.html?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2019-02-27, predict the main growth drivers for MADRIGAL PHARMACEUTICALS, INC. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0043 (1/235)
Based on information available up to 2019-02-27, the main growth drivers for Madrigal Pharmaceuticals, Inc. in 2019 are expected to be:

1. **MGL-3196 (```Resmetirom```)**: Madrigal's lead compound, a thyroid hormone receptor beta (THR-β) agonist, has shown promising results in Phase 2 clinical trials for the treatment of non-alcoholic steatohepatitis (NASH) and heterozygous familial hypercholesterolemia (HeFH). Positive results from these trials are expected to drive growth and investor interest in 2019.

2. **NASH Market Opportunity**: The NASH market is expected to grow significantly in the coming years, driven by increasing prevalence and a lack of effective treatments. Madrigal's MGL-3196 is well-positioned to capitalize on this opportunity, with potential for significant revenue growth if approved.

3. **Partnership and Licensing Opportunities**: Madrigal may explore partnership and licensing opportunities for MGL-3196, which could provide additional revenue streams and help accelerate the development and commercialization of the compound.

4. **Expansion of Clinical Trials**: Madrigal is expected to initiate new clinical trials for MGL-3196 in 2019, including a Phase 3 trial for NASH, which will help drive growth and increase visibility for the company.

5. **Increased Investor Interest**: Positive results from clinical trials and the growing NASH market opportunity are expected to attract increased investor interest in Madrigal, driving growth in the company's stock price and market capitalization.

These growth drivers are based on information available up to 2019-02-27 and may not reflect any subsequent developments or updates.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0032 (1/313)
Based on publicly available information through 2019-02-27, here are some potential growth drivers for Madrigal Pharmaceuticals, Inc. in 2019:

1. **NASH (Non-Alcoholic Steatohepatitis) Treatment**: Madrigal's lead product candidate, MGL-3196 (```resmetirom```), is being developed for the treatment of NASH, a growing market with a significant unmet medical need. The company's focus on NASH could drive growth as the market for NASH treatments is expected to expand in the coming years.
2. **Partnership with Novartis**: In 2018, Madrigal announced a partnership with Novartis to develop and commercialize MGL-3196. This partnership could provide access to Novartis' global resources, expertise, and commercial infrastructure, potentially accelerating Madrigal's growth.
3. **Clinical Trial Progress**: Madrigal's clinical trials for MGL-3196 are ongoing, and the company has reported positive interim results. Successful completion of these trials and the potential for regulatory approvals could drive growth as the company advances its product candidate through the development pipeline.
4. **Oral Small Molecule Therapies**: Madrigal's focus on oral small molecule therapies could provide a competitive advantage in the NASH market, which is expected to be a key area of focus for pharmaceutical companies in the coming years.
5. **Strong Cash Position**: As of 2019-02-27, Madrigal had a cash position of approximately $143 million, which could provide the company with the necessary resources to continue advancing its product candidate and executing its business strategy.
6. **Growing Awareness of NASH**: Increasing awareness of NASH as a significant health issue could drive growth for Madrigal as the company's product candidate is positioned to address this unmet medical need.

These factors could contribute to Madrigal Pharmaceuticals' growth in 2019, but it's essential to note that the company's actual performance may differ from these predictions.

**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0030 (1/330)
Based on publicly available information through 2019-02-27, here are some potential growth drivers for Madrigal Pharmaceuticals, Inc. in 2019:

1. **NASH (Non-Alcoholic Steatohepatitis) Pipeline**: Madrigal's lead product candidate, MGL-3196 (```resmetirom```), is being developed for the treatment of NASH, a growing market with a high unmet medical need. The company's focus on NASH could drive growth as the market size is expected to expand in the coming years.
2. **Phase 3 Clinical Trials**: Madrigal is planning to initiate a Phase 3 clinical trial for MGL-3196 in NASH patients with liver biopsy-confirmed NASH. Successful completion of this trial could lead to FDA approval and significant revenue growth.
3. **Partnerships and Collaborations**: Madrigal has partnered with several organizations, including the National Institutes of Health (NIH) and the University of California, San Diego, to support the development of MGL-3196. These partnerships could provide access to new technologies, expertise, and funding, driving growth.
4. **Cash Position**: As of 2019-02-27, Madrigal had approximately $120 million in cash and cash equivalents. This cash position could provide the company with the necessary resources to fund its operations, including clinical trials, and drive growth.
5. **Competitive Advantage**: Madrigal's MGL-3196 has a unique mechanism of action, which may provide a competitive advantage in the NASH market. The company's focus on a single, high-potential product candidate could allow it to concentrate resources and drive growth.
6. **Growing Market for NASH Treatments**: The NASH market is expected to grow significantly in the coming years, driven by the increasing prevalence of the disease and the lack of effective treatments. Madrigal's focus on this market could position the company for growth as the market expands.

These factors could contribute to Madrigal Pharmaceuticals' growth in 2019, but it's essential to note that the company's actual performance may differ from these predictions.

## 0001048477-22-000012 — BIOMARIN PHARMACEUTICAL INC (2022)
### # Words: T MDA: 6660, T+1 MDA: 5930
### LAB Words:
- roctavian, Count in T: 0, Count in T+1: 17
### Explanation:
First approved in Europe (before FDA) in August 2022
https://investors.biomarin.com/news/news-details/2022/First-Gene-Therapy-for-Adults-with-Severe-Hemophilia-A-BioMarins-ROCTAVIAN-valoctocogene-roxaparvovec-Approved-by-European-Commission-EC-08-24-2022/?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2022-02-25, predict the main growth drivers for BIOMARIN PHARMACEUTICAL INC in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0044 (1/228)
Based on information available up to 2022-02-25, the main growth drivers for BioMarin Pharmaceutical Inc. in 2022 are expected to be:

1. **Voxzogo (Vosoritide)**: BioMarin's Voxzogo, a treatment for achondroplasia, the most common form of dwarfism, was approved by the FDA in November 2021. The company expects significant revenue growth from this new product launch in 2022.

2. **Valoctocogene Roxaparvovec (```Roctavian```)**: BioMarin's gene therapy for severe hemophilia A, Valoctocogene Roxaparvovec, is expected to be a major growth driver in 2022. Although the FDA delayed approval in 2021, the company is working to address regulatory concerns and anticipates approval and commercialization in 2022.

3. **Naglazyme and Kuvan**: BioMarin's existing products, Naglazyme (for MPS VI) and Kuvan (for phenylketonuria), are expected to continue generating significant revenue in 2022, driven by steady demand and potential label expansions.

4. **Expansion into Emerging Markets**: BioMarin plans to expand its presence in emerging markets, such as Latin America, Asia, and the Middle East, which could contribute to growth in 2022.

5. **Research and Development Pipeline**: BioMarin's R&D pipeline includes several promising candidates, including BMN 307 (for phenylketonuria) and BMN 331 (for hereditary angioedema). Progress in these programs could drive growth and investor interest in 2022.

These growth drivers are expected to contribute to BioMarin's revenue and earnings growth in 2022, despite potential challenges and uncertainties in the biopharmaceutical industry.

## 0001060736-20-000006 — SEATTLE GENETICS INC /WA (2020)
### # Words: T MDA: 9017, T+1 MDA: 10652
### LAB Words:
- tukysa, Count in T: 0, Count in T+1: 39
- merck, Count in T: 0, Count in T+1: 34
### Explanation:
Tucatinib was filed for approval on Decemeer 23rd 2019. These mention it is still in approval, which is accurate
https://www.drugs.com/history/tukysa.html

Seattle Genetics and Merck began to work together in September 2020:
https://www.merck.com/news/seattle-genetics-and-merck-announce-two-strategic-oncology-collaborations/?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2020-02-06, predict the main growth drivers for SEATTLE GENETICS INC /WA in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0116 (3/259)
Based on information available up to 2020-02-06, the main growth drivers for Seattle Genetics, Inc. (SGEN) in 2020 are expected to be:

1. **Adcetris (Brentuximab Vedotin) Sales Growth**: Adcetris, a monoclonal antibody-based therapy for certain types of lymphoma, has been a key revenue driver for Seattle Genetics. Continued growth in Adcetris sales, particularly in the US and international markets, is expected to contribute to the company's revenue growth in 2020.

2. **Padcev (Enfortumab Vedotin) Launch and Adoption**: Padcev, a monoclonal antibody-based therapy for bladder cancer, received FDA approval in December 2019. The launch and adoption of Padcev are expected to drive revenue growth for Seattle Genetics in 2020, particularly in the US market.

3. **```Tukysa``` (Tucatinib) Approval and Launch**: ```Tukysa```, a small molecule inhibitor for breast cancer, was under review by the FDA as of 2020-02-06. Approval and launch of ```Tukysa``` in 2020 could provide an additional growth driver for Seattle Genetics.

4. **Collaboration and Licensing Agreements**: Seattle Genetics has a history of collaborating with other biopharmaceutical companies to develop and commercialize its products. The company may continue to enter into new collaboration and licensing agreements in 2020, which could provide additional revenue streams and growth opportunities.

5. **Pipeline Advancements**: Seattle Genetics has a robust pipeline of products in various stages of development. Advancements in the company's pipeline, including the initiation of new clinical trials and the presentation of positive data, could drive growth and increase investor confidence in 2020.

These growth drivers are based on publicly available information and should not be considered as investment advice.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0058 (2/343)
Based on publicly available information up to 2020-02-06, here are some potential growth drivers for Seattle Genetics, Inc. (now known as Seagen Inc.) in 2020:

1. **ADCETRIS (Brentuximab Vedotin) growth**: ADCETRIS, a cancer treatment for Hodgkin lymphoma and non-Hodgkin lymphoma, was approved in 2011. In 2019, the company reported strong sales growth for ADCETRIS, with revenue increasing by 24% year-over-year. This trend is likely to continue in 2020, driven by increasing adoption and expanding indications.
2. **ADC-based pipeline progress**: Seattle Genetics has a robust pipeline of ADC-based therapies in various stages of development, including tucatinib (```Tukysa```) for HER2-positive breast cancer, enfortumab vedotin (Padcev) for urothelial cancer, and ladiratuzumab vedotin for HER2-positive breast cancer. Positive clinical trial results and regulatory submissions for these candidates could drive growth in 2020.
3. **Partnerships and collaborations**: The company has established partnerships with major pharmaceutical companies, such as Pfizer, ```Merck```, and GlaxoSmithKline, to develop and commercialize its ADC-based therapies. These partnerships could lead to increased revenue and growth opportunities in 2020.
4. **Expansion into new indications**: Seattle Genetics has been exploring new indications for its ADC-based therapies, such as ADCETRIS in multiple myeloma and non-Hodgkin lymphoma. Positive clinical trial results in these areas could expand the addressable market and drive growth in 2020.
5. **Increasing adoption in emerging markets**: The company has been expanding its commercial presence in emerging markets, such as China and Japan. Growing demand for ADC-based therapies in these regions could contribute to revenue growth in 2020.
6. **Investor confidence and valuation**: Seattle Genetics' stock price has been increasing in recent years, driven by positive clinical trial results and growing adoption of its ADC-based therapies. This increased investor confidence could lead to higher valuations and growth opportunities in 2020.

These factors suggest that Seattle Genetics is well-positioned for growth in 2020, driven by the continued success of ADCETRIS, progress in its pipeline, and expanding partnerships and collaborations.

## 0001069530-20-000009 — CASSAVA SCIENCES INC (2020)
### # Words: T MDA: 3935, T+1 MDA: 5034
### LAB Words:
- simufilam, Count in T: 0, Count in T+1: 29
-!plan, Count in T: 0, Count in T+1: 36
### Explanation:
The drug was in Phase 2b clinical trials, however the name Simufilam was not announced until later. 
https://www.globenewswire.com/news-release/2020/03/19/2003336/0/en/Cassava-Sciences-Announces-Clinical-Update-and-Business-Progress-Across-Neuroscience-Pipeline.html?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2020-03-26, predict the main growth drivers for CASSAVA SCIENCES INC in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0166 (4/241)
Based on information available up to 2020-03-26, the main growth drivers for Cassava Sciences, Inc. (SAVA) in 2020 are expected to be:

1. **```Simufilam``` (PTI-125) Development**: Cassava Sciences' lead product candidate, ```Simufilam```, is an investigational treatment for Alzheimer's disease. The company was expected to initiate a Phase 2b clinical trial for ```Simufilam``` in 2020, which could drive growth through increased research and development activities.

2. **SavaDx Development**: SavaDx is Cassava Sciences' investigational diagnostic biomarker to detect Alzheimer's disease. The company was working on advancing SavaDx through clinical trials, which could lead to increased growth through potential partnerships and collaborations.

3. **Strategic Partnerships**: Cassava Sciences may explore strategic partnerships to advance its product candidates, including ```Simufilam``` and SavaDx. Such partnerships could provide the company with access to additional resources, expertise, and funding, driving growth and development.

4. **Government Grants and Funding**: As a company focused on developing treatments for neurodegenerative diseases, Cassava Sciences may be eligible for government grants and funding. Securing such funding could provide the company with additional resources to advance its research and development activities.

5. **Increased Awareness and Interest in Alzheimer's Disease**: The growing awareness and interest in Alzheimer's disease, combined with the company's focus on developing innovative treatments, could drive growth through increased investor interest and attention from the medical community.

These growth drivers are based on the company's product pipeline, research and development activities, and market trends as of 2020-03-26.

## 0001178670-21-000010 — ALNYLAM PHARMACEUTICALS, INC. (2021)
### # Words: T MDA: 4266, T+1 MDA: 3564
### LAB Words:
- vutrisiran, Count in T: 0, Count in T+1: 10
### Explanation:
Vutrisiran name was known and it was up for approval. 
https://investors.alnylam.com/press-release?id=24771&utm_source=chatgpt.com
### Verdict: Noise
### Input:
Using only information through 2021-02-11, predict the main growth drivers for ALNYLAM PHARMACEUTICALS, INC. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0089 (2/224)
Based on information available up to 2021-02-11, the main growth drivers for Alnylam Pharmaceuticals, Inc. in 2021 are expected to be:

1. **ONPATTRO (patisiran)**: Continued growth in sales of ONPATTRO, an RNAi therapeutic for the treatment of hereditary transthyretin-mediated amyloidosis (hATTR amyloidosis). The drug received FDA approval in 2018 and has shown steady sales growth since its launch.

2. **GIVLAARI (givosiran)**: Increasing adoption of GIVLAARI, an RNAi therapeutic for the treatment of acute hepatic porphyria (AHP). The drug received FDA approval in 2019 and is expected to contribute significantly to Alnylam's revenue growth in 2021.

3. **OXLUMO (lumasiran)**: Launch and commercialization of OXLUMO, an RNAi therapeutic for the treatment of primary hyperoxaluria type 1 (PH1). The drug received FDA approval in November 2020, and its sales are expected to contribute to Alnylam's growth in 2021.

4. **```Vutrisiran```**: Potential approval and launch of ```vutrisiran```, an RNAi therapeutic for the treatment of hATTR amyloidosis. The drug is currently in Phase 3 clinical trials and has shown promising results.

5. **Collaborations and Partnerships**: Alnylam's collaborations with other pharmaceutical companies, such as Regeneron Pharmaceuticals and Vir Biotechnology, are expected to drive growth through the development of new RNAi therapeutics and expansion of its pipeline.

These growth drivers are expected to contribute to Alnylam's revenue growth and expansion of its RNAi therapeutics portfolio in 2021.

## 0001178879-20-000015 — AMICUS THERAPEUTICS, INC. (2020)
### # Words: T MDA: 5808, T+1 MDA: 6656
### LAB Words:
- treated, Count in T: 0, Count in T+1: 18
- alglucosidase, Count in T: 0, Count in T+1: 18
- alfa, Count in T: 0, Count in T+1: 18
### Explanation:
Treated is mentioned in the context of trials but for a different drug. 
https://www.sec.gov/ix?doc=/Archives/edgar/data/0001178879/000117887921000004/fold-20201231.htm
### Verdict: Noise
### Input:
Using only information through 2020-03-02, predict the main growth drivers for AMICUS THERAPEUTICS, INC. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0026 (1/378)
Based on publicly available information through 2020-03-02, here are some potential growth drivers for Amicus Therapeutics, Inc. (FOLD) in 2020:

1. **Galafold (migalastat) launch and growth**: Amicus Therapeutics' lead product, Galafold (migalastat), was approved by the FDA in February 2019 for the treatment of Fabry disease. In 2020, the company may see growth in sales and revenue from this product, particularly as more patients are diagnosed with Fabry disease and as the product gains market share.
2. **Expanded access to Galafold**: Amicus Therapeutics may continue to expand access to Galafold through various channels, such as increasing its availability in more countries, adding new distribution partners, or launching new formulations or dosing regimens. This could lead to increased sales and revenue growth.
3. **Pipeline progress**: Amicus Therapeutics has a pipeline of other products in development, including AT2221 (a Pompe disease treatment) and AT343 (a Fabry disease treatment). Positive clinical trial results or regulatory approvals for these products could lead to new revenue streams and growth opportunities for the company.
4. **Partnerships and collaborations**: Amicus Therapeutics may form new partnerships or collaborations with other companies, research institutions, or patient advocacy groups to advance its pipeline products or expand its reach in the market. These partnerships could provide access to new technologies, expertise, or resources, driving growth and innovation.
5. **Increased awareness and education**: As the company continues to raise awareness about Fabry disease and its treatment options, more patients may be diagnosed and ```treated``` with Galafold, leading to increased sales and revenue growth.
6. **Competitive advantage**: Amicus Therapeutics' Galafold has a unique mechanism of action and may offer a competitive advantage over other treatments for Fabry disease. As the company continues to promote and market its product, it may gain market share and drive growth.
7. **Expansion into new geographies**: Amicus Therapeutics may expand its commercial presence into new geographies, such as Europe or Asia, where there may be a growing demand for Fabry disease treatments. This could lead to increased sales and revenue growth.

These are some potential growth drivers for Amicus Therapeutics in 2020, based on publicly available information through 2020-03-02.

## 0001178879-23-000004 — AMICUS THERAPEUTICS, INC. (2023)
### # Words: T MDA: 4436, T+1 MDA: 3346
### LAB Words:
- +, Count in T: 0, Count in T+1: 14
- opfolda, Count in T: 0, Count in T+1: 14
- sold, Count in T: 0, Count in T+1: 7
### Explanation:
The alfa + miglustat terminology was not used until the approval but otherwise the drugs were together in the trials.
https://www.drugs.com/clinical_trials/u-s-fda-defers-action-filing-gaa-late-onset-pompe-21058.html
### Verdict: Weak LAB
### Input:
Using only information through 2023-03-01, predict the main growth drivers for AMICUS THERAPEUTICS, INC. in 2023. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0036 (1/281)
Based on information available up to 2023-03-01, the main growth drivers for Amicus Therapeutics, Inc. in 2023 are expected to be:

1. **Galafold (migalastat) sales growth**: As the first and only oral treatment approved for adults with Fabry disease who have a specific genetic mutation, Galafold is expected to continue driving revenue growth for Amicus. The company has been expanding its commercial efforts and increasing market penetration, which should lead to increased sales.

2. **AT-GAA (cipaglucosidase alfa ```+``` miglustat) regulatory progress**: Amicus is developing AT-GAA, a potential treatment for Pompe disease. Positive results from clinical trials and potential regulatory approvals in the US and EU could lead to significant revenue growth and expansion of the company's product portfolio.

3. **Pipeline advancements**: Amicus has a robust pipeline of rare disease treatments, including programs for Batten disease, Fabry disease, and other lysosomal storage disorders. Advancements in these programs, including positive clinical trial results and regulatory milestones, could drive growth and increase investor confidence.

4. **Global expansion and partnerships**: Amicus has been expanding its global presence through partnerships and collaborations. The company's partnerships with Japanese pharmaceutical companies, such as JCR Pharmaceuticals, and its expansion into new markets, such as China, could drive growth and increase access to its treatments.

5. **Increased focus on gene therapy**: Amicus has been investing in gene therapy research and development, which could lead to new treatment options for rare diseases. The company's gene therapy programs, including its collaboration with the University of Pennsylvania, could drive growth and increase its presence in the gene therapy market.

These growth drivers are based on publicly available information and may not reflect the company's current situation or future performance.

## 0001193125-19-057610 — Karyopharm Therapeutics Inc. (2019)
### # Words: T MDA: 8207, T+1 MDA: 8085
### LAB Words:
- xpovio, Count in T: 0, Count in T+1: 47
### Explanation:
Xpovio and pomalidomide are different drugs. Focusing on Xpovio - selinexor

The first approval for selinexor was July 3rd, 2019
https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-selinexor-multiple-myeloma

This also mentions other use cases of Xpovio that eventually it gets approved for.
### Verdict: Strong LAB
### Input:
Using only information through 2019-02-28, predict the main growth drivers for Karyopharm Therapeutics Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0239 (9/377)
Based on publicly available information up to 2019-02-28, here are some potential growth drivers for Karyopharm Therapeutics Inc. in 2019:

1. **```Xpovio``` (```Xpovio```) approval and launch**: Karyopharm's lead product, ```Xpovio``` (pomalidomide), was approved by the FDA in February 2018 for the treatment of patients with multiple myeloma who have received at least two prior therapies, including a proteasome inhibitor and an immunomodulatory agent. In 2019, the company was likely to focus on launching ```Xpovio``` and expanding its market share in the multiple myeloma treatment market.
2. **Commercialization of ```Xpovio``` in the US**: As ```Xpovio``` was approved in the US, Karyopharm was expected to invest in commercialization efforts, including building a sales force, establishing relationships with healthcare providers, and educating patients and payers about the benefits of ```Xpovio```.
3. **Expansion of ```Xpovio``` into new indications**: Karyopharm was likely to explore expanding the use of ```Xpovio``` into other indications, such as myelodysplastic syndromes (MDS) or other hematological malignancies, based on the results of ongoing clinical trials.
4. **Partnerships and collaborations**: Karyopharm may have formed or strengthened partnerships with other companies, research institutions, or organizations to advance its pipeline products, such as selinexor (KPT-330), a selective inhibitor of the nuclear export protein XPO1, which was in Phase 2 clinical trials for various indications.
5. **Clinical trial progress**: Karyopharm was likely to continue enrolling patients in ongoing clinical trials for its pipeline products, including selinexor, and present data from these trials at medical conferences, which could lead to further regulatory approvals or partnerships.
6. **Regulatory interactions**: The company may have engaged with regulatory agencies, such as the FDA, to discuss the development and approval of its pipeline products, including selinexor, which could lead to accelerated approval or breakthrough therapy designations.
7. **Investor and analyst interest**: Karyopharm's stock price and market capitalization may have been influenced by investor and analyst interest in the company's pipeline products and commercial prospects, which could have driven growth in the company's valuation.

These factors are based on publicly available information up to 2019-02-28 and may not reflect the company's actual performance or future prospects.

**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0231 (9/390)
Based on publicly available information through 2019-02-28, here are the main growth drivers for Karyopharm Therapeutics Inc. in 2019:

1. **```Xpovio``` (```Xpovio```)**: Karyopharm's lead product, ```Xpovio``` (pomalidomole, a selective inhibitor of the nuclear export protein (NXT), was approved by the FDA in February 2019 for the treatment of adult patients with multiple myeloma who have received at least two prior therapies, including a proteasome inhibitor and an immunomodulatory agent. The approval of ```Xpovio``` is expected to drive growth for the company in 2019.
2. **Commercialization and Sales**: With ```Xpovio``` now on the market, Karyopharm will focus on commercializing the product and generating revenue. The company will need to build a sales force, establish relationships with healthcare providers, and develop a marketing strategy to reach the target patient population.
3. **Expanded Label Indications**: Karyopharm is planning to pursue additional label expansions for ```Xpovio```, including in the treatment of patients with relapsed or refractory multiple myeloma who have received one prior therapy. Approval of these expanded indications could further increase the product's market potential and drive growth for the company.
4. **Partnerships and Collaborations**: Karyopharm has a robust pipeline of preclinical and clinical programs, including the oral, small molecule inhibitors of the Nuclear Export protein (NXT) platform. The company is expected to form partnerships with pharmaceutical companies to develop these programs, which could provide additional revenue streams and growth opportunities.
5. **Cash Position**: As of Q3 2018, Karyopharm had $143.4 million in cash and cash equivalents. The company's cash position provides a solid foundation to support the commercialization of ```Xpovio``` and fund its pipeline programs.
6. **Orphan Drug Status**: ```Xpovio``` was granted orphan drug status for the treatment of multiple myeloma, which provides seven years of market exclusivity in the US and EU. This exclusivity, combined with the product's mechanism of action, is expected to drive growth for the company in 2019.
7. **Market Opportunity**: Multiple myeloma is a growing market, with an increasing number of patients being diagnosed with the disease. The market is also becoming more complex, with the introduction of new treatments and therapies. Karyopharm's ```Xpovio``` is well-positioned to capture a share of this growing market.

**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0201 (8/398)
Based on publicly available information through 2019-02-28, here are some potential main growth drivers for Karyopharm Therapeutics Inc. in 2019:

1. **```Xpovio``` (```Xpovio```) Launch and Commercialization**: Karyopharm's lead product, ```Xpovio``` (selinexor), a selective inhibitor of the nuclear export protein XPO1, was approved by the FDA in October 2019 for the treatment of patients with multiple myeloma who have received at least 3 prior therapies, including a proteasome inhibitor and an immunomodulatory agent. The company is likely to focus on commercializing ```Xpovio``` in 2019, which could drive growth through revenue recognition and increased visibility in the multiple myeloma treatment market.
2. **Phase 3 Clinical Trials**: Karyopharm has several ongoing Phase 3 clinical trials for ```Xpovio``` in combination with other therapies for various indications, including multiple myeloma, lymphoma, and solid tumors. Positive trial results could lead to additional regulatory approvals and expanded indications for ```Xpovio```, driving growth through increased revenue and market share.
3. **Partnerships and Collaborations**: Karyopharm has partnered with several pharmaceutical companies, including Amgen, Bristol-Myers Squibb, and Ono Pharmaceutical Co., Ltd. to develop and commercialize its products. These partnerships could lead to additional funding, expertise, and access to new markets, driving growth through increased revenue and market share.
4. **Expanded Product Pipeline**: Karyopharm has a pipeline of preclinical and clinical-stage programs targeting various indications, including multiple myeloma, lymphoma, and solid tumors. Positive data from these programs could lead to additional product approvals and revenue streams, driving growth through increased revenue and market share.
5. **Increased Focus on Commercialization and Regulatory Affairs**: As ```Xpovio``` approaches commercialization, Karyopharm is likely to invest in building its commercial infrastructure, including sales and marketing teams, to support the launch and growth of the product. This could drive growth through increased revenue and market share.
6. **Growing Demand for Targeted Therapies**: The multiple myeloma treatment market is growing, driven by an increasing understanding of the disease biology and the need for more targeted and effective therapies. Karyopharm's ```Xpovio```, which targets the nuclear export protein XPO1, a key regulator of protein transport, may benefit from this trend, driving growth through increased demand and market share.

These are some of the potential growth drivers for Karyopharm Therapeutics Inc. in 2019, based on publicly available information through 2019-02-28.

## 0001193125-19-070954 — ChemoCentryx, Inc. (2019)
### # Words: T MDA: 5962, T+1 MDA: 6200
### LAB Words:
- anca, Count in T: 0, Count in T+1: 13
### Explanation:
The ANCA term was not used in the 10-K though it was used in another document dated to before there.
https://cdn.clinicaltrials.gov/large-docs/27/NCT02994927/Prot_000.pdf?utm_source=chatgpt.com
### Verdict: Weak LAB
### Input:
Using only information through 2019-03-11, predict the main growth drivers for ChemoCentryx, Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0044 (1/225)
Based on information available up to 2019-03-11, the main growth drivers for ChemoCentryx, Inc. in 2019 are expected to be:

1. **Avacopan (CCX168)**: ChemoCentryx's lead product candidate, Avacopan, is a C5a receptor inhibitor being developed for the treatment of anti-neutrophil cytoplasmic antibody (```ANCA```)-associated vasculitis (AAV). Positive results from the Phase III ADVOCATE trial, announced in 2018, are expected to drive growth in 2019 as the company prepares for regulatory submissions and potential commercialization.

2. **Partnership with Vifor Fresenius Medical Care Renal Pharma (VFMCRP)**: ChemoCentryx's partnership with VFMCRP, announced in 2016, is expected to continue driving growth in 2019. The partnership is focused on the development and commercialization of Avacopan for AAV and other indications.

3. **Expansion of Avacopan into new indications**: ChemoCentryx is exploring the potential of Avacopan in other indications, including C3 glomerulopathy (C3G) and hidradenitis suppurativa (HS). Positive results from these studies could drive growth in 2019 and beyond.

4. **Advancements in the company's pipeline**: ChemoCentryx has a pipeline of other product candidates, including CCX140, a CCR2 inhibitor being developed for the treatment of focal segmental glomerulosclerosis (FSGS). Progress in these programs is expected to contribute to growth in 2019.

Overall, ChemoCentryx's growth in 2019 is expected to be driven by the advancement of Avacopan towards commercialization, expansion into new indications, and progress in the company's pipeline.

## 0001213900-20-007544 — TFF Pharmaceuticals, Inc. (2020)
### # Words: T MDA: 1819, T+1 MDA: 2203
### LAB Words:
- australia, Count in T: 0, Count in T+1: 7
- phase, Count in T: 0, Count in T+1: 5
- covid-19, Count in T: 0, Count in T+1: 6
- trial, Count in T: 0, Count in T+1: 5
### Explanation:
Phase may or may not be LAB. Covid on March 27th also may or may not be.
### Verdict: Weak LAB 
### Input:
Using only information through 2020-03-27, predict the main growth drivers for TFF Pharmaceuticals, Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0042 (1/238)
Based on information available up to 2020-03-27, the main growth drivers for TFF Pharmaceuticals, Inc. in 2020 are expected to be:

1. **Advancements in Thin Film Freezing (TFF) Technology**: As a pioneer in the field, TFF Pharmaceuticals is likely to continue innovating and improving its proprietary technology, which enables the creation of dry powder formulations of complex molecules. This could lead to increased adoption and partnerships.

2. **Partnerships and Collaborations**: TFF Pharmaceuticals has already established partnerships with prominent pharmaceutical companies, such as UNION Therapeutics and Augmenta Bioworks. Further collaborations and licensing agreements are expected to drive growth by expanding the company's pipeline and revenue streams.

3. **Pipeline Progress**: The company's pipeline, including its lead candidates, Voriconazole Inhalation Powder and Tacrolimus Inhalation Powder, is expected to progress through clinical trials. Positive results and regulatory approvals could significantly drive growth.

4. **Increased Focus on Inhalation Therapies**: The ```COVID-19``` pandemic has highlighted the importance of inhalation therapies. TFF Pharmaceuticals' expertise in this area could lead to increased interest and investment in its technologies and products.

5. **Growing Demand for Dry Powder Formulations**: The pharmaceutical industry's shift towards dry powder formulations, driven by their advantages in terms of stability, convenience, and patient compliance, is expected to benefit TFF Pharmaceuticals, which is well-positioned to capitalize on this trend.

These growth drivers are expected to contribute to TFF Pharmaceuticals' expansion and success in 2020, based on information available up to 2020-03-27.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0029 (1/347)
Based on publicly available information through 2020-03-27, here are some potential growth drivers for TFF Pharmaceuticals, Inc. in 2020:

1. **Commercialization of TFF's lead product, Tlando**: TFF Pharmaceuticals acquired the rights to Tlando, a generic version of the FDA-approved drug, tolterodine tartrate extended-release capsules, in 2019. As TFF continues to commercialize Tlando, it is likely to drive revenue growth for the company in 2020.
2. **Expansion of Tlando's market reach**: TFF may focus on expanding the market reach of Tlando, potentially through partnerships with distributors, wholesalers, or pharmacies, which could lead to increased sales and revenue growth.
3. **Development of new products**: TFF has a pipeline of generic products in development, including a generic version of the FDA-approved drug, tolterodine tartrate extended-release capsules, which is currently in ```Phase``` III clinical trials. Successful development and approval of these products could drive growth for the company in the future.
4. **Cost savings and operational efficiencies**: As a generic pharmaceutical company, TFF may focus on optimizing its operations to reduce costs and improve efficiency, which could lead to increased profitability and growth.
5. **Partnerships and collaborations**: TFF may explore partnerships or collaborations with other pharmaceutical companies, contract manufacturers, or distributors to expand its product offerings, improve its supply chain, or access new markets, which could drive growth and revenue.
6. **Generic market trends**: The generic pharmaceutical market is expected to continue growing in 2020, driven by increasing demand for affordable healthcare and the patent cliff of many branded pharmaceuticals. TFF's focus on generic products positions the company to benefit from this trend.
7. **Regulatory environment**: TFF may benefit from a favorable regulatory environment, including the FDA's efforts to promote generic competition and the Hatch-Waxman Act, which provides incentives for generic companies to develop and market generic versions of branded pharmaceuticals.

These are some potential growth drivers for TFF Pharmaceuticals, Inc. in 2020, based on publicly available information through 2020-03-27.

## 0001213900-21-014575 — TFF Pharmaceuticals, Inc. (2021)
### # Words: T MDA: 2203, T+1 MDA: 2312
### LAB Words:
- income, Count in T: 0, Count in T+1: 5
- incentive, Count in T: 0, Count in T+1: 6
- payments, Count in T: 0, Count in T+1: 5
- tax, Count in T: 0, Count in T+1: 10
- collaborative, Count in T: 0, Count in T+1: 6
### Explanation:
Some of these words are related to interest income and the others are related to a section at the end of the the MD&A Research and Development Tax Incentive related to the Australian Taxation Office. 
The drugs in question TFF-100 seem to be hallucinated. 
There is a vague paragraph about "Collaborative Arrangements" in the T+1 MDA. It is unclear why it is there.
This should be weak LAB or maybe noise  
### Verdict: Weak LAB
### Input:
Using only information through 2021-03-10, predict the main growth drivers for TFF Pharmaceuticals, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0052 (1/191)
Based on information available up to 2021-03-10, the main growth drivers for TFF Pharmaceuticals, Inc. in 2021 are expected to be:

1. **Advancements in Thin Film Freezing (TFF) Technology**: TFF Pharmaceuticals' proprietary technology platform is expected to continue to attract partnerships and collaborations, driving growth through licensing agreements and joint development projects.

2. **Inhaled COVID-19 Treatment**: The company's inhaled COVID-19 treatment, which utilizes its TFF technology, may experience significant growth due to the ongoing pandemic and the need for effective treatments.

3. **Expansion of Pipeline**: TFF Pharmaceuticals' growing pipeline of products, including those for respiratory diseases and biodefense applications, is expected to drive growth through new partnerships, grants, and government contracts.

4. **Government Funding and Grants**: The company may continue to receive government funding and grants for its biodefense and pandemic-related projects, providing a source of non-dilutive capital and driving growth.

5. **Strategic Partnerships**: TFF Pharmaceuticals' ability to form strategic partnerships with pharmaceutical companies, government agencies, and research institutions is expected to drive growth through ```collaborative``` development projects and licensing agreements.

These growth drivers are based on the company's historical performance, industry trends, and market conditions up to 2021-03-10.

**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0029 (1/343)
Based on publicly available information as of 2021-03-10, here are some potential growth drivers for TFF Pharmaceuticals, Inc. in 2021:

1. **TFF's lead product, TFF-100 (sulindac sulfone)**: TFF Pharmaceuticals has been developing TFF-100, a reformulation of the existing drug sulindac sulfone, which has shown promise in treating certain types of cancer, including pancreatic cancer. If TFF-100 receives regulatory approval, it could drive growth for the company.
2. **Orphan drug designation**: TFF-100 has been granted Orphan Drug Designation by the FDA for the treatment of pancreatic cancer. This designation can provide the company with certain incentives, such as ```tax``` credits, clinical trial design assistance, and a potential seven-year marketing exclusivity period, which could drive growth.
3. **Partnerships and collaborations**: TFF Pharmaceuticals has partnered with various organizations, including the University of Texas Southwestern Medical Center, to develop and commercialize its products. These partnerships could provide access to new technologies, expertise, and funding, which could drive growth.
4. **Expansion of clinical trials**: TFF Pharmaceuticals has been expanding its clinical trials for TFF-100, including a Phase 2 trial in pancreatic cancer. Successful completion of these trials could lead to regulatory approval and increased revenue for the company.
5. **Increased awareness and adoption of personalized medicine**: The company's focus on developing targeted therapies, such as TFF-100, may benefit from the growing trend towards personalized medicine, which could drive growth as more patients and healthcare providers adopt these types of treatments.
6. **Competitive advantage in the oncology market**: TFF Pharmaceuticals' focus on developing treatments for cancer, a growing and increasingly competitive market, could provide the company with a competitive advantage as it seeks to establish itself as a player in the oncology space.
7. **Potential for additional product pipeline**: TFF Pharmaceuticals has a pipeline of other products in development, including a reformulation of the anti-inflammatory drug, celecoxib. Successful development of these products could provide additional growth opportunities for the company.

## 0001356576-20-000010 — SUPERNUS PHARMACEUTICALS, INC. (2020)
### # Words: T MDA: 4171, T+1 MDA: 7228
### LAB Words:
- navitor, Count in T: 0, Count in T+1: 15
- uswm, Count in T: 0, Count in T+1: 26
-!intangible, Count in T: 0, Count in T+1: 23
-!fair, Count in T: 0, Count in T+1: 28
-!value, Count in T: 0, Count in T+1: 30
-!acquired, Count in T: 0, Count in T+1: 17
-!asset, Count in T: 0, Count in T+1: 17
### Explanation:
This transaction happened in April 2020. I can't find anything related to 2016. 
https://www.globenewswire.com/news-release/2020/04/28/2023750/0/en/Supernus-to-Acquire-CNS-Portfolio-from-US-WorldMeds.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-28, predict the main growth drivers for SUPERNUS PHARMACEUTICALS, INC. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0038 (1/260)
Based on information available up to 2020-02-28, the main growth drivers for Supernus Pharmaceuticals, Inc. in 2020 are expected to be:

1. **Trokendi XR and Oxtellar XR**: Continued growth in prescriptions and revenue from these two epilepsy medications, which are the company's flagship products. Both products have shown steady growth in the past, and this trend is expected to continue in 2020.

2. **APOKYN**: Growth in sales of APOKYN, a treatment for Parkinson's disease, which was ```acquired``` by Supernus in 2016. The company has been working to increase awareness and expand the reach of this product, which is expected to contribute to revenue growth in 2020.

3. **SPN-812**: Potential approval and launch of SPN-812, a novel non-stimulant treatment for attention deficit hyperactivity disorder (ADHD). The company submitted a New Drug Application (NDA) for SPN-812 in November 2019, and approval is expected in 2020. A successful launch of this product could provide a significant boost to the company's revenue.

4. **SPN-810**: Progress in the development of SPN-810, a treatment for impulsive aggression in patients with ADHD. The company is conducting Phase III clinical trials for this product, and positive results could lead to an NDA submission and potential approval in the future.

5. **International Expansion**: Expansion of the company's products into new international markets, which could provide additional revenue growth opportunities. Supernus has been working to establish partnerships and build its presence in various regions, including Europe and Asia.

These growth drivers are based on the company's product portfolio, pipeline, and business strategy as of 2020-02-28.

## 0001356576-21-000028 — SUPERNUS PHARMACEUTICALS, INC. (2021)
### # Words: T MDA: 7228, T+1 MDA: 9142
### LAB Words:
- adamas, Count in T: 0, Count in T+1: 37
- qelbree, Count in T: 0, Count in T+1: 24
### Explanation:
Qelbree name was not announced but the drug was close to approval
https://www.drugs.com/history/qelbree.html?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2021-03-08, predict the main growth drivers for SUPERNUS PHARMACEUTICALS, INC. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0049 (2/407)
Based on publicly available information through 2021-03-08, here are some potential growth drivers for Supernus Pharmaceuticals, Inc. in 2021:

1. **Continued growth of Oxtellar XR**: Supernus' lead product, Oxtellar XR (oxcarbazepine extended-release), is a treatment for epilepsy. The company has been expanding its marketing efforts and has seen increasing demand for the product. As the epilepsy market continues to grow, Oxtellar XR is likely to benefit from this trend.
2. **Launch of ```Qelbree```**: Supernus has been preparing for the launch of ```Qelbree``` (viloxazine extended-release), a treatment for attention deficit hyperactivity disorder (ADHD). The company has been building a sales team and marketing infrastructure to support the launch, which could lead to significant revenue growth in 2021.
3. **Expansion into new markets**: Supernus has been exploring opportunities to expand its product portfolio into new markets, including the treatment of pain and other central nervous system (CNS) disorders. If the company is successful in launching new products or entering new markets, it could drive growth and increase its revenue.
4. **Increasing competition in the CNS market**: The CNS market is highly competitive, and Supernus may benefit from the entry of new competitors, which could lead to increased demand for its products. As new players enter the market, they may not have the same level of experience or resources as established players, which could give Supernus a competitive advantage.
5. **Investor interest and funding**: Supernus has received significant investment from investors, including a $100 million Series C funding round in 2020. This funding has enabled the company to invest in its products and infrastructure, which could lead to increased growth and expansion in 2021.
6. **Strategic partnerships**: Supernus has formed partnerships with other companies to expand its reach and capabilities. For example, the company partnered with a specialty pharmacy to improve access to its products. These partnerships could lead to increased sales and revenue growth.
7. **Regulatory environment**: The regulatory environment for CNS products is complex and subject to change. However, if regulatory changes or new guidelines are introduced that favor Supernus' products, it could lead to increased demand and growth.

These are just a few potential growth drivers for Supernus Pharmaceuticals, Inc. in 2021. The company's actual performance may differ from these predictions, and other factors may also impact its growth.

## 0001367644-19-000016 — Emergent BioSolutions Inc. (2019)
### # Words: T MDA: 6203, T+1 MDA: 5337
### LAB Words:
- fda, Count in T: 0, Count in T+1: 11
- anthrax, Count in T: 0, Count in T+1: 16
- vaccine, Count in T: 0, Count in T+1: 19
- announced, Count in T: 0, Count in T+1: 11
### Explanation:
This one is very difficult to tell reading the MD&As. It could be Strong LAB but I think it is just noise. Maybe Bradford can comment on it.
https://www.sec.gov/Archives/edgar/data/1367644/000136764419000016/form10-k.htm#Item7.ManagementsDiscussionandAnalysisofFinancialConditionandResultsofOperations
https://www.sec.gov/ix?doc=/Archives/edgar/data/0001367644/000136764420000010/ebs-2019123110k.htm
### Verdict: Noise
### Input:
Using only information through 2019-02-22, predict the main growth drivers for Emergent BioSolutions Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0234 (9/385)
Based on publicly available information up to 2019-02-22, here are some potential main growth drivers for Emergent BioSolutions Inc. in 2019:

1. **Growing demand for BioThrax (```Anthrax``` ```Vaccine```)**: As a leading supplier of the BioThrax ```anthrax``` ```vaccine```, Emergent BioSolutions is well-positioned to benefit from the US government's continued efforts to maintain a stockpile of ```anthrax``` ```vaccine``` for biodefense purposes. The company's contract with the US government to supply BioThrax is expected to continue, providing a stable revenue stream.
2. **Expansion of the BioPort business**: Emergent BioSolutions acquired BioPort in 2013, and since then, the company has been investing in expanding the BioPort facility in Charleston, South Carolina. In 2018, the company ```announced``` plans to invest an additional $100 million in the facility, which is expected to increase production capacity and support the growth of the BioThrax business.
3. **Growing demand for pandemic influenza vaccines**: Emergent BioSolutions has a contract with the US government to supply pandemic influenza vaccines, including the H5N1 and H7N9 avian influenza vaccines. As the threat of pandemic influenza remains a concern, the company is well-positioned to benefit from government contracts and orders for these vaccines.
4. **Increasing focus on biodefense and public health preparedness**: The US government has continued to emphasize the importance of biodefense and public health preparedness, which could lead to increased funding and contracts for companies like Emergent BioSolutions that provide critical biodefense and public health products.
5. **Expansion of the company's product portfolio**: Emergent BioSolutions has been investing in research and development to expand its product portfolio, including the development of new vaccines and therapeutics for infectious diseases. The company's pipeline includes several promising candidates, including a ```vaccine``` for the Nipah virus and a therapeutic for ```anthrax``` exposure.
6. **Partnerships and collaborations**: Emergent BioSolutions has a history of partnering with other companies and government agencies to advance its products and technologies. These partnerships could lead to new business opportunities and growth for the company in 2019.

These factors are based on publicly available information and may not be exhaustive. However, they provide a starting point for understanding the potential growth drivers for Emergent BioSolutions in 2019.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0179 (6/336)
Based on the publicly available information up to 2019-02-22, here are the potential growth drivers for Emergent BioSolutions Inc. in 2019:

1. **Growing demand for BioThrax**: Emergent BioSolutions' BioThrax, a recombinant ```anthrax``` ```vaccine```, is a key product for the company. The US government has a contract with Emergent to supply BioThrax to the Strategic National Stockpile, and the company has also been working to expand its distribution network. As the threat of bioterrorism remains a concern, the demand for BioThrax is likely to continue growing.
2. **Expansion of the BioPort facility**: In 2018, Emergent BioSolutions acquired the BioPort facility in Baltimore, Maryland, which is a key manufacturing site for the company. The expansion of this facility is expected to increase the company's production capacity, enabling it to meet growing demand for its products, including BioThrax.
3. **Growing presence in the ```vaccine``` market**: Emergent BioSolutions has been expanding its portfolio of vaccines, including its Ebola ```vaccine```, which has received ```FDA``` approval. The company's growing presence in the ```vaccine``` market, particularly in the areas of biodefense and infectious diseases, is likely to drive growth in 2019.
4. **Increasing focus on contract manufacturing**: Emergent BioSolutions has been investing in its contract manufacturing capabilities, including the acquisition of the BioPort facility. This focus on contract manufacturing is expected to drive growth as the company leverages its expertise to support other companies in the development and production of biologics and vaccines.
5. **Government contracts and funding**: Emergent BioSolutions has a significant presence in the government contracting space, with a number of contracts related to biodefense and public health. The company's ability to secure new government contracts and funding is likely to be a key driver of growth in 2019.

These factors are based on publicly available information up to 2019-02-22 and may not reflect the company's actual performance in 2019.

**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0168 (7/417)
Emergent BioSolutions Inc. (EBS) is a leading provider of public health solutions and specialty products for healthcare and government customers. Based on the company's historical trends and industry developments up to 2019-02-22, some potential main growth drivers for Emergent BioSolutions in 2019 could be:

1. **Biosolutions' Government Contract Awards**: The company has a strong track record of winning government contracts for its products and services, particularly in the areas of biothreat and pandemic preparedness. Expecting continued growth in government spending on public health initiatives, Emergent BioSolutions is likely to secure more contracts, driving revenue growth.
2. **Expansion of its BioThreat and Pandemic Preparedness Business**: Emergent BioSolutions has been expanding its capabilities in the biothreat and pandemic preparedness market through strategic acquisitions (e.g., its 2013 acquisition of New Haven Pharmaceuticals) and new product development (e.g., its partnership with the US government on pandemic influenza ```vaccine``` development). As governments and international organizations continue to prepare for potential pandemics, Emergent BioSolutions is well-positioned to benefit from this trend.
3. **Growing Demand for ```Anthrax``` ```Vaccine``` and Other BioThreat Products**: The company's ```anthrax``` ```vaccine```, BioThrax, is a key product in the US government's stockpile, and Emergent BioSolutions has been working to expand its use of this ```vaccine```. Other biothreat products, such as its botulinum toxin antitoxin, may also see increased demand as governments and international organizations focus on biosecurity and pandemic preparedness.
4. **Expansion of its Specialty Products Segment**: Emergent BioSolutions' specialty products segment, which includes its BioPort business, has been growing through new product development and strategic partnerships (e.g., its partnership with the US government on pandemic influenza ```vaccine``` development). Expect this segment to continue growing as the company expands its product offerings and capabilities.
5. **Increased Demand for its Medical Countermeasures**: The company's medical countermeasures, such as its BioThrax and botulinum toxin antitoxin, may see increased demand as governments and international organizations focus on pandemic preparedness and biosecurity.
6. **Partnerships and Collaborations**: Emergent BioSolutions has a history of partnering with government agencies, international organizations, and other companies to develop and commercialize new products. Expect the company to continue partnering with key stakeholders to drive growth and expand its product offerings.

These are some of the potential growth drivers for Emergent BioSolutions in 2019 based on the company's historical trends and industry developments up to 2019-02-22.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0135 (3/222)
Based on information available up to 2019-02-22, the main growth drivers for Emergent BioSolutions Inc. in 2019 are expected to be:

1. **Narcan (naloxone) sales growth**: Emergent BioSolutions acquired Adapt Pharma in 2018, adding Narcan, a nasal spray version of naloxone, to its portfolio. Narcan sales are expected to continue growing due to the increasing demand for opioid overdose treatments.

2. **BioThrax and other ```vaccine``` sales**: Emergent BioSolutions is a leading provider of vaccines, including BioThrax, the only FDA-approved ```anthrax``` ```vaccine```. Sales of BioThrax and other vaccines are expected to remain strong, driven by government contracts and growing demand for biodefense products.

3. **Contract manufacturing and development services**: Emergent BioSolutions offers contract manufacturing and development services to pharmaceutical and biotechnology companies. This business segment is expected to grow due to increasing demand for outsourced manufacturing and development services.

4. **Pipeline development**: Emergent BioSolutions has a pipeline of products in development, including treatments for infectious diseases and oncology. Progress in these development programs could drive growth and expansion into new markets.

5. **Government funding and contracts**: Emergent BioSolutions has a history of securing government funding and contracts for its biodefense products and services. Continued government support is expected to drive growth and revenue in 2019.

These growth drivers are based on Emergent BioSolutions' historical performance, industry trends, and market demand up to 2019-02-22.

## 0001375151-19-000016 — ZOGENIX, INC. (2019)
### # Words: T MDA: 7030, T+1 MDA: 9392
### LAB Words:
- shinyaku, Count in T: 0, Count in T+1: 30
- japan, Count in T: 0, Count in T+1: 19
- lease, Count in T: 0, Count in T+1: 34
### Explanation:
In March 2019 they enter into the "Shinyaku Aggreement" with Nippon Shinyaku Co., Ltd. (Shinyaku) for the exclusive distribution of Fintepla in Japan for the treatment of Dravet syndrome and LGS
As explained in the T+1 MDA.
### Verdict: Strong LAB
### Input:
Using only information through 2019-02-28, predict the main growth drivers for ZOGENIX, INC. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0037 (1/270)
Based on information available up to 2019-02-28, the main growth drivers for Zogenix, Inc. in 2019 are expected to be:

1. **Fintepla (ZX008)**: Zogenix's lead product candidate, Fintepla, is an investigational treatment for Dravet syndrome, a rare form of epilepsy. Positive results from Phase 3 clinical trials in 2018 demonstrated significant reductions in seizure frequency. Anticipated FDA approval and subsequent commercialization of Fintepla in 2019 are expected to drive growth.

2. **Expanded Pipeline**: Zogenix has been actively expanding its pipeline through strategic partnerships and acquisitions. The company's collaborations with other pharmaceutical companies, such as Tevard Biosciences, are expected to yield new product candidates and drive growth.

3. **International Expansion**: Zogenix has been expanding its presence in international markets, particularly in Europe and ```Japan```. The company's partnerships with local pharmaceutical companies and regulatory approvals in these regions are expected to contribute to growth.

4. **Increased Research and Development**: Zogenix has been investing heavily in research and development, with a focus on developing new treatments for rare and underserved neurological disorders. The company's R&D efforts are expected to yield new product candidates and drive growth.

5. **Growing Demand for Rare Disease Treatments**: The demand for treatments for rare diseases, such as Dravet syndrome, is increasing due to growing awareness and diagnosis rates. Zogenix's focus on developing treatments for these conditions positions the company for growth in this expanding market.

These growth drivers are expected to contribute to Zogenix's revenue and earnings growth in 2019, driven by the potential approval and commercialization of Fintepla, expansion of the company's pipeline, and increasing demand for rare disease treatments.

## 0001396814-21-000014 — Pacira BioSciences, Inc. (2021)
### # Words: T MDA: 7267, T+1 MDA: 7150
### LAB Words:
- flexion, Count in T: 0, Count in T+1: 41
- zilretta, Count in T: 0, Count in T+1: 27
-!term, Count in T: 0, Count in T+1: 19
### Explanation:
Flexion acquistion and Zilretta acquisition were both acquired in October 2021.
https://investor.pacira.com/news-releases/news-release-details/pacira-biosciences-acquire-flexion-therapeutics-further
Term is noise - flagged because of 'Term Loan'. Added to exclude list. 
### Verdict: Strong LAB
### Input:
Using only information through 2021-03-01, predict the main growth drivers for Pacira BioSciences, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0162 (4/247)
Based on information available up to 2021-03-01, the main growth drivers for Pacira BioSciences, Inc. in 2021 are expected to be:

1. **EXPAREL (bupivacaine liposome injectable suspension)**: As the company's flagship product, EXPAREL is a non-opioid, long-acting local analgesic used for postsurgical pain management. Its sales growth is expected to continue, driven by increasing adoption in various surgical procedures, including orthopedic, general, and plastic surgery.

2. **EXPAREL label expansion**: In 2020, the FDA approved a label expansion for EXPAREL to include use in pediatric patients aged 6 and older. This expansion is expected to contribute to the growth of EXPAREL sales in 2021.

3. **iovera° (cryoanalgesia)**: Pacira's iovera° system is a handheld cryoanalgesia device used to reduce pain by applying cold temperatures to specific nerves. The company expects to see increased adoption of iovera° in 2021, particularly in the orthopedic and pain management markets.

4. **```ZILRETTA``` (triamcinolone acetonide extended-release injectable suspension)**: Pacira acquired ```Flexion``` Therapeutics, the manufacturer of ```ZILRETTA```, in 2020. ```ZILRETTA``` is an extended-release corticosteroid used to treat osteoarthritis knee pain. The acquisition is expected to contribute to Pacira's revenue growth in 2021.

5. **Partnerships and collaborations**: Pacira has established partnerships with various healthcare organizations and companies to promote its products and expand its reach. These partnerships are expected to drive growth and increase the adoption of Pacira's products in 2021.

These growth drivers are expected to contribute to Pacira BioSciences' revenue growth in 2021, based on information available up to 2021-03-01.

## 0001437749-19-018974 — NATURAL ALTERNATIVES INTERNATIONAL INC (2019)
### # Words: T MDA: 5048, T+1 MDA: 3352
### LAB Words:
- covid-19, Count in T: 0, Count in T+1: 11
- pandemic, Count in T: 0, Count in T+1: 10
- former, Count in T: 0, Count in T+1: 7
### Explanation:
Covid
### Verdict: Strong LAB
### Input:
Using only information through 2019-09-24, predict the main growth drivers for NATURAL ALTERNATIVES INTERNATIONAL INC in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0054 (2/368)
Based on the publicly available information up to 2019-09-24, here are some potential growth drivers for Natural Alternatives International, Inc. (NAII) in 2020:

1. **Growing demand for plant-based and natural products**: The global market for plant-based and natural products is expected to continue growing, driven by increasing consumer demand for healthier and more sustainable options. As a company that specializes in natural and organic products, NAII is well-positioned to benefit from this trend.
2. **Expansion of e-commerce platform**: In 2019, NAII launched a new e-commerce platform, which could potentially drive growth in 2020 as more consumers turn to online shopping. A strong online presence can help the company reach a wider audience and increase sales.
3. **New product launches**: NAII has a history of launching new products, and 2020 may see the introduction of new natural and organic products that cater to emerging trends and consumer preferences. Successful new product launches can drive growth and increase revenue.
4. **Increased focus on sustainability**: Consumers are becoming increasingly environmentally conscious, and companies that prioritize sustainability are likely to see growth. NAII's focus on natural and organic products aligns with this trend, and the company may see an increase in sales as consumers seek out more sustainable options.
5. **Partnerships and collaborations**: NAII has a history of partnering with other companies and organizations to expand its product offerings and reach new markets. In 2020, the company may form new partnerships or collaborations that drive growth and increase its market share.
6. **Growing demand for immune system support products**: The ```COVID-19``` ```pandemic``` has highlighted the importance of immune system health, and NAII's products that support immune function may see increased demand in 2020.
7. **Expansion into new markets**: NAII has a presence in the US and Canada, but there may be opportunities for expansion into new markets, such as Europe or Asia, where there is growing demand for natural and organic products.

These are just a few potential growth drivers for NAII in 2020, based on publicly available information up to 2019-09-24.

## 0001479290-22-000034 — Revance Therapeutics, Inc. (2022)
### # Words: T MDA: 10403, T+1 MDA: 10506
### LAB Words:
- daxxify, Count in T: 0, Count in T+1: 48
### Explanation:
FDA approved Daxxify on September 8th, 2022. In the 2022 MDA it gets mentioned as DaxibotulinumtoxinA
### Verdict: Weak LAB (take)
### Input:
Using only information through 2022-02-28, predict the main growth drivers for Revance Therapeutics, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0262 (10/381)
Based on publicly available information through 2022-02-28, here are some potential growth drivers for Revance Therapeutics, Inc. in 2022:

1. **```Daxxify``` (DaxibotulinumtoxinA) Approval and Commercialization**: Revance's lead product, ```Daxxify```, is a long-acting neuromodulator for the treatment of adult-onset blepharospasm and is expected to be a significant growth driver for the company. The FDA approved ```Daxxify``` in January 2022, and the company is likely to focus on commercializing the product and expanding its market share in the coming year.
2. **Expansion of ```Daxxify``` into Additional Indications**: Revance has been exploring the use of ```Daxxify``` in other indications, such as facial wrinkles and frown lines. If the company receives regulatory approval for additional indications, it could lead to increased revenue growth and expanded market penetration.
3. **Partnerships and Collaborations**: Revance has a strong pipeline of product candidates, and the company may form partnerships with other pharmaceutical companies to develop and commercialize these products. Such partnerships could provide access to new markets, technologies, and expertise, driving growth for Revance.
4. **Increased Adoption of ```Daxxify``` by Physicians and Patients**: As physicians become more familiar with ```Daxxify```, they may increasingly recommend the product to their patients, leading to higher sales and revenue growth for Revance.
5. **Competitive Advantage of ```Daxxify```'s Long-Lasting Effectiveness**: ```Daxxify```'s long-acting effect (up to 12 months) may provide a competitive advantage over other neuromodulators on the market, such as Botox, which typically lasts for 3-4 months. This could lead to increased market share and revenue growth for Revance.
6. **Growing Demand for Aesthetic and Therapeutic Treatments**: The demand for aesthetic and therapeutic treatments is increasing, driven by an aging population, growing awareness of the importance of aesthetics, and expanding insurance coverage for certain treatments. Revance is well-positioned to benefit from this trend, particularly with its ```Daxxify``` product.
7. **Expansion of Revance's Sales Force and Distribution Network**: As the company grows, it may expand its sales force and distribution network to reach more physicians and patients, increasing its market share and revenue.

These are some of the potential growth drivers for Revance Therapeutics, Inc. in 2022, based on publicly available information through 2022-02-28.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0228 (6/263)
Based on information available up to 2022-02-28, the main growth drivers for Revance Therapeutics, Inc. in 2022 are expected to be:

1. **```Daxxify``` (DaxibotulinumtoxinA)**: The FDA approval of ```Daxxify```, a long-acting neurotoxin for the treatment of glabellar lines, is expected to be a significant growth driver. As the first and only peptide-formulated neuromodulator with a long duration of action, ```Daxxify``` has the potential to capture a substantial market share in the aesthetics industry.

2. **Commercial Launch of ```Daxxify```**: Following FDA approval, the commercial launch of ```Daxxify``` is expected to drive revenue growth for Revance Therapeutics. The company has been preparing for the launch by building its commercial infrastructure, including hiring a sales force and establishing a distribution network.

3. **Expansion of Therapeutic Pipeline**: Revance Therapeutics has a pipeline of therapeutic candidates, including DaxibotulinumtoxinA for Injection, which is being developed for the treatment of cervical dystonia and plantar fasciitis. Progress in these programs could drive growth and expand the company's addressable market.

4. **Strategic Partnerships**: Revance Therapeutics may explore strategic partnerships to expand its reach and accelerate growth. Collaborations with other companies or organizations could provide access to new markets, technologies, or expertise, driving growth and increasing the company's competitiveness.

5. **Increasing Demand for Aesthetic Treatments**: The demand for aesthetic treatments, including neuromodulators like ```Daxxify```, is expected to continue growing in 2022. This trend, driven by an aging population and increasing interest in non-invasive beauty treatments, could contribute to Revance Therapeutics' growth.

These factors are expected to drive growth for Revance Therapeutics, Inc. in 2022, based on information available up to 2022-02-28.

## 0001493152-19-003817 — Eton Pharmaceuticals, Inc. (2019)
### # Words: T MDA: 2520, T+1 MDA: 3772
### LAB Words:
- biorphen, Count in T: 0, Count in T+1: 14
-!contract, Count in T: 0, Count in T+1: 8
- wholesalers, Count in T: 0, Count in T+1: 9
### Explanation:
Approved in October 2019
https://www.drugs.com/history/biorphen.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2019-03-25, predict the main growth drivers for Eton Pharmaceuticals, Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0174 (4/230)
Based on information available up to 2019-03-25, Eton Pharmaceuticals, Inc.'s main growth drivers for 2019 are expected to be:

1. **ET-202 and ET-203 approvals and commercialization**: Eton's pipeline products, including ET-202 (a ready-to-use formulation of phenylephrine) and ET-203 (a formulation of a corticosteroid), were expected to drive growth in 2019. The company had submitted New Drug Applications (NDAs) for these products and was awaiting FDA approval.

2. **```Biorphen``` (phenylephrine) launch**: Eton's lead product, ```Biorphen```, a ready-to-use formulation of phenylephrine, was approved by the FDA in 2018. The commercial launch of ```Biorphen``` was expected to be a significant growth driver for the company in 2019.

3. **Partnerships and collaborations**: Eton had established partnerships with pharmaceutical companies to develop and commercialize its products. These partnerships were expected to contribute to the company's growth in 2019.

4. **Expansion of product pipeline**: Eton had a pipeline of products in various stages of development, including ET-104, a formulation of an anesthetic agent. The advancement of these products through clinical trials and regulatory approvals was expected to drive growth for the company in 2019.

5. **Increased adoption of ready-to-use formulations**: The growing demand for ready-to-use formulations in the pharmaceutical industry was expected to benefit Eton, as its products, including ```Biorphen```, were designed to meet this need.

These growth drivers were expected to contribute to Eton Pharmaceuticals' revenue growth and expansion in 2019.

## 0001493152-22-005304 — Provention Bio, Inc. (2022)
### # Words: T MDA: 6132, T+1 MDA: 8786
### LAB Words:
- tzield, Count in T: 0, Count in T+1: 43
- merger, Count in T: 0, Count in T+1: 18
- sanofi, Count in T: 0, Count in T+1: 25
### Explanation:
The term tzield was used before the FDA approval.
https://www.fda.gov/media/165364/download?utm_source=chatgpt.com
### Verdict: Noise
### Input:
Using only information through 2022-02-24, predict the main growth drivers for Provention Bio, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0040 (1/253)
Based on information available up to 2022-02-24, the main growth drivers for Provention Bio, Inc. in 2022 are expected to be:

1. **Teplizumab (```TZIELD```)**: Provention Bio's lead product candidate, Teplizumab, is a monoclonal antibody that targets CD3 receptors on T cells to prevent the onset of type 1 diabetes (T1D). The company submitted a Biologics License Application (BLA) to the FDA in January 2021, and a potential approval in 2022 could drive significant growth.

2. **Type 1 Diabetes Prevention Market**: The global T1D market is growing, driven by increasing awareness and diagnosis rates. Provention Bio's focus on preventing T1D, rather than just treating its symptoms, positions the company to capitalize on this trend.

3. **Partnerships and Collaborations**: Provention Bio has established partnerships with organizations like the Juvenile Diabetes Research Foundation (JDRF) and the National Institutes of Health (NIH). These collaborations can provide access to funding, expertise, and resources, driving growth and development.

4. **Pipeline Development**: Provention Bio has a pipeline of product candidates targeting autoimmune diseases, including PRV-3279 (a CD32B-targeting antibody) and PRV-101 (a coxsackievirus B vaccine). Advancements in these programs could contribute to the company's growth in 2022.

5. **Increased Research and Development (R&D) Investment**: Provention Bio has been investing heavily in R&D, which is expected to continue in 2022. This investment should drive progress in the company's pipeline and support growth.

These factors are expected to drive Provention Bio's growth in 2022, assuming the company continues to execute its business strategy and receives favorable regulatory decisions.

## 0001493152-22-007377 — Greenwich LifeSciences, Inc. (2022)
### # Words: T MDA: 1676, T+1 MDA: 2008
### LAB Words:
- increases, Count in T: 0, Count in T+1: 6
- asu, Count in T: 0, Count in T+1: 6
- leases, Count in T: 0, Count in T+1: 6
- topic, Count in T: 0, Count in T+1: 5
### Explanation:
Noise - increases
### Verdict: Noise
### Input:
Using only information through 2022-03-21, predict the main growth drivers for Greenwich LifeSciences, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0041 (1/246)
Based on information available up to 2022-03-21, Greenwich LifeSciences, Inc. is a clinical-stage biopharmaceutical company focused on the development of GP2, an immunotherapy designed to prevent the recurrence of breast cancer. 

The main growth drivers for Greenwich LifeSciences, Inc. in 2022 are likely to be:

1. **Advancements in GP2 Clinical Trials**: The company's lead product candidate, GP2, has shown promising results in Phase IIb clinical trials. Positive outcomes from ongoing and future clinical trials, including the planned Phase III trial, could drive growth and attract investors.

2. **Regulatory Approvals and Milestones**: Achieving regulatory milestones, such as FDA Fast Track designation or Breakthrough Therapy designation, could accelerate GP2's development and commercialization, driving growth for the company.

3. **Partnerships and Collaborations**: Establishing partnerships with pharmaceutical companies, research institutions, or other organizations could provide Greenwich LifeSciences with access to additional resources, expertise, and funding, driving growth and expansion.

4. **Increasing Awareness and Recognition**: As Greenwich LifeSciences continues to present its research and clinical trial results at conferences and publish in reputable scientific journals, the company may gain more recognition and credibility within the scientific and investment communities, potentially attracting new investors and driving growth.

5. **Growing Demand for Breast Cancer Treatments**: The global breast cancer market is expected to continue growing due to increasing incidence rates and the need for more effective treatments. Greenwich LifeSciences' focus on developing an innovative immunotherapy for breast cancer could position the company for growth as the demand for effective treatments ```increases```.

## 0001549595-23-000021 — Nurix Therapeutics, Inc. (2023)
### # Words: T MDA: 7212, T+1 MDA: 8446
### LAB Words:
- pfizer, Count in T: 0, Count in T+1: 24
### Explanation:
Parternship announced September 2023 with Pfizer's now subsidiary Seagen
https://ir.nurixtx.com/news-releases/news-release-details/nurix-announces-strategic-collaboration-seagen-combining
### Verdict: Strong LAB
### Input:
Using only information through 2023-02-09, predict the main growth drivers for Nurix Therapeutics, Inc. in 2023. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0031 (1/326)
Based on publicly available information as of 2023-02-09, I'll predict the main growth drivers for Nurix Therapeutics, Inc. in 2023:

1. **Ongoing progress in clinical trials for NIX-323 (NMDA receptor antagonist)**: Nurix is developing NMDA receptor antagonists for the treatment of Alzheimer's disease and other neurodegenerative disorders. Successful completion of ongoing clinical trials, such as the Phase 2 trial for NMDA receptor antagonist NIX-323, could drive growth through potential regulatory approvals and commercialization.
2. **Expansion of the company's pipeline beyond NMDA receptor antagonists**: In addition to NMDA receptor antagonists, Nurix is developing other programs targeting protein-protein interactions in the SH3 domain family. Growth may come from the advancement of these pipeline programs, which could provide new opportunities for the company to expand its product portfolio and address various diseases.
3. **Partnerships and collaborations with pharmaceutical companies**: Nurix has partnered with pharmaceutical companies, such as ```Pfizer```, to develop its pipeline programs. Growth may come from the successful execution of these partnerships, which could provide access to new resources, expertise, and commercialization opportunities.
4. **Increased focus on oncology and other high-value therapeutic areas**: In 2022, Nurix has stated its intention to expand its focus on oncology and other high-value therapeutic areas. Growth may come from the company's ability to successfully transition its pipeline programs into these high-value areas and secure new partnerships or funding.
5. **Continued growth in the biotech sector**: The biotech sector has been growing rapidly in recent years, driven by increased investment in R&D, new technologies, and a growing need for innovative treatments. As a member of this sector, Nurix is likely to benefit from the overall growth trend.

Please note that these growth drivers are based on publicly available information as of 2023-02-09 and are subject to change as new information becomes available.

**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0025 (1/394)
Based on publicly available information through 2023-02-09, I'll provide an analysis of the main growth drivers for Nurix Therapeutics, Inc. in 2023:

1. **Orally bioavailable small molecule degraders**: Nurix Therapeutics is a biopharmaceutical company focused on developing orally bioavailable small molecule degraders that target protein-protein interactions (PPIs). The company's lead program, NX-1607, is a small molecule degrader targeting the BCL-2/ BCL-XL PPI. The orally bioavailable nature of its lead program could be a significant growth driver, as it may offer a more convenient and patient-friendly treatment option compared to injectable therapies.
2. **Targeting cancer and neurodegenerative diseases**: Nurix's initial focus on cancer and neurodegenerative diseases, such as amyotrophic lateral sclerosis (ALS), could provide a growth driver in 2023. The company's lead program, NX-1607, is being developed for the treatment of B-cell lymphoma, multiple myeloma, and other hematological malignancies. The company's expansion into neurodegenerative diseases, such as ALS, could also provide a growth driver, given the significant unmet medical need in this area.
3. **Partnerships and collaborations**: Nurix Therapeutics has partnered with several pharmaceutical companies, including ```Pfizer```, Bristol Myers Squibb, and Celgene (a subsidiary of Bristol Myers Squibb). These partnerships could provide a growth driver in 2023, as they may lead to increased funding, expertise, and access to new markets and customers.
4. **Clinical trial progress**: The company's lead program, NX-1607, is currently in Phase 1 clinical trials. Positive results from these trials could be a significant growth driver in 2023, as they may lead to increased investor interest, partnerships, and regulatory approvals.
5. **Competitive landscape**: The company's focus on orally bioavailable small molecule degraders could provide a growth driver in 2023, as this approach may be more competitive in the market compared to other approaches, such as injectable therapies.
6. **Investor interest**: Nurix Therapeutics has received significant investment from venture capital firms, including the Series C financing round in 2022. Continued investor interest in the company's technology and pipeline could be a growth driver in 2023, as it may lead to increased funding and access to new markets and customers.

These are the main growth drivers for Nurix Therapeutics, Inc. in 2023, based on publicly available information through 2023-02-09.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0024 (1/412)
Based on publicly available information through 2023-02-09, here are some potential growth drivers for Nurix Therapeutics, Inc. in 2023:

1. **Advancements in Targeted Protein Degradation (TPD) Technology**: Nurix Therapeutics is a leader in the development of TPD technology, which allows for the selective degradation of disease-causing proteins. As the company continues to advance its TPD platform, it may attract more attention from investors, partners, and potential customers, driving growth.
2. **Pipeline Expansion**: Nurix Therapeutics has a pipeline of preclinical and clinical-stage programs targeting various diseases, including cancer, neurodegenerative disorders, and autoimmune diseases. The company's ability to advance its pipeline and bring new programs into the clinic could drive growth through increased visibility, partnerships, and potential licensing deals.
3. **Partnerships and Collaborations**: Nurix Therapeutics has already established partnerships with several pharmaceutical companies, including a collaboration with ```Pfizer``` to develop TPD-based therapies for cancer. The company may continue to form new partnerships, expanding its reach and resources, and driving growth through access to new markets and technologies.
4. **Investor Interest and Funding**: Nurix Therapeutics has received significant funding from investors, including a $100 million Series C financing round in 2021. The company's ability to attract and retain investors may continue to drive growth through increased resources and visibility.
5. **Regulatory Advancements**: The FDA has granted Fast Track designation to Nurix Therapeutics' lead program, NX-1607, for the treatment of multiple myeloma. Regulatory advancements, such as this designation, can accelerate the development and approval process, driving growth through increased visibility and potential revenue.
6. **Expansion into New Therapeutic Areas**: Nurix Therapeutics has a broad pipeline across various therapeutic areas, including cancer, neurodegenerative disorders, and autoimmune diseases. The company's ability to expand into new therapeutic areas may drive growth through increased visibility, partnerships, and potential licensing deals.
7. **Increased Focus on Precision Medicine**: Nurix Therapeutics' TPD technology has the potential to enable precision medicine approaches, where therapies are tailored to specific patient subpopulations. As the company advances its pipeline and partnerships, it may increase its focus on precision medicine, driving growth through improved efficacy and reduced side effects.

These growth drivers are based on publicly available information and may not be exhaustive. The actual growth drivers for Nurix Therapeutics in 2023 may differ based on various factors, including the company's execution, market conditions, and unforeseen events.

## 0001558370-19-001601 — ALBIREO PHARMA, INC. (2019)
### # Words: T MDA: 5912, T+1 MDA: 7082
### LAB Words:
- odevixibat, Count in T: 0, Count in T+1: 26
### Explanation:
A2450 mentioned 323 times in 2019 10-K
Odevixibat name first used on January 25th, 2021
https://www.sec.gov/Archives/edgar/data/1322505/000110465921006884/tm213952d1_ex99-1.htm?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2019-03-06, predict the main growth drivers for ALBIREO PHARMA, INC. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0071 (2/281)
Based on information available up to 2019-03-06, the main growth drivers for Albireo Pharma, Inc. in 2019 are expected to be:

1. **```Odevixibat``` (A4250)**: Albireo's lead product candidate, a highly potent and selective inhibitor of the ileal bile acid transporter, is expected to drive growth. ```Odevixibat``` has shown promising results in clinical trials for the treatment of rare pediatric liver diseases, such as progressive familial intrahepatic cholestasis (PFIC) and biliary atresia. The company plans to initiate a Phase 3 trial for PFIC in 2019.

2. **Expansion of bile acid modulation pipeline**: Albireo is exploring the therapeutic potential of bile acid modulation in various liver and gastrointestinal diseases. The company's pipeline includes several preclinical and early-stage clinical programs, which are expected to advance in 2019, driving growth and potentially leading to new partnerships or collaborations.

3. **Partnerships and collaborations**: Albireo has established partnerships with companies like EA Pharma Co., Ltd. (EA Pharma) for the development and commercialization of elobixibat in Japan. The company may explore additional partnerships or collaborations in 2019 to further develop its pipeline and expand its global reach.

4. **Regulatory milestones**: Albireo expects to achieve regulatory milestones in 2019, including the potential approval of elobixibat in Japan for the treatment of chronic constipation. These milestones can drive growth by providing access to new markets and revenue streams.

5. **Increased research and development (R&D) investment**: Albireo plans to invest in R&D to advance its pipeline and explore new therapeutic areas. This investment is expected to drive growth by potentially leading to new product candidates and expanding the company's addressable market.

These growth drivers are based on Albireo's business strategy, pipeline, and market trends up to 2019-03-06.

## 0001558370-20-002536 — Scholar Rock Holding Corp (2020)
### # Words: T MDA: 7246, T+1 MDA: 8156
### LAB Words:
- apitegromab, Count in T: 0, Count in T+1: 22
- covid-19, Count in T: 0, Count in T+1: 19
- pandemic, Count in T: 0, Count in T+1: 19
### Explanation:
Covid
### Verdict: Strong LAB
### Input:
Using only information through 2020-03-12, predict the main growth drivers for Scholar Rock Holding Corp in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0043 (2/462)
Based on publicly available information through 2020-03-12, I'll attempt to predict the main growth drivers for Scholar Rock Holding Corp in 2020. Keep in mind that these are educated guesses and may not be entirely accurate.

Scholar Rock Holding Corp is a biopharmaceutical company focused on the discovery and development of small molecule inhibitors of the transforming growth factor-beta (TGF-β) pathway. Here are some potential growth drivers for the company in 2020:

1. **Advancements in SRK-015**: Scholar Rock's lead candidate, SRK-015, is a potent and selective inhibitor of the TGF-β pathway. In 2019, the company reported positive interim results from a Phase 1 clinical trial of SRK-015 in patients with facioscapulohumeral muscular dystrophy (FSHD). In 2020, the company may continue to advance SRK-015 through clinical trials, potentially leading to increased visibility and interest from investors.
2. **Expansion of the TGF-β pipeline**: Scholar Rock has a robust pipeline of TGF-β inhibitors, including SRK-015, SRK-181, and SRK-333. The company may continue to advance these programs through preclinical and clinical development, increasing the potential for multiple revenue streams and growth opportunities.
3. **Partnerships and collaborations**: Scholar Rock may form partnerships or collaborations with pharmaceutical companies, research institutions, or other organizations to accelerate the development of its pipeline candidates or to access new technologies and expertise. Such partnerships can provide access to additional resources, expertise, and geographic reach, driving growth and increasing the company's visibility.
4. **Regulatory updates**: Scholar Rock may receive updates from regulatory agencies, such as the FDA, regarding the status of its clinical trials or the approval process for its pipeline candidates. Positive regulatory updates can lead to increased investor confidence and growth in the company's stock price.
5. **Increased focus on rare diseases**: Scholar Rock has a strong focus on rare diseases, and the company may continue to prioritize the development of treatments for these conditions. As the company advances its pipeline candidates, it may attract attention from investors and patients with rare diseases, driving growth and increasing the company's visibility.
6. **Expansion of the management team and board**: Scholar Rock may add experienced executives or board members with a track record of success in the biopharmaceutical industry. This can bring new expertise, networks, and resources to the company, driving growth and increasing the company's credibility.

These are some potential growth drivers for Scholar Rock Holding Corp in 2020. The company's actual growth drivers may differ, and the company's performance may be influenced by various factors, including the ```COVID-19``` ```pandemic```, changes in the biopharmaceutical industry, and the company's ability to execute on its development plans.

## 0001558370-21-001730 — ALBIREO PHARMA, INC. (2021)
### # Words: T MDA: 6506, T+1 MDA: 8725
### LAB Words:
- bylvay, Count in T: 0, Count in T+1: 51
### Explanation:
Bylvay was approved by the FDA on July 20, 2021, not January 2021
https://www.biospace.com/albireo-announces-expanded-phase-3-data-on-bylvay-odevixibat-and-a3907-at-upcoming-easl-international-liver-congress?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2021-02-25, predict the main growth drivers for ALBIREO PHARMA, INC. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0191 (7/367)
Based on publicly available information through 2021-02-25, here are some potential main growth drivers for Albireo Pharma, Inc. in 2021:

1. **Orphan Drug Enzyme Replacement Therapy (ERT) for Progressive Cholestasis (PBC)**: Albireo's lead product, ```Bylvay``` (odevaximab), is an oral ERT for the treatment of PBC, a rare liver disease. The FDA approval of ```Bylvay``` in January 2021 is expected to drive growth, as it provides a new treatment option for patients with PBC.
2. **Growing Market Opportunity in PBC**: The PBC market is expected to grow as the disease becomes more recognized and diagnosed. Albireo's ```Bylvay``` is the first oral ERT for PBC, which may increase its market share as more patients and physicians become aware of the treatment option.
3. **Expanded Distribution and Marketing Efforts**: Albireo has been expanding its commercial infrastructure and distribution network in the US and Europe. As the company continues to build its sales and marketing efforts, it may increase its market share and revenue.
4. **Partnerships and Collaborations**: Albireo has partnered with various organizations, such as the National PBC Foundation, to raise awareness about PBC and ```Bylvay```. These partnerships may help increase the company's visibility and drive growth.
5. **Increasing Competition in the Gastrointestinal (GI) Market**: The GI market is becoming increasingly competitive, with several new treatments and products being approved or in development. Albireo's ```Bylvay``` may benefit from this competition, as patients and physicians become more aware of the treatment options available for PBC.
6. **Potential for Label Expansion**: Albireo may seek to expand the label for ```Bylvay``` to include additional indications, such as other liver diseases. If successful, this could increase the product's market potential and drive growth.
7. **Increasing Reimbursement and Access**: As ```Bylvay``` becomes more widely available, reimbursement and access to the treatment may improve, driving growth in sales and revenue.

Please note that these are potential growth drivers based on publicly available information and may not be a comprehensive or exhaustive list. The actual growth drivers for Albireo Pharma, Inc. in 2021 may differ.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0167 (6/360)
Based on publicly available information through 2021-02-25, here are some potential growth drivers for Albireo Pharma, Inc. in 2021:

1. **Orphan Drug Designation for ```Bylvay``` (odevzantib):** Albireo's lead product, ```Bylvay``` (odevzantib), received orphan drug designation from the FDA for the treatment of progressive familial intrahepatic cholestasis (PFIC) in 2020. This designation can provide market exclusivity and other benefits, which could drive growth for the company.
2. **PFIC Market Opportunity:** PFIC is a rare genetic disorder that affects the liver's ability to transport bile salts, leading to severe liver damage and other complications. With the orphan drug designation, Albireo is well-positioned to capture a significant share of the PFIC market, which is estimated to be around $1.5 billion by 2025.
3. **Commercialization of ```Bylvay```:** Albireo plans to commercialize ```Bylvay``` in the US and Europe, which could drive revenue growth in 2021. The company has established a commercial team and has partnered with specialty pharmacies to support the launch.
4. **Expansion into Other Indications:** Albireo is exploring the potential of ```Bylvay``` in other indications, such as primary sclerosing cholangitis (PSC) and biliary atresia. If successful, this could expand the product's addressable market and drive growth.
5. **Partnerships and Collaborations:** Albireo has partnered with companies like AstraZeneca and other pharmaceutical companies to develop and commercialize its products. These partnerships can provide access to new markets, technologies, and expertise, which could drive growth.
6. **Regulatory Approvals:** Albireo is also developing a pipeline of products, including a potential treatment for biliary atresia. Regulatory approvals for these products could provide additional growth opportunities for the company.
7. **Increased Awareness and Education:** As the company continues to raise awareness about PFIC and other rare liver diseases, it may attract more patients and healthcare professionals, driving growth through increased adoption of ```Bylvay``` and other products.

These factors could contribute to Albireo Pharma's growth in 2021, but it's essential to note that the company's actual performance may vary based on various market and regulatory factors.

**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0136 (5/368)
Based on publicly available information through 2021-02-25, here are some potential main growth drivers for Albireo Pharma, Inc. in 2021:

1. **Orphan drug Enthera (enzymes for the treatment of orphan diseases):** The company's lead product, ```Bylvay``` (odevrix), is an enzyme replacement therapy for the treatment of primary sclerosing cholangitis (PSC), a rare liver disease. The FDA approval of ```Bylvay``` in 2020 and the European Medicines Agency (EMA) approval in 2021 are expected to drive growth.
2. **Expanding product pipeline:** Albireo has a pipeline of additional enzyme replacement therapies for other orphan diseases, including Bytanisha (a treatment for cystic fibrosis) and a potential treatment for Gaucher disease. The company's pipeline may generate revenue growth in the coming years.
3. **Partnerships and collaborations:** Albireo has partnered with pharmaceutical companies, such as Abbott, to develop and commercialize its products. These partnerships may provide additional revenue streams and accelerate growth.
4. **Increasing awareness of orphan diseases:** The company's focus on orphan diseases, which affect relatively small patient populations, may benefit from growing awareness of these diseases and an increasing recognition of the need for effective treatments.
5. **Expanding global reach:** The company's European Medicines Agency (EMA) approval of ```Bylvay``` in 2021 may enable Albireo to expand its geographic reach, increasing sales in the European Union and other countries.
6. **Increasing competition in the pharmaceutical market:** The company's focus on a niche area of the market (orphan diseases) may allow it to grow market share as larger pharmaceutical companies may not be as competitive in this area.
7. **Improving market access:** The company's efforts to improve market access for ```Bylvay```, including the establishment of a patient support program, may increase sales and growth.
8. **Increasing revenue from existing products:** The company's existing product, ```Bylvay```, is expected to generate increasing revenue as it gains market share and as the company expands its marketing and sales efforts.

Please note that these predictions are based on publicly available information and may not reflect the full scope of the company's growth drivers.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0040 (1/251)
Based on information available up to 2021-02-25, I predict the main growth drivers for Albireo Pharma, Inc. in 2021 to be:

1. **Odevixibat (```Bylvay```)**: Albireo's lead product candidate, a highly potent and selective inhibitor of the ileal bile acid transporter, is expected to drive growth. Odevixibat has received FDA approval for the treatment of pruritus in patients with progressive familial intrahepatic cholestasis (PFIC) and has shown promising results in clinical trials for other cholestatic liver diseases.

2. **Expansion of Clinical Trials**: Albireo plans to initiate and expand clinical trials for odevixibat in various indications, including Alagille syndrome, biliary atresia, and primary sclerosing cholangitis. Positive results from these trials could lead to increased investor confidence and growth.

3. **Partnerships and Collaborations**: Albireo has established partnerships with companies like Genfit and has a licensing agreement with EA Pharma for the development and commercialization of elobixibat in certain countries. These partnerships could provide revenue streams and support growth.

4. **Regulatory Approvals**: Albireo expects to receive regulatory approvals for odevixibat in various countries, including the European Union and Japan. These approvals would expand the company's market reach and drive growth.

5. **Increasing Awareness of Cholestatic Liver Diseases**: Albireo's efforts to raise awareness about cholestatic liver diseases, such as PFIC and Alagille syndrome, could lead to increased diagnosis and treatment rates, driving demand for odevixibat and supporting growth.

These growth drivers are based on Albireo's product pipeline, clinical trial plans, and partnerships, as well as the increasing awareness of cholestatic liver diseases.

## 0001558370-21-001839 — Cara Therapeutics, Inc. (2021)
### # Words: T MDA: 11866, T+1 MDA: 13117
### LAB Words:
- difelikefalin, Count in T: 0, Count in T+1: 54
### Explanation:
Both of these are found in the T and T+1 MDA
### Verdict: Noise
### Input:
Using only information through 2021-02-25, predict the main growth drivers for Cara Therapeutics, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0038 (1/263)
Based on information available up to 2021-02-25, the main growth drivers for Cara Therapeutics, Inc. in 2021 are expected to be:

1. **KORSUVA (```difelikefalin```) injection**: The company's lead product candidate, KORSUVA, is a kappa opioid receptor agonist being developed for the treatment of moderate-to-severe pruritus (itching) in patients with chronic kidney disease (CKD) undergoing hemodialysis. Positive Phase 3 trial results and a potential FDA approval in 2021 could drive growth.

2. **Oral KORSUVA**: Cara Therapeutics is also developing an oral formulation of KORSUVA for the treatment of pruritus in patients with non-dialysis-dependent CKD and atopic dermatitis. Progress in these programs could expand the company's market opportunities.

3. **Partnerships and collaborations**: Cara Therapeutics has partnerships with companies like Fresenius Medical Care North America and Vifor Pharma to commercialize KORSUVA in the US and international markets. These partnerships could provide significant revenue streams and drive growth.

4. **Expansion of the company's pipeline**: Cara Therapeutics is exploring the potential of its kappa opioid receptor agonist platform in other indications, such as chronic pain and gastroenterology. Advancements in these programs could create new growth opportunities.

5. **Increased recognition of pruritus as a significant unmet medical need**: Growing awareness of the impact of pruritus on patients' quality of life and the lack of effective treatments could lead to increased demand for Cara Therapeutics' products and drive growth.

These factors are expected to contribute to Cara Therapeutics' growth in 2021, driven by the potential approval and commercialization of KORSUVA, expansion of the company's pipeline, and increasing recognition of the unmet medical need in pruritus treatment.

## 0001558370-22-003335 — BioXcel Therapeutics, Inc. (2022)
### # Words: T MDA: 5332, T+1 MDA: 5500
### LAB Words:
- consolidated, Count in T: 0, Count in T+1: 11
- igalmi, Count in T: 0, Count in T+1: 28
### Explanation:
Igalmi name revealed on April 6, 2022
https://ir.bioxceltherapeutics.com/news-releases/news-release-details/bioxcel-therapeutics-announces-fda-approval-igalmitm?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2022-03-11, predict the main growth drivers for BioXcel Therapeutics, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0153 (4/261)
Based on information available up to 2022-03-11, the main growth drivers for BioXcel Therapeutics, Inc. in 2022 are expected to be:

1. **```IGALMI``` (BXCL501)**: BioXcel's lead product candidate, ```IGALMI```, is a sublingual film formulation of dexmedetomidine for the acute treatment of agitation associated with schizophrenia and bipolar disorder. The company submitted a New Drug Application (NDA) to the FDA in 2021, and a potential approval in 2022 could drive significant growth.

2. **BXCL701**: BioXcel's BXCL701 is an orally administered, systemic innate immunity activator for the treatment of aggressive forms of prostate cancer and other solid tumors. The company is conducting clinical trials for BXCL701, and positive results could lead to increased investor interest and growth.

3. **Partnerships and Collaborations**: BioXcel has established partnerships with pharmaceutical companies, such as Merck and Pfizer, to develop and commercialize its product candidates. These partnerships could provide significant revenue streams and drive growth in 2022.

4. **Expansion of Clinical Trials**: BioXcel is expanding its clinical trials for ```IGALMI``` and BXCL701, which could lead to increased R&D expenses but also drive growth through the advancement of its product pipeline.

5. **Growing Demand for Mental Health Treatments**: The COVID-19 pandemic has highlighted the need for effective treatments for mental health disorders, such as agitation associated with schizophrenia and bipolar disorder. BioXcel's ```IGALMI``` could benefit from this growing demand, driving growth in 2022.

These growth drivers are based on the company's product pipeline, partnerships, and market trends, and are subject to change based on various factors, including regulatory approvals, clinical trial results, and market conditions.

## 0001564590-19-004492 — Apellis Pharmaceuticals, Inc. (2019)
### # Words: T MDA: 8690, T+1 MDA: 12942
### LAB Words:
- pegcetacoplan, Count in T: 0, Count in T+1: 54
- sfj, Count in T: 0, Count in T+1: 64
### Explanation:
The term Pegcetacoplan was first used in later 2019
https://investors.apellis.com/news-releases/news-release-details/apellis-dosed-first-patient-phase-3-study-apl-2-treatment-naive?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2019-02-26, predict the main growth drivers for Apellis Pharmaceuticals, Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0095 (3/317)
Based on publicly available information through 2019-02-26, here are the main growth drivers for Apellis Pharmaceuticals, Inc. in 2019:

1. **Geographic Expansion of ```Pegcetacoplan``` (APL-2) Clinical Trials**: Apellis Pharmaceuticals is developing ```pegcetacoplan```, a complement inhibitor for the treatment of geographic atrophy (GA) secondary to age-related macular degeneration (AMD). In 2019, the company planned to initiate a Phase 3 clinical trial in the United States and Europe, which could lead to increased visibility and potential growth.
2. **Complement Inhibition in Rare Diseases**: Apellis' complement inhibition platform has the potential to address various rare diseases, including paroxysmal nocturnal hemoglobinuria (PNH), atypical hemolytic uremic syndrome (aHUS), and others. The company's focus on this area could lead to new partnerships, collaborations, and revenue streams.
3. **Partnerships and Collaborations**: Apellis had already established partnerships with companies like Biogen and the University of Pennsylvania to develop its complement inhibitors. In 2019, the company might have continued to explore partnerships to expand its pipeline and increase its reach.
4. **Regulatory Approvals**: Apellis had already received FDA Fast Track designation for ```pegcetacoplan``` in GA secondary to AMD. In 2019, the company might have been working towards obtaining regulatory approvals for its other pipeline candidates, which could have driven growth.
5. **Investor Interest and Funding**: Apellis had raised significant funding in 2018, and in 2019, the company might have continued to attract investor interest, potentially leading to increased funding and growth opportunities.
6. **Expansion of Clinical Trials in Other Indications**: Apellis had already initiated clinical trials in other indications, such as PNH and aHUS. In 2019, the company might have expanded its clinical trial portfolio to other rare diseases, which could have driven growth and increased visibility.

These factors could have contributed to Apellis Pharmaceuticals' growth in 2019.

## 0001564590-19-005514 — Aimmune Therapeutics, Inc. (2019)
### # Words: T MDA: 7386, T+1 MDA: 7132
### LAB Words:
- palforzia, Count in T: 0, Count in T+1: 27
### Explanation:
Palforzia approved on January 31, 2020
https://www.drugs.com/history/palforzia.html
### Verdict: Strong LAB
### Input:
Using only information through 2019-02-28, predict the main growth drivers for Aimmune Therapeutics, Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0267 (9/337)
Based on publicly available information through 2019-02-28, here are some potential growth drivers for Aimmune Therapeutics, Inc. in 2019:

1. **```Palforzia``` (AR101) approval and launch**: Aimmune's lead product, ```Palforzia``` (AR101), is an oral immunotherapy for peanut allergy. In January 2019, the FDA approved ```Palforzia``` for the treatment of peanut allergy in children and adolescents. A successful launch of ```Palforzia``` could drive growth for the company in 2019.
2. **Commercialization and market access**: With the approval of ```Palforzia```, Aimmune will need to establish a commercial infrastructure to support the launch, including sales, marketing, and distribution. The company's ability to secure market access, reimbursement, and insurance coverage for ```Palforzia``` could drive growth in 2019.
3. **Expansion of clinical pipeline**: Aimmune has a pipeline of other immunotherapy products in development, including AR101 for tree nut allergy and AR101 for multiple food allergies. Positive clinical trial results and progress in these programs could provide additional growth opportunities for the company in 2019.
4. **Partnerships and collaborations**: Aimmune has partnered with companies like Nestle Health Science and DBV Technologies to develop and commercialize its products. These partnerships could provide access to new markets, technologies, and expertise, driving growth for the company in 2019.
5. **Increasing awareness and adoption of immunotherapy**: Growing awareness and adoption of immunotherapy as a treatment option for food allergies could drive demand for Aimmune's products, including ```Palforzia```, in 2019.
6. **Expansion of the company's commercial organization**: Aimmune may invest in expanding its commercial organization to support the launch of ```Palforzia``` and other products, which could drive growth in 2019.
7. **Potential for label expansion**: Aimmune may seek to expand the label for ```Palforzia``` to include additional patient populations, such as adults or children with a history of anaphylaxis, which could drive growth in 2019.

These factors could contribute to the growth of Aimmune Therapeutics, Inc. in 2019.

## 0001564590-19-005543 — MyoKardia Inc (2019)
### # Words: T MDA: 7416, T+1 MDA: 3865
### LAB Words:
- danicamtiv, Count in T: 0, Count in T+1: 8
### Explanation:
Danicamtiv name used in T+1 MDA
https://www.sec.gov/ix?doc=/Archives/edgar/data/0001552451/000156459020007418/myok-10k_20191231.htm
### Verdict: Weak LAB (take)
### Input:
Using only information through 2019-02-28, predict the main growth drivers for MyoKardia Inc in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0086 (2/233)
Based on information available up to 2019-02-28, MyoKardia Inc. is a clinical-stage biopharmaceutical company focused on developing and commercializing therapies for the treatment of serious and neglected cardiovascular diseases. 

The main growth drivers for MyoKardia Inc. in 2019 are expected to be:

1. **Mavacamten (MYK-461)**: This is the company's lead product candidate, which is being developed for the treatment of hypertrophic cardiomyopathy (HCM). Positive results from the Phase 2 PIONEER-HCM clinical trial and the initiation of the Phase 3 EXPLORER-HCM trial are expected to drive growth and investor interest.

2. **```Danicamtiv``` (MYK-491)**: This is another key product candidate being developed for the treatment of dilated cardiomyopathy (DCM). The initiation of the Phase 2 study for ```danicamtiv``` is expected to drive growth and expand the company's pipeline.

3. **Strategic Partnerships**: MyoKardia's partnership with Sanofi for the development and commercialization of mavacamten is expected to provide significant funding and expertise, driving growth and reducing financial risks.

4. **Research and Development**: MyoKardia's continued investment in research and development is expected to drive growth by advancing its pipeline and identifying new product candidates.

5. **Regulatory Milestones**: The achievement of regulatory milestones, such as the potential approval of mavacamten by the FDA, is expected to drive growth and increase investor confidence.

Overall, MyoKardia's growth in 2019 is expected to be driven by the advancement of its product candidates, strategic partnerships, and regulatory milestones.

## 0001564590-19-005639 — NEKTAR THERAPEUTICS (2019)
### # Words: T MDA: 10044, T+1 MDA: 8850
### LAB Words:
- bempegaldesleukin, Count in T: 0, Count in T+1: 42
### Explanation:
Approved on August 1st, 2019
https://news.bms.com/news/partnering/2019/Nektar-Therapeutics-and-Bristol-Myers-Squibb-Announce-US-FDA-Breakthrough-Therapy-Designation-for-Bempegaldesleukin-NKTR-214-in-Combination-with-Opdivo-nivolumab-for-the-Treatment-of-Patients-with-Untreated-Advanced-Melanoma/default.aspx
### Verdict: Weak LAB (take)
### Input:
Using only information through 2019-03-01, predict the main growth drivers for NEKTAR THERAPEUTICS in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0045 (1/223)
Based on information available up to 2019-03-01, the main growth drivers for Nektar Therapeutics in 2019 are expected to be:

1. **NKTR-181 (Oxycodone extended-release tablets)**: Nektar's opioid analgesic, NKTR-181, was approved by the FDA in August 2018 for the treatment of moderate to severe chronic pain. The commercial launch of NKTR-181 was expected to drive revenue growth for the company in 2019.

2. **NKTR-214 (```Bempegaldesleukin```)**: Nektar's lead immuno-oncology candidate, NKTR-214, was in Phase 3 clinical trials for the treatment of various types of cancer, including melanoma, renal cell carcinoma, and urothelial carcinoma. Positive trial results and potential regulatory approvals were expected to drive growth for the company in 2019.

3. **Partnerships and Collaborations**: Nektar had partnerships with major pharmaceutical companies, including Bristol-Myers Squibb, Pfizer, and Eli Lilly, among others. These partnerships were expected to generate significant revenue for the company in 2019 through milestone payments and royalties.

4. **Pipeline Development**: Nektar had a robust pipeline of early-stage candidates in various therapeutic areas, including oncology, immunology, and pain management. Advancements in these programs were expected to drive growth for the company in 2019 through potential partnerships, licensing agreements, and regulatory approvals.

Overall, Nektar Therapeutics' growth in 2019 was expected to be driven by a combination of commercial success with NKTR-181, advancements in its pipeline programs, and revenue generated from partnerships and collaborations.

## 0001564590-19-005808 — SANGAMO THERAPEUTICS, INC (2019)
### # Words: T MDA: 5787, T+1 MDA: 4907
### LAB Words:
- biogen, Count in T: 0, Count in T+1: 10
### Explanation:
Partership with Biogen announced on February 27, 2020
https://www.globenewswire.com/news-release/2020/02/27/1992252/0/en/Biogen-and-Sangamo-Announce-Global-Collaboration-to-Develop-Gene-Regulation-Therapies-for-Alzheimer-s-Parkinson-s-Neuromuscular-and-Other-Neurological-Diseases.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2019-03-01, predict the main growth drivers for SANGAMO THERAPEUTICS, INC in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0031 (1/326)
Based on publicly available information up to 2019-03-01, here are some potential growth drivers for Sangamo Therapeutics, Inc. (SGMO) in 2019:

1. **Gene Editing Technology Advancements**: Sangamo's gene editing technology, based on zinc finger nucleases (ZFNs) and CRISPR-Cas9, has shown promise in treating genetic diseases. The company's ability to improve its gene editing tools and expand its product pipeline could drive growth.
2. **ZFP Therapeutics Platform**: Sangamo's ZFP Therapeutics platform has been used to develop treatments for various genetic diseases, including sickle cell disease, beta-thalassemia, and Huntington's disease. The company's ability to advance its ZFP Therapeutics platform and expand its pipeline could drive growth.
3. **Partnerships and Collaborations**: Sangamo has partnered with several companies, including Pfizer, ```Biogen```, and Sanofi, to develop and commercialize its gene editing technologies. These partnerships could lead to new revenue streams and growth opportunities.
4. **Regulatory Approvals**: Sangamo's lead product candidate, ST-400, is an investigational gene therapy for severe hemophilia A. The company may receive regulatory approvals for ST-400 in 2019, which could drive growth and revenue.
5. **Increased Focus on Gene Editing for Rare Diseases**: Sangamo has been expanding its focus on gene editing for rare diseases, which could lead to new growth opportunities and partnerships.
6. **Expansion of Gene Editing Applications**: The company's gene editing technology has the potential to be applied to a wide range of diseases, including cancer, cardiovascular disease, and neurological disorders. Expanding the applications of its technology could drive growth and increase its addressable market.
7. **Investment in Research and Development**: Sangamo has been investing in research and development to improve its gene editing technology and expand its pipeline. This investment could lead to new growth opportunities and partnerships.

These factors could contribute to the growth of Sangamo Therapeutics, Inc. in 2019.

**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0027 (1/369)
Based on publicly available information through 2019-03-01, here are some potential growth drivers for Sangamo Therapeutics, Inc. in 2019:

1. **Gene therapy pipeline progress**: Sangamo has a robust pipeline of gene therapy programs in various stages of development, including its lead program, ST-400, for the treatment of severe combined immunodeficiency due to adenosine deaminase deficiency (ADA-SCID). Positive clinical trial results and regulatory updates on these programs could drive growth.
2. **Gene editing partnerships**: Sangamo has partnered with several companies, including Pfizer, ```Biogen```, and others, to develop gene therapies using its zinc finger nuclease (ZFN) technology. These partnerships could lead to increased revenue and growth through milestone payments and royalties.
3. **Expansion of ZFN technology**: Sangamo's ZFN technology has the potential to be used in a wide range of therapeutic areas, including inherited diseases, cancer, and regenerative medicine. The company may expand its use of ZFNs in new areas, leading to increased revenue and growth.
4. **Increased focus on beta-thalassemia program**: In 2018, Sangamo announced positive results from a Phase 1/2 clinical trial of its beta-thalassemia program, ST-400. The company may continue to invest in this program, which could lead to growth through regulatory approvals and commercialization.
5. **Growing demand for gene therapies**: The gene therapy market is expected to grow rapidly in the coming years, driven by the increasing number of approved products and the potential for new indications. Sangamo's position in this market could lead to growth through increased demand for its products and services.
6. **Expansion of Sangamo's gene therapy manufacturing capabilities**: The company may invest in expanding its manufacturing capabilities to support the growing demand for its products, which could lead to increased revenue and growth.
7. **Potential for new indications and partnerships**: Sangamo's ZFN technology has the potential to be used in new indications, and the company may partner with other companies to develop new products, leading to growth through new revenue streams.

These are some of the potential growth drivers for Sangamo Therapeutics, Inc. in 2019 based on publicly available information through 2019-03-01.

**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0025 (1/400)
Based on publicly available information through 2019-03-01, here are some potential main growth drivers for Sangamo Therapeutics, Inc. in 2019:

1. **Gene therapy pipeline progress**: Sangamo has a robust pipeline of gene therapy programs in various stages of development, including its lead program, ST-400, for the treatment of Fabry disease. Positive clinical trial results and regulatory approvals could drive growth in 2019.
2. **Gene therapy pipeline expansion**: Sangamo has been expanding its pipeline through partnerships and internal research. In 2018, the company announced a partnership with Pfizer to develop a gene therapy for Huntington's disease. New partnerships and pipeline additions could drive growth through 2019.
3. **Gene editing technology advancements**: Sangamo's proprietary zinc finger nuclease (ZFN) and TALEN (transcription activator-like effector nuclease) gene editing technologies are key components of its gene therapy platform. Improvements to these technologies could increase the efficiency and effectiveness of its gene therapy programs, driving growth.
4. **Increased adoption of gene therapy**: The gene therapy market is expected to grow rapidly in 2019, driven by increasing awareness of the potential of gene therapies to treat previously incurable diseases. Sangamo's gene therapy programs could benefit from this growing interest and adoption.
5. **Partnerships and collaborations**: Sangamo has partnered with several large pharmaceutical companies, including Pfizer, ```Biogen```, and Gilead Sciences. New partnerships and collaborations could drive growth through 2019, providing access to new technologies, expertise, and revenue streams.
6. **Cash position and financial resources**: At the end of 2018, Sangamo had approximately $430 million in cash and cash equivalents, which should provide a strong foundation for continued investment in its pipeline programs and partnerships.
7. **Gene therapy regulatory environment**: The regulatory environment for gene therapies is expected to become more favorable in 2019, with the FDA and other regulatory agencies providing more guidance on the development and approval of these therapies. A more favorable regulatory environment could accelerate Sangamo's growth.
8. **Competitive positioning**: Sangamo's ZFN and TALEN technologies are considered among the most advanced in the gene therapy field. The company's competitive positioning could drive growth through 2019 as the gene therapy market expands.

These are some of the potential growth drivers for Sangamo Therapeutics, Inc. in 2019 based on publicly available information through 2019-03-01.

## 0001564590-19-009879 — Forty Seven, Inc. (2019)
### # Words: T MDA: 6311, T+1 MDA: 7872
### LAB Words:
- magrolimab, Count in T: 0, Count in T+1: 20
- repayment, Count in T: 0, Count in T+1: 17
### Explanation:
I may be wrong but I think that the name was used here, in 2017 
https://clinicaltrials.gov/study/NCT03248479
### Verdict: Noise
### Input:
Using only information through 2019-03-28, predict the main growth drivers for Forty Seven, Inc. in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0082 (2/244)
Based on information available up to 2019-03-28, Forty Seven, Inc., a clinical-stage immuno-oncology company, is expected to experience growth driven by the following main factors in 2019:

1. **Progress in ```Magrolimab``` (5F9) clinical trials**: Forty Seven's lead product candidate, ```Magrolimab```, is a monoclonal antibody targeting CD47. Positive results from ongoing clinical trials, particularly in combination with azacitidine for the treatment of myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML), are expected to drive growth.

2. **Expanding pipeline and new collaborations**: Forty Seven has a growing pipeline of immuno-oncology product candidates, including FSI-189 and FSI-174. New collaborations and partnerships, potentially with larger pharmaceutical companies, could accelerate the development of these candidates and drive growth.

3. **Increased recognition and adoption of CD47 as a therapeutic target**: As more research emerges on the role of CD47 in cancer, Forty Seven's expertise in targeting this pathway is likely to attract more attention and investment, driving growth.

4. **Growing demand for innovative cancer treatments**: The global cancer treatment market is expected to continue growing, driven by an aging population and increasing demand for more effective and targeted therapies. Forty Seven's focus on immuno-oncology positions the company to capitalize on this trend.

5. **IPO proceeds and funding**: Forty Seven completed its initial public offering (IPO) in June 2018, raising approximately $112 million. The company is expected to use these funds to advance its clinical programs, expand its pipeline, and build its organizational capabilities, driving growth in 2019.

## 0001564590-20-006408 — Allakos Inc. (2020)
### # Words: T MDA: 6070, T+1 MDA: 7010
### LAB Words:
- lirentelimab, Count in T: 0, Count in T+1: 28
### Explanation:
The answer mentions Phase 2 Trials. It was at best in Phase 1 as of 2020-02-25
https://www.globenewswire.com/news-release/2020/10/26/2114146/0/en/Allakos-Announces-Results-from-a-Phase-1-Study-of-Subcutaneously-Administered-Lirentelimab-AK002.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-25, predict the main growth drivers for Allakos Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0042 (1/237)
Based on information available up to 2020-02-25, the main growth drivers for Allakos Inc. in 2020 are expected to be:

1. **AK002 (```Lirentelimab```) Development**: Allakos' lead compound, AK002, is an anti-Siglec-8 antibody being developed for the treatment of eosinophilic gastrointestinal diseases (EGIDs) and other mast cell-related disorders. Positive results from clinical trials, including a Phase 2 study in EGIDs, are expected to drive growth and investor interest.

2. **Expanding Pipeline**: Allakos has a growing pipeline of preclinical programs targeting various diseases, including asthma, atopic dermatitis, and other inflammatory conditions. Advancements in these programs could contribute to the company's growth and diversification.

3. **Strategic Partnerships**: Allakos may explore partnerships or collaborations with larger pharmaceutical companies to accelerate the development and commercialization of its pipeline assets, including AK002. Such partnerships could provide significant funding and expertise, driving growth and increasing the company's visibility.

4. **Increasing Awareness of EGIDs**: As Allakos continues to develop AK002, the company is also working to raise awareness about EGIDs, a group of rare and underserved diseases. Increased awareness and understanding of these conditions could lead to greater recognition of the need for effective treatments, driving growth and demand for Allakos' products.

5. **Regulatory Milestones**: Allakos is expected to achieve various regulatory milestones in 2020, including potential orphan drug designations and Fast Track designations for AK002. These milestones could provide a catalyst for growth and increase investor confidence in the company's pipeline.

## 0001564590-20-007021 — Sage Therapeutics, Inc. (2020)
### # Words: T MDA: 12193, T+1 MDA: 12078
### LAB Words:
- biogen, Count in T: 0, Count in T+1: 44
### Explanation:
Parternship announced on November 27th 2020
https://investors.biogen.com/news-releases/news-release-details/biogen-and-sage-therapeutics-announce-global-collaboration
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-27, predict the main growth drivers for Sage Therapeutics, Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0040 (1/247)
Based on information available up to 2020-02-27, the main growth drivers for Sage Therapeutics, Inc. in 2020 are expected to be:

1. **Zulresso (brexanolone) sales growth**: Zulresso, the company's first FDA-approved product, was launched in June 2019 for the treatment of postpartum depression (PPD). As the first and only FDA-approved treatment for PPD, Zulresso is expected to continue to drive revenue growth for Sage in 2020.

2. **Potential approval and launch of zuranolone (SAGE-217)**: Zuranolone, an investigational oral therapy for major depressive disorder (MDD) and PPD, was in Phase 3 clinical trials as of 2020-02-27. If approved, zuranolone could become a significant growth driver for Sage, given its potential to address a larger patient population than Zulresso.

3. **Expansion of Zulresso's label**: Sage was exploring the potential for Zulresso to treat other indications, such as bipolar depression. If successful, label expansions could increase the addressable market for Zulresso and drive additional revenue growth.

4. **Strategic partnerships and collaborations**: Sage had a collaboration with ```Biogen``` to develop and commercialize zuranolone and SAGE-324, a potential treatment for essential tremor and other neurological disorders. This partnership could provide Sage with additional resources and expertise to support the development and commercialization of its pipeline assets.

5. **Advancements in the company's pipeline**: Sage had several other pipeline assets in various stages of development, including SAGE-718 for cognitive disorders and SAGE-904 for neurological disorders. Progress in these programs could contribute to the company's growth prospects in 2020 and beyond.

## 0001564590-20-007350 — Apellis Pharmaceuticals, Inc. (2020)
### # Words: T MDA: 12942, T+1 MDA: 12226
### LAB Words:
- sobi, Count in T: 0, Count in T+1: 36
### Explanation:
Parternship with Sobi was announced October 27th 2020
https://www.globenewswire.com/news-release/2020/10/27/2114976/0/en/Apellis-and-Sobi-Enter-Collaboration-for-Global-Co-development-and-Ex-US-Commercialization-of-Systemic-Pegcetacoplan-in-Rare-Diseases-with-Urgent-Need-for-New-Treatments.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-27, predict the main growth drivers for Apellis Pharmaceuticals, Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0050 (1/199)
Based on information available up to 2020-02-27, the main growth drivers for Apellis Pharmaceuticals, Inc. in 2020 are expected to be:

1. **Pegcetacoplan (APL-2)**: Apellis' lead product candidate, a C3 inhibitor for the treatment of paroxysmal nocturnal hemoglobinuria (PNH) and geographic atrophy (GA). Positive Phase 2 results in PNH and GA, and the initiation of Phase 3 trials, are expected to drive growth.
2. **Pipeline expansion**: Apellis' pipeline includes other complement inhibitors, such as APL-9, targeting various diseases, including autoimmune disorders and cancer. Advancements in these programs could contribute to growth.
3. **Strategic partnerships**: Apellis has collaborations with companies like Swedish Orphan Biovitrum AB (```Sobi```) for the development and commercialization of pegcetacoplan. These partnerships may provide additional revenue streams and support growth.
4. **Increased R&D investment**: Apellis has been investing heavily in research and development, which is expected to continue in 2020. This investment should drive progress in its pipeline and contribute to growth.
5. **Potential regulatory milestones**: Apellis may achieve regulatory milestones, such as FDA approval for pegcetacoplan, which could significantly drive growth.

These factors are expected to contribute to Apellis' growth in 2020, driven by the advancement of its pipeline, strategic partnerships, and increased investment in R&D.

## 0001564590-20-008141 — FATE THERAPEUTICS INC (2020)
### # Words: T MDA: 9469, T+1 MDA: 10742
### LAB Words:
- janssen, Count in T: 0, Count in T+1: 44
### Explanation:
Announced collaboration on April 2th 2020
https://ir.fatetherapeutics.com/news-releases/news-release-details/fate-therapeutics-announces-worldwide-collaboration-janssen
### Verdict: Strong LAB
### Input:
Using only information through 2020-03-02, predict the main growth drivers for FATE THERAPEUTICS INC in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0036 (1/281)
Based on information available up to 2020-03-02, the main growth drivers for Fate Therapeutics Inc. in 2020 are expected to be:

1. **Advancements in iPSC-derived cell therapies**: Fate Therapeutics is a leader in the development of induced pluripotent stem cell (iPSC)-derived cell therapies. The company's pipeline includes several programs that utilize iPSCs to create off-the-shelf, allogeneic cell therapies for various diseases, including cancer and autoimmune disorders. Progress in these programs is expected to drive growth.

2. **FT516 and FT596 programs**: Fate Therapeutics' lead product candidates, FT516 and FT596, are expected to be key growth drivers in 2020. FT516 is an iPSC-derived natural killer (NK) cell therapy for cancer, while FT596 is a chimeric antigen receptor (CAR) NK cell therapy for B-cell malignancies. Positive data from these programs could lead to increased investor interest and partnerships.

3. **Collaborations and partnerships**: Fate Therapeutics has established partnerships with major pharmaceutical companies, including ```Janssen``` Biotech and Ono Pharmaceutical. These collaborations provide significant funding and validation for the company's technology, and are expected to contribute to growth in 2020.

4. **Expansion of manufacturing capabilities**: To support the development of its cell therapies, Fate Therapeutics is investing in the expansion of its manufacturing capabilities. This includes the construction of a new manufacturing facility, which is expected to increase the company's ability to produce high-quality cell therapies and drive growth.

5. **Increased recognition of cell therapy potential**: The cell therapy space has gained significant attention in recent years, with several high-profile approvals and acquisitions. As the field continues to advance, Fate Therapeutics is well-positioned to benefit from increased recognition of the potential of cell therapies, driving growth and interest in the company's programs.

## 0001564590-20-011037 — Arcturus Therapeutics Holdings Inc. (2020)
### # Words: T MDA: 3855, T+1 MDA: 5424
### LAB Words:
- phase, Count in T: 0, Count in T+1: 12
- lunar-cov19, Count in T: 0, Count in T+1: 19
- vaccine, Count in T: 0, Count in T+1: 23
- trial, Count in T: 0, Count in T+1: 14
- singapore, Count in T: 0, Count in T+1: 20
- grant, Count in T: 0, Count in T+1: 11
### Explanation:
This is just noise 
### Verdict: Noise
### Input:
Using only information through 2020-03-16, predict the main growth drivers for Arcturus Therapeutics Holdings Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0422 (16/379)
Based on publicly available information up to 2020-03-16, here are some potential growth drivers for Arcturus Therapeutics Holdings Inc. in 2020:

1. **ARCT-810 (Lunenburg virus ```vaccine```)**: Arcturus is developing ARCT-810, a self-replicating RNA (repRNA) ```vaccine``` candidate for the prevention of Lassa fever, a severe and potentially life-threatening viral disease. The company has reported positive preclinical data, and a ```Phase``` 1 clinical ```trial``` was initiated in 2019. A successful outcome in this ```trial``` could lead to further development and commercialization, driving growth.
2. **ARCT-810's potential for use in pandemic preparedness**: The Lassa fever ```vaccine``` candidate has the potential to be used in pandemic preparedness and response efforts, which could be a significant growth driver for Arcturus. The company may receive funding and support from governments and organizations to develop and stockpile the ```vaccine```, providing a potential revenue stream.
3. **ARCT-021 (HBV ```vaccine```)**: Arcturus is also developing ARCT-021, a self-replicating RNA (repRNA) ```vaccine``` candidate for the prevention of Hepatitis B virus (HBV). A successful ```Phase``` 1 clinical ```trial``` in 2019 and ongoing ```Phase``` 2 clinical trials could lead to further development and commercialization, driving growth.
4. **Partnerships and collaborations**: Arcturus has partnered with various organizations, such as the Bill and Melinda Gates Foundation, to support the development of its ```vaccine``` candidates. These partnerships could provide funding, expertise, and access to new markets, driving growth.
5. **RepRNA technology**: Arcturus' proprietary repRNA technology has the potential to be used in the development of multiple ```vaccine``` candidates, which could lead to a pipeline of products and a diversified revenue stream. The company's technology could also be licensed to other companies, generating revenue through royalties.
6. **Growing demand for RNA-based vaccines**: The RNA-based ```vaccine``` market is growing, driven by the increasing demand for vaccines against infectious diseases. Arcturus' repRNA technology is well-positioned to capitalize on this trend, driving growth through the development and commercialization of its ```vaccine``` candidates.

These factors could contribute to the growth of Arcturus Therapeutics Holdings Inc. in 2020. However, the company's actual performance may be influenced by various factors, including the outcome of clinical trials, regulatory approvals, and market conditions.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0219 (7/319)
Based on publicly available information up to 2020-03-16, here are some potential growth drivers for Arcturus Therapeutics Holdings Inc. in 2020:

1. **COVID-19 ```Vaccine``` Development**: Arcturus Therapeutics is developing a COVID-19 ```vaccine``` candidate, ARCT-154, which is a self-amplifying RNA (saRNA) ```vaccine```. The company has received funding from the US government to support the development of this ```vaccine```, and it has been granted Fast Track designation by the FDA. A successful ```vaccine``` development and approval could lead to significant revenue growth for the company.
2. **Expansion of RNA-based Therapies**: Arcturus Therapeutics has a platform technology for the development of RNA-based therapies, including saRNA and messenger RNA (mRNA). The company has several programs in various stages of development, including oncology, infectious diseases, and rare genetic disorders. The expansion of this platform could lead to new product approvals and revenue growth.
3. **Partnerships and Collaborations**: Arcturus Therapeutics has partnered with several companies, including the US government, to support the development of its COVID-19 ```vaccine``` and other programs. These partnerships could provide access to new funding, expertise, and resources, which could drive growth for the company.
4. **Regulatory Advancements**: The FDA has granted Fast Track designation to Arcturus Therapeutics' COVID-19 ```vaccine``` candidate, which could expedite the development and review process. Additionally, the company has received Orphan Drug designation for its ARCT-810 program, which could provide additional regulatory benefits and incentives.
5. **Increased Focus on RNA-based Therapies**: The COVID-19 pandemic has accelerated the development and adoption of RNA-based therapies, which could lead to increased demand for Arcturus Therapeutics' products and technologies.

These factors could contribute to the growth of Arcturus Therapeutics Holdings Inc. in 2020, but it's essential to note that the company's actual performance may vary based on various market and regulatory factors.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0215 (5/233)
Based on information available up to 2020-03-16, the main growth drivers for Arcturus Therapeutics Holdings Inc. in 2020 are likely to be:

1. **COVID-19 ```Vaccine``` Development**: Arcturus Therapeutics had announced its plans to develop a COVID-19 ```vaccine``` using its ```LUNAR-COV19``` program, which leverages the company's proprietary LUNAR delivery technology and STARR mRNA technology. The rapid development of a COVID-19 ```vaccine``` was expected to drive growth for the company in 2020.

2. **Partnerships and Collaborations**: Arcturus Therapeutics had established partnerships with major pharmaceutical companies, such as Janssen Pharmaceuticals and Ultragenyx Pharmaceutical, to develop and commercialize its mRNA-based therapies. These partnerships were expected to provide significant funding and support for the company's research and development activities, driving growth in 2020.

3. **Advancements in mRNA Technology**: Arcturus Therapeutics' proprietary STARR mRNA technology was expected to drive growth in 2020 by enabling the development of novel mRNA-based therapies for various diseases, including rare genetic disorders and infectious diseases.

4. **Expansion of Pipeline**: Arcturus Therapeutics had a diverse pipeline of mRNA-based therapies in various stages of development, including programs for cystic fibrosis, ornithine transcarbamylase (OTC) deficiency, and glycogen storage disease type III. The advancement of these programs was expected to drive growth for the company in 2020.

Overall, Arcturus Therapeutics' growth in 2020 was expected to be driven by its COVID-19 ```vaccine``` development efforts, partnerships and collaborations, advancements in mRNA technology, and expansion of its pipeline.

**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0059 (2/340)
Based on publicly available information up to 2020-03-16, I predict the main growth drivers for Arcturus Therapeutics Holdings Inc. in 2020 to be:

1. **ARCT-810 (Lunginhaler)**: Arcturus is developing ARCT-810, a proprietary, inhaled RNAi therapeutic for the treatment of respiratory and pulmonary diseases, including cystic fibrosis and lung cancer. The company is planning to initiate a ```Phase``` 1 clinical ```trial``` for ARCT-810 in 2019, and assuming successful results, this program could drive growth in 2020.
2. **ARCT-810's companion diagnostic**: The development of a companion diagnostic for ARCT-810, which is expected to be a key factor in the program's success, could also drive growth in 2020. A companion diagnostic would help identify patients who are most likely to benefit from ARCT-810 treatment.
3. **Partnerships and collaborations**: Arcturus has partnered with several organizations, including the National Institutes of Health (NIH) and the Cystic Fibrosis Foundation Therapeutics Development Network, to support the development of ARCT-810. Additional partnerships and collaborations in 2020 could drive growth through access to new technologies, expertise, and funding.
4. **RNAi therapeutics market growth**: The RNAi therapeutics market is expected to grow rapidly in the coming years, driven by the potential of RNAi to treat a wide range of diseases. As a leader in the field, Arcturus is well-positioned to benefit from this growth, assuming the company can successfully develop and commercialize its products.
5. **Cash management and funding**: Arcturus had approximately $44.5 million in cash and cash equivalents as of December 31, 2019. Assuming the company manages its cash resources effectively, it should be able to fund its operations and development activities in 2020, including the ARCT-810 program.
6. **Competitive advantage of Arcturus' technology**: Arcturus' proprietary RNAi technology, including its lipid-mediated delivery system, may provide a competitive advantage in the development of RNAi therapeutics. If the company can successfully leverage this technology, it could drive growth in 2020.

## 0001564590-21-008915 — Vir Biotechnology, Inc. (2021)
### # Words: T MDA: 8444, T+1 MDA: 8723
### LAB Words:
- sotrovimab, Count in T: 0, Count in T+1: 41
### Explanation:
First use of the name March 26, 2021
https://www.idstewardship.com/sotrovimab/?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2021-02-25, predict the main growth drivers for Vir Biotechnology, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0035 (1/282)
Based on information available up to 2021-02-25, the main growth drivers for Vir Biotechnology, Inc. in 2021 are likely to be:

1. **COVID-19 treatment and prevention efforts**: Vir Biotechnology has been actively involved in developing treatments for COVID-19, including VIR-7831 (```sotrovimab```), a monoclonal antibody that targets the SARS-CoV-2 virus. The company's efforts in this area are expected to drive growth, particularly if their treatments receive regulatory approvals and are adopted by healthcare systems.

2. **Partnerships and collaborations**: Vir Biotechnology has established partnerships with major pharmaceutical companies, such as GlaxoSmithKline (GSK) and Alnylam Pharmaceuticals. These collaborations are expected to drive growth by providing access to new technologies, expertise, and resources, as well as potential revenue streams through milestone payments and royalties.

3. **Advancements in chronic hepatitis B treatment**: Vir Biotechnology has been developing VIR-2218, a RNA interference (RNAi) therapy for the treatment of chronic hepatitis B. The company's efforts in this area are expected to drive growth, particularly if their treatments demonstrate efficacy and safety in clinical trials.

4. **Expansion of pipeline**: Vir Biotechnology has a diverse pipeline of programs targeting various infectious diseases, including influenza, HIV, and tuberculosis. The company's efforts to advance these programs through clinical development are expected to drive growth, particularly if they demonstrate promising results and attract interest from investors and partners.

5. **Government funding and contracts**: Vir Biotechnology has received funding from government agencies, such as the U.S. Department of Health and Human Services, to support the development of treatments for infectious diseases. The company's ability to secure additional government funding and contracts is expected to drive growth, particularly if they are able to leverage these resources to advance their pipeline programs.

## 0001564590-21-009467 — CYTOKINETICS INC (2021)
### # Words: T MDA: 6766, T+1 MDA: 6043
### LAB Words:
- aficamten, Count in T: 0, Count in T+1: 34
- loans, Count in T: 0, Count in T+1: 14
### Explanation:
The name was likely first used in October 2021
https://pubs.acs.org/doi/10.1021/acs.jmedchem.1c01290
### Verdict: Weak LAB (take)
### Input:
Using only information through 2021-02-26, predict the main growth drivers for CYTOKINETICS INC in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0093 (2/216)
Based on information available up to 2021-02-26, the main growth drivers for Cytokinetics, Inc. in 2021 are expected to be:

1. **Omadacycline and ```Aficamten``` (CK-274)**: Cytokinetics' cardiac myosin inhibitor, ```aficamten``` (CK-274), was in Phase II clinical trials for the treatment of hypertrophic cardiomyopathy (HCM) and non-obstructive HCM. Positive results from these trials could drive growth.

2. **Reldesemtiv (CK-2127107)**: Reldesemtiv, a fast skeletal muscle troponin activator, was being developed in collaboration with Astellas Pharma for the treatment of amyotrophic lateral sclerosis (ALS) and spinal muscular atrophy (SMA). Progress in these trials could contribute to growth.

3. **CK-271 (CK-601)**: CK-271, a cardiac myosin inhibitor, was in Phase I clinical trials for the treatment of HCM. Positive results from these trials could drive growth.

4. **Partnerships and Collaborations**: Cytokinetics had partnerships with companies like Astellas Pharma and Amgen. These collaborations could provide significant funding and support for the development of their pipeline candidates, driving growth.

5. **Pipeline Expansion**: Cytokinetics had a diverse pipeline of muscle-directed therapies, including compounds in various stages of development for the treatment of muscle-related diseases. Advancements in these programs could contribute to growth.

These growth drivers are based on the company's pipeline and partnerships as of 2021-02-26. The actual growth drivers may have varied depending on various factors, including trial outcomes and regulatory developments.

## 0001564590-21-009624 — REATA PHARMACEUTICALS INC (2021)
### # Words: T MDA: 9159, T+1 MDA: 8764
### LAB Words:
- kyowa, Count in T: 0, Count in T+1: 24
- kirin, Count in T: 0, Count in T+1: 24
### Explanation:
It is difficult to tell. The agreement was standing since 2009 however Kyowa Kirin is almost never mentioned in 2021 10-K and mentioned over 100 times in 2022. Saying noise but could be LAB
"In March 2021, the Company’s performance obligation period under the Kyowa Kirin Agreement was extended to June 2022, which decreased quarterly revenue recognition by approximately $0.4 million prospectively."
https://www.sec.gov/ix?doc=/Archives/edgar/data/0001358762/000156459022007338/reta-10k_20211231.htm
### Verdict: Noise
### Input:
Using only information through 2021-03-01, predict the main growth drivers for REATA PHARMACEUTICALS INC in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0088 (2/227)
Based on information available up to 2021-03-01, the main growth drivers for Reata Pharmaceuticals Inc. in 2021 are expected to be:

1. **Bardoxolone methyl (bardoxolone)**: Reata's lead product candidate for the treatment of chronic kidney disease (CKD) caused by Alport syndrome, a rare genetic disorder. Positive Phase 3 trial results and potential FDA approval were expected to drive growth.
2. **Omaveloxolone**: Another key product candidate for the treatment of Friedreich's ataxia, a rare genetic disorder. Positive Phase 2 trial results and potential progression to Phase 3 trials were expected to contribute to growth.
3. **Expanding pipeline**: Reata's research and development efforts were focused on expanding its pipeline of product candidates, including potential treatments for other rare diseases. Progress in these areas was expected to drive growth.
4. **Strategic partnerships**: Reata had partnerships with other pharmaceutical companies, such as ```Kyowa``` ```Kirin```, to develop and commercialize its product candidates. These partnerships were expected to provide additional revenue streams and support growth.
5. **Increasing recognition of Alport syndrome and Friedreich's ataxia**: Growing awareness of these rare diseases and the need for effective treatments was expected to drive demand for Reata's product candidates, contributing to growth.

These growth drivers were expected to contribute to Reata's revenue growth, expansion of its pipeline, and increased recognition as a leader in the development of treatments for rare diseases.

## 0001564590-21-009883 — ChemoCentryx, Inc. (2021)
### # Words: T MDA: 5281, T+1 MDA: 5931
### LAB Words:
- tavneos, Count in T: 0, Count in T+1: 44
### Explanation:
FDA Approved it (and first use of name) in October 2021
https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-add-drug-adults-rare-form-blood-vessel-inflammation
### Verdict: Strong LAB
### Input:
Using only information through 2021-03-01, predict the main growth drivers for ChemoCentryx, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0243 (9/370)
Based on publicly available information through 2021-03-01, here are some potential growth drivers for ChemoCentryx, Inc. (CCXI) in 2021:

1. **```Tavneos``` (avacopan) approval and launch**: ChemoCentryx's lead product, ```Tavneos``` (avacopan), is a first-in-class oral inhibitor of the complement component 5 (C5) receptor, which is involved in the pathogenesis of various inflammatory and autoimmune diseases. The FDA approved ```Tavneos``` in February 2021 for the treatment of ANCA-associated vasculitis (AAV), a rare autoimmune disorder. A successful launch of ```Tavneos``` in 2021 could drive growth for the company.
2. **Commercialization of ```Tavneos```**: As ```Tavneos``` gains traction in the market, ChemoCentryx's commercialization efforts will be a key growth driver. The company will need to build a sales team, establish relationships with healthcare providers, and educate the market about the benefits of ```Tavneos```.
3. **Expansion into new indications**: ChemoCentryx is exploring ```Tavneos``` in other indications, such as atopic dermatitis, lupus nephritis, and COVID-19. Positive results from ongoing clinical trials in these areas could lead to additional approvals and further growth.
4. **Partnerships and collaborations**: ChemoCentryx may form partnerships with other companies to expand its reach, improve its commercial capabilities, or access new markets. Such collaborations could provide additional growth opportunities for the company.
5. **Increased focus on rare diseases**: ChemoCentryx has a strong pipeline of rare disease programs, including CCX140, CCX140-B, and CCX140-A. Positive clinical data from these programs could lead to new product approvals and growth for the company.
6. **Expanded research and development**: ChemoCentryx's research and development efforts are focused on identifying new targets and developing new treatments for various diseases. Successful discovery and development of new products could drive growth and increase the company's market value.
7. **Increased visibility and awareness**: As ```Tavneos``` gains approval and launches, ChemoCentryx is likely to receive more attention from investors, analysts, and the media, which could lead to increased visibility and awareness of the company's products and pipeline.

These factors could contribute to ChemoCentryx's growth in 2021, but it's essential to note that the company's actual performance may differ from these predictions.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0036 (1/280)
Based on information available up to 2021-03-01, the main growth drivers for ChemoCentryx, Inc. in 2021 are expected to be:

1. **Avacopan (CCX168)**: ChemoCentryx's lead product candidate, Avacopan, is a C5a receptor inhibitor for the treatment of ANCA-associated vasculitis (AAV) and other autoimmune diseases. Positive results from the Phase III ADVOCATE trial in 2020 demonstrated the efficacy and safety of Avacopan in AAV patients. The company is expected to file a New Drug Application (NDA) with the FDA in 2021, which could lead to regulatory approval and commercialization.

2. **```Tavneos``` (Avacopan) for other indications**: ChemoCentryx is also exploring the potential of Avacopan in other autoimmune diseases, such as hidradenitis suppurativa (HS) and lupus nephritis. Positive results from ongoing clinical trials in these indications could expand the market potential of Avacopan.

3. **CCX559**: ChemoCentryx's CCX559 is a CCR2 receptor inhibitor being developed for the treatment of diabetic nephropathy. The company has reported positive results from a Phase II trial, and further development of CCX559 could provide an additional growth driver.

4. **Partnerships and collaborations**: ChemoCentryx has established partnerships with major pharmaceutical companies, such as Vifor Pharma and Fresenius Medical Care, to develop and commercialize its products. These partnerships could provide significant revenue streams and help drive growth in 2021.

5. **Regulatory milestones**: ChemoCentryx is expected to achieve several regulatory milestones in 2021, including the potential approval of Avacopan in the United States and Europe. These milestones could trigger significant payments from partners and increase the company's revenue.

Overall, ChemoCentryx's growth in 2021 is expected to be driven by the advancement of its lead product candidate, Avacopan, as well as the development of other pipeline assets and partnerships.

## 0001564590-21-009887 — ORASURE TECHNOLOGIES INC (2021)
### # Words: T MDA: 6409, T+1 MDA: 6280
### LAB Words:
- inteliswab, Count in T: 0, Count in T+1: 13
### Explanation:
Google results show earlier in 2021 but the links are broken. Regardless, it likely did not have
authorization until at least June 2021 if not later. 
https://orasure.gcs-web.com/news-releases/news-release-details/us-fda-authorizes-inteliswabtm-covid-19-rapid-tests-otc-single
### Verdict: Strong LAB
### Input:
Using only information through 2021-03-01, predict the main growth drivers for ORASURE TECHNOLOGIES INC in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0043 (1/234)
Based on information available up to 2021-03-01, I predict the main growth drivers for OraSure Technologies, Inc. in 2021 to be:

1. **COVID-19 Testing**: As a leading provider of point-of-care diagnostic tests and specimen collection devices, OraSure is likely to benefit from the ongoing demand for COVID-19 testing. The company's ```InteliSwab``` COVID-19 Rapid Test, which received FDA Emergency Use Authorization (EUA) in 2020, is expected to contribute significantly to revenue growth.

2. **Infectious Disease Testing**: OraSure's portfolio of infectious disease tests, including those for HIV, HCV, and influenza, will likely continue to drive growth as healthcare providers and governments prioritize disease surveillance and prevention.

3. **Molecular Diagnostics**: The company's molecular diagnostics business, which includes its DNA Genotek subsidiary, is expected to grow as the demand for molecular testing increases, particularly in the areas of infectious disease and genetic testing.

4. **International Expansion**: OraSure has been expanding its global presence, and this trend is likely to continue in 2021. The company's international sales are expected to grow as it enters new markets and increases its distribution channels.

5. **Government Contracts and Funding**: As a provider of diagnostic tests and specimen collection devices, OraSure may benefit from government contracts and funding initiatives aimed at supporting public health responses to infectious diseases, including COVID-19.

These growth drivers are based on the company's historical performance, industry trends, and market demand up to 2021-03-01.

## 0001564590-21-012607 — Syndax Pharmaceuticals Inc (2021)
### # Words: T MDA: 7742, T+1 MDA: 7356
### LAB Words:
- incyte, Count in T: 0, Count in T+1: 15
### Explanation:
The parternship with Incyte was announced on September 27, 2021
https://ir.syndax.com/node/10466/pdf?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2021-03-12, predict the main growth drivers for Syndax Pharmaceuticals Inc in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0081 (2/248)
Based on information available up to 2021-03-12, the main growth drivers for Syndax Pharmaceuticals Inc in 2021 are expected to be:

1. **Progress of SNDX-5613**: The company's lead candidate, SNDX-5613, a highly selective, oral Menin inhibitor, is expected to drive growth. In 2020, Syndax announced positive data from the Phase 1 trial of SNDX-5613, demonstrating its potential in treating acute leukemias. Further progress in clinical trials and potential regulatory approvals are expected to drive growth.

2. **Advancements in SNDX-6352**: Another key candidate, SNDX-6352, a monoclonal antibody targeting CSF1R, is being evaluated in various solid tumors. Positive data from ongoing trials could lead to increased investor interest and growth.

3. **Expansion of the pipeline**: Syndax has a diverse pipeline of oncology candidates. The company's efforts to advance these candidates through clinical trials and potentially into commercialization are expected to drive growth.

4. **Strategic partnerships and collaborations**: Syndax has a history of forming strategic partnerships, including a collaboration with ```Incyte``` Corporation to evaluate SNDX-6352 in combination with ```Incyte```'s Jakafi. Further partnerships and collaborations could provide growth opportunities.

5. **Increased focus on precision medicine**: Syndax's focus on precision medicine, including the development of targeted therapies like SNDX-5613, is expected to drive growth as the company leverages advances in genetic analysis and biomarker identification to develop more effective treatments.

These factors are expected to contribute to Syndax Pharmaceuticals' growth in 2021, driven by the advancement of its pipeline candidates, strategic partnerships, and the increasing focus on precision medicine.

## 0001564590-21-014169 — ALX ONCOLOGY HOLDINGS INC (2021)
### # Words: T MDA: 7820, T+1 MDA: 6724
### LAB Words:
- evorpacept, Count in T: 0, Count in T+1: 18
### Explanation:
Evorpacept was likely first used in November 2021
https://pubmed.ncbi.nlm.nih.gov/34793719/
### Verdict: Weak LAB (take)
### Input:
Using only information through 2021-03-18, predict the main growth drivers for ALX ONCOLOGY HOLDINGS INC in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0077 (2/261)
Based on information available up to 2021-03-18, the main growth drivers for ALX Oncology Holdings Inc. in 2021 are expected to be:

1. **Advancements in CD47-targeting cancer therapies**: ALX Oncology's lead candidate, ```evorpacept``` (also known as ALX148), is a CD47-targeting antibody that has shown promising results in clinical trials. The company is expected to continue advancing ```evorpacept``` through clinical development, which could drive growth and attract investor attention.

2. **Expansion of clinical trials and pipeline development**: ALX Oncology has a pipeline of cancer therapies in various stages of development. The company is expected to initiate new clinical trials and expand existing ones, which could lead to new data readouts and potential partnerships or collaborations.

3. **Growing interest in immuno-oncology**: The immuno-oncology space has seen significant growth in recent years, driven by the success of checkpoint inhibitors and other immunotherapies. ALX Oncology's focus on CD47-targeting therapies positions the company to benefit from this trend.

4. **Strategic partnerships and collaborations**: ALX Oncology has established partnerships with major pharmaceutical companies, including Merck and Pfizer. These partnerships could provide the company with access to additional resources, expertise, and funding, driving growth and accelerating the development of its pipeline candidates.

5. **Increasing recognition of CD47 as a key target in cancer therapy**: CD47 has emerged as a promising target in cancer therapy, with several companies developing CD47-targeting therapies. ALX Oncology's expertise in this area could position the company for growth as the field continues to evolve.

These growth drivers are based on publicly available information and should not be considered as investment advice.

## 0001564590-21-015146 — iTeos Therapeutics, Inc. (2021)
### # Words: T MDA: 8213, T+1 MDA: 8442
### LAB Words:
- gsk, Count in T: 0, Count in T+1: 40
### Explanation:
Announced on June 14, 2021
https://www.gsk.com/en-gb/media/press-releases/gsk-and-iteos-therapeutics-announce-development/
### Verdict: Strong LAB
### Input:
Using only information through 2021-03-24, predict the main growth drivers for iTeos Therapeutics, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0028 (1/355)
Based on publicly available information through 2021-03-24, here are some potential growth drivers for iTeos Therapeutics, Inc. in 2021:

1. **PD-1/CTLA-4 combination therapy**: iTeos Therapeutics is developing a PD-1/CTLA-4 combination therapy, which has shown promising results in clinical trials. The company's lead product candidate, EOS2006, is a PD-1/CTLA-4 bispecific antibody that has demonstrated significant anti-tumor activity in patients with advanced solid tumors. The success of this therapy could drive growth for the company in 2021.
2. **Expansion of clinical trials**: iTeos Therapeutics has been expanding its clinical trials for EOS2006, including a Phase 2 trial in patients with non-small cell lung cancer (NSCLC) and a Phase 1b trial in patients with melanoma. The expansion of these trials could lead to increased visibility and interest in the company's product candidate, driving growth in 2021.
3. **Partnerships and collaborations**: iTeos Therapeutics has partnered with several pharmaceutical companies, including ```GSK``` and Servier, to develop and commercialize its product candidates. These partnerships could provide the company with additional resources and expertise, driving growth and increasing its visibility in the market.
4. **Immuno-oncology market growth**: The immuno-oncology market is expected to continue growing in 2021, driven by the increasing adoption of checkpoint inhibitors and other immunotherapies. As a player in this space, iTeos Therapeutics is well-positioned to benefit from this growth trend.
5. **Regulatory milestones**: iTeos Therapeutics has several regulatory milestones approaching in 2021, including the potential for FDA approval of EOS2006. The achievement of these milestones could lead to increased visibility and growth for the company.
6. **Strong cash position**: iTeos Therapeutics has a strong cash position, with $434.4 million in cash and cash equivalents as of December 31, 2020. This provides the company with the financial resources to continue to advance its product candidates and drive growth in 2021.

These factors could contribute to the growth of iTeos Therapeutics in 2021, but it's essential to note that the company's actual performance may differ from these predictions.

**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0028 (1/362)
Based on publicly available information through 2021-03-24, here are some potential main growth drivers for iTeos Therapeutics, Inc. in 2021:

1. **Tecemotide's Phase III trial results**: iTeos Therapeutics is developing tecemotide, an anti-CD73 monoclonal antibody, for the treatment of non-small cell lung cancer (NSCLC) and pancreatic cancer. Positive Phase III trial results in 2021 could lead to a potential FDA approval and significant growth for the company.
2. **Expansion of the company's pipeline**: iTeos Therapeutics has a pipeline of several clinical-stage programs, including its lead candidate, infigratinib (formerly known as GDC-0449), a fibroblast growth factor receptor (FGFR) inhibitor for the treatment of various cancers. The company's ability to advance its pipeline and initiate new clinical trials could drive growth.
3. **Partnerships and collaborations**: iTeos Therapeutics has partnered with pharmaceutical companies, such as ```GSK```, to develop and commercialize its products. The company's ability to secure additional partnerships or collaborations could provide access to new funding, expertise, and commercialization opportunities, driving growth.
4. **Immuno-oncology market growth**: The immuno-oncology market is expected to continue growing rapidly in 2021, driven by the increasing use of cancer immunotherapies. As a company focused on developing cancer therapies, iTeos Therapeutics is well-positioned to benefit from this trend.
5. **Increased focus on cancer treatment**: The company's focus on cancer treatment, particularly in areas with high unmet medical need, such as NSCLC and pancreatic cancer, could drive growth as the company's pipeline and partnerships advance.
6. **Cash position and funding**: As of 2021-03-24, iTeos Therapeutics had approximately $230 million in cash and cash equivalents. The company's cash position and access to additional funding could enable it to continue to advance its pipeline and drive growth.
7. **Regulatory updates**: The company's ability to receive regulatory updates, such as FDA feedback on its clinical trials or IND submissions, could provide a catalyst for growth as the company advances its pipeline.

These are some of the potential growth drivers for iTeos Therapeutics in 2021 based on publicly available information.

**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0027 (1/365)
Based on publicly available information as of 2021-03-24, here are some potential main growth drivers for iTeos Therapeutics, Inc. in 2021:

1. **Talimogene laherpapevecle (T-vec)**: iTeos is developing T-vec, an oncolytic immunotherapy for the treatment of metastatic melanoma. Positive Phase III trial results in 2014 and subsequent regulatory submissions may lead to T-vec's approval in 2021, providing a significant revenue stream for the company.
2. **Anti-TIGiT (Anti-TIGIT) program**: iTeos is developing an anti-TIGIT program, which is a promising area of research in cancer immunotherapy. A Phase I trial for the anti-TIGIT program is ongoing, and positive results could lead to further development and potential partnerships, driving growth.
3. **Partnerships and collaborations**: iTeos has partnered with major pharmaceutical companies, such as ```GSK```, Sanofi, and Pfizer, to develop and commercialize its products. These partnerships may lead to additional funding, expertise, and access to new markets, driving growth.
4. **Expansion of clinical trials**: iTeos is expanding its clinical trial portfolio, including the initiation of new Phase II trials for T-vec in other cancer indications, such as breast cancer and lung cancer. Successful trial outcomes could lead to additional approvals and revenue growth.
5. **Immuno-oncology market growth**: The immuno-oncology market is expected to grow significantly in 2021, driven by increasing demand for cancer treatments that target the immune system. As a player in this space, iTeos is well-positioned to benefit from this growth.
6. **Cash position and funding**: As of 2021, iTeos had approximately $230 million in cash and cash equivalents, which should provide sufficient funding to support its operations and development pipeline.
7. **Key opinion leader and thought leader relationships**: iTeos has established relationships with key thought leaders and opinion leaders in the oncology community, which could help drive the adoption of its products and therapies.
8. **T-IGIT and other programs in development**: iTeos has a robust pipeline of other programs, including T-IGIT, which targets the immune checkpoint protein TIGG, and a program targeting the cancer stem cell population. Positive results from these programs could lead to additional growth opportunities.

## 0001564590-22-009681 — Poseida Therapeutics, Inc. (2022)
### # Words: T MDA: 9727, T+1 MDA: 10453
### LAB Words:
- roche, Count in T: 0, Count in T+1: 44
### Explanation:
Parternship announced August 3rd, 2022
https://www.prnewswire.com/news-releases/poseida-therapeutics-announces-strategic-global-collaboration-with-roche-focused-on-allogeneic-car-t-cell-therapies-for-hematologic-malignancies-301598555.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2022-03-10, predict the main growth drivers for Poseida Therapeutics, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0039 (1/255)
Based on information available up to 2022-03-10, the main growth drivers for Poseida Therapeutics, Inc. in 2022 are expected to be:

1. **Advancements in Cell Therapy Pipeline**: Poseida's pipeline of cell therapies, including P-BCMA-101 for multiple myeloma and P-PSMA-101 for prostate cancer, are expected to drive growth. Positive clinical trial results and potential regulatory approvals could lead to increased investor interest and partnerships.

2. **Partnerships and Collaborations**: Poseida has established partnerships with major pharmaceutical companies, such as ```Roche```, to develop and commercialize its cell therapies. Additional partnerships and collaborations are expected to drive growth by providing access to new markets, technologies, and funding.

3. **Expansion of Gene Editing Capabilities**: Poseida's proprietary gene editing technology, known as the piggyBac DNA Modification System, is expected to drive growth by enabling the development of new cell therapies and potentially licensing opportunities.

4. **Increased Focus on Solid Tumors**: Poseida's expansion into solid tumors, such as prostate cancer and other indications, is expected to drive growth by increasing the company's addressable market and potential revenue streams.

5. **Growing Interest in Cell Therapy**: The cell therapy market is expected to continue growing in 2022, driven by increasing interest in innovative treatments for cancer and other diseases. Poseida is well-positioned to benefit from this trend, with its pipeline of cell therapies and proprietary gene editing technology.

These growth drivers are expected to contribute to Poseida's growth in 2022, although the company's actual performance may be influenced by various factors, including regulatory developments, competition, and market conditions.

## 0001628280-19-002369 — AERIE PHARMACEUTICALS INC (2019)
### # Words: T MDA: 10729, T+1 MDA: 10648
### LAB Words:
- rocklatan, Count in T: 0, Count in T+1: 59
### Explanation:
The drug was in development and had its NDA been submitted. 
https://www.drugs.com/history/rocklatan.html?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2019-03-01, predict the main growth drivers for AERIE PHARMACEUTICALS INC in 2019. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0177 (5/282)
Based on information available up to 2019-03-01, the main growth drivers for Aerie Pharmaceuticals Inc. in 2019 are expected to be:

1. **Rhopressa (netarsudil ophthalmic solution) 0.02%**: This is the company's first FDA-approved product, launched in the US in April 2018. Rhopressa is a novel once-daily eye drop for the reduction of intraocular pressure (IOP) in patients with glaucoma or ocular hypertension. Continued commercialization and market penetration of Rhopressa are expected to drive revenue growth in 2019.

2. **```Rocklatan``` (netarsudil and latanoprost ophthalmic solution) 0.02%/0.005%**: This is Aerie's second product, which received FDA approval in March 2019. ```Rocklatan``` is a once-daily eye drop that combines Rhopressa with latanoprost, a widely used prostaglandin analogue, for the reduction of IOP in patients with glaucoma or ocular hypertension. The launch of ```Rocklatan``` is expected to contribute significantly to Aerie's revenue growth in 2019.

3. **Expansion of Sales and Marketing Efforts**: Aerie has been investing in expanding its sales and marketing infrastructure to support the commercialization of Rhopressa and ```Rocklatan```. The company is expected to continue to build its sales force and marketing capabilities to increase product awareness and drive adoption among eye care professionals.

4. **Research and Development Pipeline**: Aerie has a pipeline of products in various stages of development, including AR-1105, a sustained-release implant for the treatment of glaucoma and ocular hypertension. While these products are not expected to contribute to revenue growth in 2019, they represent potential future growth drivers for the company.

Overall, Aerie Pharmaceuticals' growth in 2019 is expected to be driven primarily by the continued commercialization of Rhopressa and the launch of ```Rocklatan```, as well as the expansion of its sales and marketing efforts.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0113 (4/354)
Based on publicly available information through 2019-03-01, here are some potential growth drivers for Aerie Pharmaceuticals, Inc. (AERI) in 2019:

1. **Rhopressa's continued growth**: Aerie's lead product, Rhopressa (netarsudil), a once-daily eye drop for glaucoma, was launched in the US in 2016. In 2018, the company reported strong sales growth for Rhopressa, and it's likely that this trend will continue in 2019, driven by increasing adoption and market share gains.
2. **Commercialization of ```Rocklatan```**: Aerie's second product, ```Rocklatan``` (netarsudil and latanoprost), was approved by the FDA in 2018. In 2019, the company is expected to continue to build commercial momentum for ```Rocklatan```, which has the potential to become a leading treatment for glaucoma.
3. **Expansion of sales force and marketing efforts**: Aerie has been investing in its sales force and marketing efforts to support the commercialization of its products. In 2019, the company may continue to expand its sales team and marketing initiatives to reach more ophthalmologists and optometrists, driving growth in Rhopressa and ```Rocklatan``` sales.
4. **Pipeline development**: Aerie has a pipeline of potential new products, including AR-1105, a dry eye treatment, and AR-15512, a potential treatment for glaucoma. While these products are still in development, they may contribute to the company's growth prospects in the long term.
5. **Increasing competition in the glaucoma market**: The glaucoma market is becoming increasingly competitive, with new entrants and generic competition emerging. Aerie's focus on building a strong sales force and marketing efforts may help the company maintain its market share and drive growth in a competitive environment.
6. **Potential for international expansion**: Aerie has been focused on the US market, but there may be opportunities for international expansion, particularly in Europe and other developed markets. If the company is successful in expanding its reach, it could drive growth in 2019 and beyond.

These are just a few potential growth drivers for Aerie Pharmaceuticals in 2019, based on publicly available information through 2019-03-01.

## 0001628280-21-003336 — Lantheus Holdings, Inc. (2021)
### # Words: T MDA: 10105, T+1 MDA: 10710
### LAB Words:
- pylarify, Count in T: 0, Count in T+1: 51
### Explanation:
FDA approved it in May 2021 (after the date in the input)
https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-second-psma-targeted-pet-imaging-drug-men-prostate-cancer
### Verdict: Strong LAB
### Input:
Using only information through 2021-02-25, predict the main growth drivers for Lantheus Holdings, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0083 (2/241)
Based on information available up to 2021-02-25, the main growth drivers for Lantheus Holdings, Inc. in 2021 are expected to be:

1. **```PYLARIFY``` (piflufolastat F 18)**: Lantheus' prostate-specific membrane antigen (PSMA)-targeted positron emission tomography (PET) imaging agent, which received FDA approval in May 2021, but was predicted to be approved in 2021 prior to 2021-02-25. ```PYLARIFY``` is expected to drive growth in the company's oncology portfolio.

2. **DEFINITY (perflutren lipid microsphere)**: Lantheus' ultrasound contrast agent, which has been a key revenue driver for the company. Continued adoption and increased use of DEFINTY in ultrasound procedures are expected to contribute to growth.

3. **Strategic Partnerships and Collaborations**: Lantheus has a history of forming partnerships to expand its product offerings and reach new markets. The company may continue to pursue collaborations and partnerships to drive growth and increase its presence in the market.

4. **International Expansion**: Lantheus has been working to expand its presence in international markets, particularly in Europe and Asia. The company may continue to invest in these efforts to drive growth and increase its global footprint.

5. **Diversification of Product Portfolio**: Lantheus has been working to diversify its product portfolio through investments in research and development. The company may continue to invest in new product development and acquisitions to drive growth and reduce its dependence on a single product.

These growth drivers are based on the company's historical performance, industry trends, and market expectations as of 2021-02-25.

## 0001640455-20-000034 — Jounce Therapeutics, Inc. (2020)
### # Words: T MDA: 5752, T+1 MDA: 6144
### LAB Words:
- gilead, Count in T: 0, Count in T+1: 24
### Explanation:
Gilead and Jounce announced partnership on September 1st, 2020
https://www.gilead.com/news/news-details/2020/gilead-sciences-and-jounce-therapeutics-announce-exclusive-license-agreement-for-novel-immunotherapy-program?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-27, predict the main growth drivers for Jounce Therapeutics, Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0030 (1/335)
Based on publicly available information through 2020-02-27, here are some potential growth drivers for Jounce Therapeutics, Inc. (NASDAQ: JNCE) in 2020:

1. **Vantictumab (JTX-4014) clinical trials**: Jounce Therapeutics is developing vantictumab, a monoclonal antibody targeting TIGIT, a novel immune checkpoint protein. Positive results from ongoing clinical trials, such as the Phase 1/2 trial in patients with advanced solid tumors, could lead to increased investor interest and potential partnerships.
2. **Partnerships and collaborations**: Jounce Therapeutics has partnered with several pharmaceutical companies, including Bristol-Myers Squibb (BMY) and ```Gilead``` Sciences (GILD), to develop and commercialize its pipeline candidates. These partnerships could lead to increased funding, expertise, and access to new markets.
3. **Immuno-oncology market growth**: The immuno-oncology market is expected to continue growing rapidly, driven by the increasing adoption of checkpoint inhibitors and the development of new targets like TIGIT. Jounce Therapeutics' focus on this area could position the company for growth as the market expands.
4. **Pipeline expansion**: Jounce Therapeutics has a pipeline of multiple candidates, including JTX-1317, a TIGIT-targeting antibody-drug conjugate, and JTX-4013, a TIGIT-targeting bispecific antibody. Positive data from these programs could lead to additional partnerships, licensing deals, or even regulatory approvals.
5. **Increased visibility and awareness**: As Jounce Therapeutics continues to present data at conferences and publish results in scientific journals, the company may gain increased visibility and recognition within the industry, potentially attracting new investors and partners.
6. **Cash runway extension**: Jounce Therapeutics has a strong cash position, with approximately $230 million in cash and cash equivalents as of Q3 2019. This cash runway could support the company's operations and allow it to continue advancing its pipeline candidates without needing to raise additional capital in the near term.

These factors could contribute to Jounce Therapeutics' growth in 2020, but it's essential to note that the company's actual performance may differ from these predictions.

## 0001654151-20-000003 — Deciphera Pharmaceuticals, Inc. (2020)
### # Words: T MDA: 9417, T+1 MDA: 10597
### LAB Words:
- qinlock, Count in T: 0, Count in T+1: 83
- study, Count in T: 0, Count in T+1: 33
### Explanation:
The drug was under priority review at the time and was expected to be approved in 2020.
https://www.drugs.com/history/qinlock.html?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2020-03-09, predict the main growth drivers for Deciphera Pharmaceuticals, Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 1.0
**Proportion Bad:** 0.0265 (8/302)
Based on publicly available information through 2020-03-09, I'll predict the main growth drivers for Deciphera Pharmaceuticals, Inc. in 2020:

1. **```Qinlock``` (ripasciributyl sulfate) commercialization and sales growth**: Deciphera's lead product, ```Qinlock``` (ripasciributyl sulfate), is an oral, potent, and selective inhibitor of the KIT and PDGFRA kinases. Deciphera is planning to launch ```Qinlock``` in the US market in 2020 for the treatment of patients with Gastrointestinal Stromal Tumors (GIST). Strong sales growth is expected as ```Qinlock``` gains traction in the GIST market.
2. **Expansion of clinical trials and pipeline progress**: Deciphera has a pipeline of clinical-stage programs, including DCC-3014 (a KIT inhibitor for GIST and other cancers) and DCC-3016 (a KIT and PDGFR inhibitor for GIST and other cancers). Positive clinical trial results and regulatory approvals for these programs could drive growth through 2020.
3. **Partnerships and collaborations**: Deciphera has partnered with pharmaceutical companies, such as Eli Lilly and Company, to develop and commercialize its products. Additional partnerships and collaborations could drive growth through 2020 by providing access to new markets, technologies, and expertise.
4. **Increased awareness and adoption of ```Qinlock``` among oncologists and patients**: As Deciphera launches ```Qinlock``` in the US market, the company will focus on educating oncologists and patients about the benefits of ```Qinlock```, which could lead to increased adoption and growth in sales.
5. **Growing demand for targeted cancer therapies**: The global market for cancer therapies is shifting towards targeted therapies, which are generally more effective and have fewer side effects than traditional chemotherapy. Deciphera's kinase inhibitors, such as ```Qinlock```, are part of this trend, and growing demand for targeted cancer therapies could drive growth for Deciphera in 2020.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0144 (3/208)
Based on information available up to 2020-03-09, the main growth drivers for Deciphera Pharmaceuticals, Inc. in 2020 are expected to be:

1. **```Qinlock``` (Ripretinib)**: Deciphera's lead product candidate, ```Qinlock```, a broad-spectrum KIT and PDGFRα inhibitor, was granted Priority Review by the FDA for the treatment of fourth-line gastrointestinal stromal tumor (GIST). Approval and commercialization of ```Qinlock``` were expected to drive significant revenue growth in 2020.

2. **Pipeline Advancements**: Deciphera's pipeline includes several promising candidates, such as DCC-3014 (a CSF1R inhibitor) and rebastinib (a TIE2 inhibitor). Progress in clinical trials and potential data readouts for these candidates were expected to contribute to the company's growth in 2020.

3. **Strategic Partnerships**: Deciphera had established partnerships with companies like Zai Lab and Ipsen to develop and commercialize its products in various regions. These partnerships were expected to provide additional revenue streams and support the company's growth in 2020.

4. **Increased Research and Development (R&D) Investments**: Deciphera had been investing heavily in R&D to advance its pipeline and expand its product portfolio. Continued investments in R&D were expected to drive innovation and growth in 2020.

These growth drivers were expected to contribute to Deciphera's expansion and revenue growth in 2020, based on information available up to 2020-03-09.

## 0001683168-21-002764 — Avid Bioservices, Inc. (2021)
### # Words: T MDA: 5265, T+1 MDA: 4615
### LAB Words:
- gene, Count in T: 0, Count in T+1: 10
- therapy, Count in T: 0, Count in T+1: 10
### Explanation:
Biospace announced their entry into gene therapy in October 2021.
https://www.biospace.com/avid-bioservices-announces-expansion-into-viral-vector-development-and-manufacturing-services-for-cell-and-gene-therapy?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2021-06-29, predict the main growth drivers for Avid Bioservices, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0174 (8/459)
Based on publicly available information through 2021-06-29, here are some potential main growth drivers for Avid Bioservices, Inc. in 2022:

1. **Increasing demand for contract development and manufacturing services (CDMO)**: Avid Bioservices is a leading provider of CDMO services, which are critical for the development and manufacturing of biopharmaceutical products. As the biopharmaceutical industry continues to grow, driven by an aging population, increasing healthcare spending, and the need for innovative treatments, Avid Bioservices is well-positioned to benefit from this trend.
2. **Growing demand for cell and ```gene``` ```therapy``` services**: Avid Bioservices has a strong presence in cell and ```gene``` ```therapy``` development and manufacturing, which is a rapidly growing area in the biopharmaceutical industry. The company's expertise in this area, combined with the increasing investment in cell and ```gene``` ```therapy``` research and development, positions Avid Bioservices for growth in this area.
3. **Expansion of its San Diego facility**: In 2020, Avid Bioservices announced the expansion of its San Diego facility, which will increase its capacity for cell and ```gene``` ```therapy``` development and manufacturing. This expansion is expected to be completed in 2022, which will enable the company to take on more projects and increase its revenue.
4. **Increasing demand for ADC (Antibody-Drug Conjugate) development and manufacturing services**: Avid Bioservices has a strong presence in ADC development and manufacturing, which is a rapidly growing area in the biopharmaceutical industry. The company's expertise in this area, combined with the increasing investment in ADC research and development, positions Avid Bioservices for growth in this area.
5. **Strategic partnerships and collaborations**: Avid Bioservices has a history of forming strategic partnerships and collaborations with biopharmaceutical companies, contract research organizations (CROs), and other service providers. These partnerships can provide the company with new business opportunities, access to new technologies, and increased visibility in the market.
6. **Increasing demand for biopharmaceutical manufacturing services in the US**: Avid Bioservices has a strong presence in the US, which is a major market for biopharmaceutical manufacturing services. The company's US-based facilities are well-positioned to benefit from the increasing demand for biopharmaceutical manufacturing services in the country.
7. **Growing demand for quality and regulatory services**: Avid Bioservices offers a range of quality and regulatory services, including quality control, quality assurance, and regulatory consulting. As the biopharmaceutical industry becomes increasingly complex, companies are seeking more expertise in these areas, which positions Avid Bioservices for growth.

These are some of the potential growth drivers for Avid Bioservices, Inc. in 2022. The company's ability to execute on these opportunities will depend on various factors, including its operational performance, strategic partnerships, and market conditions.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0109 (4/368)
Based on the publicly available information up to 2021-06-29, here are some potential growth drivers for Avid Bioservices, Inc. in 2022:

1. **Increasing demand for contract research and development (CR&D) services**: Avid Bioservices is a leading provider of CR&D services, including process development, analytical and formulation development, and commercial manufacturing. As the biopharmaceutical industry continues to grow, the demand for CR&D services is expected to increase, driving growth for Avid Bioservices.
2. **Expansion of its cGMP manufacturing capabilities**: Avid Bioservices has been investing in its cGMP manufacturing capabilities, including the expansion of its facilities and the addition of new equipment. This expansion is expected to increase its capacity to handle larger-scale manufacturing projects, potentially leading to increased revenue growth.
3. **Growing demand for biologics and biosimilars**: The biologics and biosimilars market is expected to continue growing, driven by the increasing demand for complex biopharmaceuticals. Avid Bioservices' expertise in CR&D and manufacturing services positions it well to capitalize on this trend.
4. **Partnerships and collaborations**: Avid Bioservices has a history of partnering with pharmaceutical and biotechnology companies to provide CR&D and manufacturing services. These partnerships can lead to new business opportunities and revenue growth.
5. **Increased focus on cell and ```gene``` ```therapy``` development**: Cell and ```gene``` ```therapy``` is a rapidly growing area of research and development, and Avid Bioservices has the capabilities to support the development of these complex therapies. As more companies enter this space, Avid Bioservices may see increased demand for its services.
6. **Expansion of its services to support the development of mRNA-based therapies**: With the emergence of mRNA-based therapies, Avid Bioservices may see an increase in demand for its services, particularly in the areas of process development and manufacturing.
7. **Investment in digital transformation and technology**: Avid Bioservices has been investing in digital transformation and technology to improve its operational efficiency and customer experience. This investment may lead to increased productivity and competitiveness, driving growth and revenue expansion.

These are some potential growth drivers for Avid Bioservices, Inc. in 2022, based on publicly available information up to 2021-06-29.

**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0035 (1/288)
Based on information available up to 2021-06-29, the main growth drivers for Avid Bioservices, Inc. in 2022 are predicted to be:

1. **Increasing Demand for Biologics and Cell Therapies**: The biologics and cell ```therapy``` markets are expected to continue growing, driven by an increasing number of approved products and a strong pipeline of candidates in development. As a contract development and manufacturing organization (CDMO) specializing in biologics and cell therapies, Avid Bioservices is well-positioned to benefit from this trend.

2. **Expansion of Manufacturing Capacity**: Avid Bioservices has been investing in the expansion of its manufacturing capacity, including the addition of new suites and equipment at its facilities. This increased capacity is expected to enable the company to take on more clients and projects, driving revenue growth.

3. **Growing Customer Base**: Avid Bioservices has been actively expanding its customer base, including partnerships with new clients and the extension of existing relationships. The company's expertise in biologics and cell therapies, combined with its expanded manufacturing capacity, is expected to attract new customers and drive growth.

4. **Diversification of Services**: Avid Bioservices has been diversifying its services to include additional offerings such as process development, analytical testing, and regulatory support. This expanded service portfolio is expected to attract new customers and increase revenue from existing clients.

5. **Strategic Partnerships and Collaborations**: Avid Bioservices has been actively pursuing strategic partnerships and collaborations with other companies and research institutions. These partnerships are expected to drive growth by providing access to new technologies, expertise, and customers.

Overall, Avid Bioservices' growth in 2022 is expected to be driven by a combination of increasing demand for biologics and cell therapies, expanded manufacturing capacity, a growing customer base, diversification of services, and strategic partnerships and collaborations.

## 0001711279-22-000004 — Krystal Biotech, Inc. (2022)
### # Words: T MDA: 6464, T+1 MDA: 7078
### LAB Words:
- b-vec, Count in T: 0, Count in T+1: 20
### Explanation:
B-Vec term was likely first used in April 2022
https://www.globenewswire.com/news-release/2022/04/11/2419890/0/en/Krystal-Biotech-Announces-Home-Dosing-in-B-VEC-Open-Label-Extension-Study.html?utm_source=chatgpt.com
### Verdict: Weak LAB (take)
### Input:
Using only information through 2022-02-28, predict the main growth drivers for Krystal Biotech, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0047 (1/215)
Based on information available up to 2022-02-28, the main growth drivers for Krystal Biotech, Inc. in 2022 are expected to be:

1. **Advancements in Gene Therapy Pipeline**: Krystal Biotech's lead product candidate, Vyjuvek (```B-VEC```), is a gene therapy for the treatment of dystrophic epidermolysis bullosa (DEB). Positive results from clinical trials and potential FDA approval could drive growth.

2. **Expansion of Pipeline**: Krystal Biotech has a robust pipeline of gene therapies targeting various skin diseases. Progress in these programs, including KB105 for autosomal recessive congenital ichthyosis (ARCI) and KB104 for Netherton syndrome, could contribute to growth.

3. **Strategic Partnerships and Collaborations**: Krystal Biotech may form partnerships or collaborations to accelerate the development and commercialization of its gene therapies, which could provide access to new markets, technologies, and funding.

4. **Increasing Awareness and Diagnosis of Rare Skin Diseases**: Growing awareness and diagnosis of rare skin diseases, such as DEB and ARCI, could lead to increased demand for Krystal Biotech's gene therapies.

5. **Regulatory Support for Gene Therapies**: The FDA's increasing support for gene therapies, including the introduction of new guidelines and expedited review pathways, could facilitate the approval and commercialization of Krystal Biotech's products.

These growth drivers are based on the company's pipeline, industry trends, and regulatory environment as of 2022-02-28.

## 0001711279-23-000008 — Krystal Biotech, Inc. (2023)
### # Words: T MDA: 7078, T+1 MDA: 9126
### LAB Words:
- vyjuvek, Count in T: 0, Count in T+1: 38
### Explanation:
FDA approved the drug on May 19, 2023
https://www.biospace.com/krystal-biotech-receives-fda-approval-for-the-first-ever-redosable-gene-therapy-vyjuvek-beremagene-geperpavec-svdt-for-the-treatment-of-dystrophic-epidermolysis-bullosa
### Verdict: Weak LAB (take)
### Input:
Using only information through 2023-02-27, predict the main growth drivers for Krystal Biotech, Inc. in 2023. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0103 (3/291)
Based on information available up to 2023-02-27, the main growth drivers for Krystal Biotech, Inc. in 2023 are expected to be:

1. **Advancements in Gene Therapy Pipeline**: Krystal Biotech's lead product candidate, ```Vyjuvek``` (beremagene geperpavec), is a topical gene therapy for the treatment of dystrophic epidermolysis bullosa (DEB). The company is expected to continue making progress in its clinical trials, which could lead to regulatory approvals and commercialization.

2. **Expansion of Pipeline into New Indications**: Krystal Biotech is exploring the potential of its gene therapy platform to treat other rare skin diseases. The company's pipeline expansion is expected to drive growth by increasing its addressable market and providing new opportunities for revenue generation.

3. **Strategic Partnerships and Collaborations**: Krystal Biotech may form partnerships with other biotechnology or pharmaceutical companies to accelerate the development and commercialization of its gene therapies. These partnerships could provide access to new markets, technologies, and expertise, driving growth and increasing the company's competitiveness.

4. **Regulatory Approvals and Commercialization**: Krystal Biotech is expected to receive regulatory approvals for its lead product candidate, ```Vyjuvek```, in 2023. The commercialization of ```Vyjuvek``` is expected to drive revenue growth and increase the company's visibility in the market.

5. **Increasing Awareness and Diagnosis of Rare Skin Diseases**: Krystal Biotech's efforts to raise awareness about rare skin diseases, such as DEB, are expected to lead to increased diagnosis and treatment rates. This, in turn, is expected to drive demand for the company's gene therapies and contribute to its growth.

These growth drivers are expected to contribute to Krystal Biotech's growth in 2023, but the actual outcome may be influenced by various factors, including regulatory decisions, market conditions, and the company's ability to execute its business strategy.

## 0001714899-20-000026 — Denali Therapeutics Inc. (2020)
### # Words: T MDA: 10915, T+1 MDA: 13000
### LAB Words:
- biogen, Count in T: 0, Count in T+1: 67
### Explanation:
Biogen agreement was October 2020. 
https://www.globenewswire.com/news-release/2020/10/07/2104936/0/en/Denali-Therapeutics-Announces-Closing-of-Collaboration-and-Share-Purchase-Agreements-with-Biogen.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2020-02-27, predict the main growth drivers for Denali Therapeutics Inc. in 2020. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 1b-98b Alpha: 0.5
**Proportion Bad:** 0.0028 (1/362)
Based on publicly available information through 2020-02-27, here are some potential main growth drivers for Denali Therapeutics Inc. in 2020:

1. **Progress in Parkinson's Disease (PD) and Lewy Body Dementia (LBD) programs**: Denali Therapeutics has been actively developing its proprietary platform of monoclonal antibodies targeting tau and alpha-synuclein, which are implicated in the pathogenesis of PD and LBD. Positive results from ongoing clinical trials, such as the Phase 2 trial of DNL201 in PD, could lead to increased interest and investment in the company.
2. **Tau and alpha-synuclein programs' potential for first-in-class treatments**: Denali's proprietary platform has the potential to offer first-in-class treatments for tau and alpha-synuclein-related diseases, which could lead to significant growth in revenue and market share.
3. **Partnerships and collaborations**: Denali has partnered with leading research institutions and pharmaceutical companies, such as the Michael J. Fox Foundation and ```Biogen```, to advance its pipeline. Successful collaborations could lead to increased funding, expertise, and access to new markets.
4. **Expansion of clinical trials**: Denali has been expanding its clinical trial pipeline, including the initiation of new trials for its tau and alpha-synuclein programs. Positive trial results could lead to accelerated development and increased growth.
5. **Growing awareness of tau and alpha-synuclein-related diseases**: As the scientific community becomes increasingly aware of the importance of tau and alpha-synuclein in neurodegenerative diseases, Denali's focus on these targets could lead to increased interest and investment in the company.
6. **Denali's proprietary platform and technology**: The company's proprietary platform and technology have the potential to enable the development of multiple treatments for various neurodegenerative diseases, providing a strong foundation for long-term growth.
7. **Increased focus on neurodegenerative diseases**: The growing awareness of neurodegenerative diseases, such as Alzheimer's, Parkinson's, and LBD, could lead to increased investment and research in this area, benefiting Denali's pipeline and growth prospects.

Please note that these predictions are based on publicly available information and may not reflect the company's actual growth drivers or performance in 2020.

**LLM Config:** 8B Alpha: 0
**Proportion Bad:** 0.0025 (1/394)
Based on publicly available information through 2020-02-27, here are some potential growth drivers for Denali Therapeutics Inc. in 2020:

1. **Progress in Alzheimer's Disease (AD) Program**: Denali Therapeutics is developing a pipeline of small molecule and antibody-based therapeutics for neurodegenerative diseases, including Alzheimer's disease. The company's lead program, DNL201, is a monoclonal antibody targeting tau protein, which is a key driver of AD pathology. Positive results from ongoing clinical trials, such as the Phase 1b/2a trial, could lead to increased investor interest and partnerships.
2. **Expansion of Tau Program**: Denali's tau program is expanding to include additional targets and modalities, such as small molecules and gene therapies. This diversification could lead to increased revenue potential and partnerships with pharmaceutical companies.
3. **Partnerships and Collaborations**: Denali has established partnerships with leading research institutions and pharmaceutical companies, such as the University of California, San Francisco (UCSF) and ```Biogen```. These collaborations could lead to access to new technologies, expertise, and funding, driving growth and innovation.
4. **Advancements in Gene Therapy**: Denali is developing a gene therapy program for neurodegenerative diseases, including AD. Positive results from preclinical studies and potential partnerships with gene therapy companies could drive growth and increase the company's valuation.
5. **Increased Focus on Neurodegenerative Diseases**: Denali's focus on neurodegenerative diseases, such as AD, Parkinson's disease, and amyotrophic lateral sclerosis (ALS), positions the company to benefit from the growing interest in these areas. As the company advances its pipeline, it may attract more investors and partners.
6. **Strong Financial Position**: Denali has a strong balance sheet, with over $200 million in cash and equivalents as of Q3 2019. This financial stability will enable the company to continue investing in its pipeline and pursue strategic partnerships.
7. **Management Team and Board**: Denali's management team and board of directors have a strong track record in the biotech industry, with experience in developing and commercializing innovative therapies. Their expertise and network could lead to successful partnerships and collaborations.

These factors suggest that Denali Therapeutics Inc. may experience growth in 2020 driven by advancements in its Alzheimer's disease program, expansion of its tau program, partnerships and collaborations, and increased focus on neurodegenerative diseases.

## 0001720725-21-000023 — Oyster Point Pharma, Inc. (2021)
### # Words: T MDA: 5594, T+1 MDA: 9261
### LAB Words:
- tyrvaya, Count in T: 0, Count in T+1: 48
- credit, Count in T: 0, Count in T+1: 31
### Explanation:
Approved in October 2021. Was not announced to be under review until March 2, 2021
https://www.drugs.com/history/tyrvaya.html?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2021-02-18, predict the main growth drivers for Oyster Point Pharma, Inc. in 2021. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0177 (4/226)
Based on information available up to 2021-02-18, the main growth drivers for Oyster Point Pharma, Inc. in 2021 are expected to be:

1. **```TYRVAYA``` (varenicline solution) Nasal Spray**: Oyster Point Pharma's lead product candidate, ```TYRVAYA```, received FDA approval in October 2020 for the treatment of the signs and symptoms of dry eye disease. The commercial launch of ```TYRVAYA``` is expected to drive revenue growth in 2021.

2. **Dry Eye Disease Market Expansion**: The dry eye disease market is growing due to an increasing prevalence of the condition, driven by factors such as aging population, prolonged screen time, and environmental factors. Oyster Point Pharma is well-positioned to capitalize on this trend with ```TYRVAYA```.

3. **Increased Awareness and Diagnosis**: Oyster Point Pharma's efforts to raise awareness about dry eye disease and its treatment options are expected to lead to increased diagnosis and treatment rates, driving growth in 2021.

4. **Expanding Sales and Marketing Efforts**: The company plans to expand its sales and marketing efforts to reach more eye care professionals and patients, which is expected to drive growth in 2021.

5. **Potential Partnerships and Collaborations**: Oyster Point Pharma may explore partnerships and collaborations to expand its reach and offerings, which could drive growth in 2021.

These growth drivers are based on publicly available information and may not reflect the company's actual performance or future events.

## 0001764013-21-000052 — Immunovant, Inc. (2021)
### # Words: T MDA: 8456, T+1 MDA: 5466
### LAB Words:
- batoclimab, Count in T: 0, Count in T+1: 52
### Explanation:
The most recent update at the time was a voluntary pause. 
https://www.immunovant.com/investors/news-events/press-releases/detail/4/immunovant-announces-voluntary-pause-in-clinical-dosing-of?utm_source=chatgpt.com
https://www.immunovant.com/investors/news-events/press-releases/detail/26/immunovant-provides-regulatory-update-regarding-initiation?utm_source=chatgpt.com
### Verdict: Strong LAB
### Input:
Using only information through 2021-06-01, predict the main growth drivers for Immunovant, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0048 (1/210)
Based on information available up to 2021-06-01, Immunovant, Inc.'s main growth drivers for 2022 are likely to be:

1. **IMVT-1401 (```Batoclimab```)**: Immunovant's lead product candidate, an anti-FcRn antibody for the treatment of autoimmune diseases such as myasthenia gravis, Graves' disease, and warm autoimmune hemolytic anemia. Positive results from ongoing clinical trials could drive growth.

2. **Pipeline Expansion**: Immunovant's research and development efforts focused on identifying new targets and developing additional product candidates to address various autoimmune diseases. Expanding the pipeline could attract investors and drive growth.

3. **Strategic Partnerships**: Immunovant's collaborations with pharmaceutical companies, research institutions, or other biotechnology companies could provide access to new technologies, expertise, and resources, driving growth and accelerating the development of its product candidates.

4. **Increased Research and Development Investments**: Immunovant's investments in research and development, including the expansion of its team and infrastructure, could lead to new discoveries and advancements in its product candidates, driving growth.

5. **Growing Demand for Autoimmune Disease Treatments**: The increasing prevalence of autoimmune diseases and the need for effective treatments could drive demand for Immunovant's product candidates, contributing to growth.

Please note that these predictions are based on historical data and may not reflect the actual growth drivers for Immunovant, Inc. in 2022.

## 0001787306-22-000009 — Arcutis Biotherapeutics, Inc. (2022)
### # Words: T MDA: 9466, T+1 MDA: 10403
### LAB Words:
- zoryve, Count in T: 0, Count in T+1: 31
### Explanation:
Approved and name first used in July 2022
https://www.drugs.com/newdrugs/fda-approves-zoryve-roflumilast-cream-plaque-psoriasis-5866.html
### Verdict: Weak LAB (take)
### Input:
Using only information through 2022-02-22, predict the main growth drivers for Arcutis Biotherapeutics, Inc. in 2022. Do not respond with saying you do not know.

### Outputs:
**LLM Config:** 405B Alpha: 0
**Proportion Bad:** 0.0099 (2/202)
Based on information available up to 2022-02-22, the main growth drivers for Arcutis Biotherapeutics, Inc. in 2022 are expected to be:

1. **```Zoryve``` (roflumilast) cream**: The company's lead product candidate, ```Zoryve```, is a topical phosphodiesterase-4 (PDE4) inhibitor for the treatment of plaque psoriasis. Positive results from Phase 3 trials and potential FDA approval in 2022 could drive growth.

2. **ARQ-151 (roflumilast) foam**: Another formulation of roflumilast, ARQ-151 foam, is being developed for the treatment of seborrheic dermatitis and plaque psoriasis. Positive clinical trial results and potential regulatory approvals could contribute to growth.

3. **ARQ-252**: This is a topical Janus kinase (JAK) inhibitor being developed for the treatment of vitiligo and other autoimmune dermatological conditions. Progress in clinical trials and potential partnerships or collaborations could drive growth.

4. **Strategic partnerships and collaborations**: Arcutis Biotherapeutics may form partnerships or collaborations with other pharmaceutical companies to develop and commercialize its products, which could provide additional growth opportunities.

5. **Expansion of the company's pipeline**: Arcutis Biotherapeutics may continue to expand its pipeline through the development of new product candidates, which could drive long-term growth.

These growth drivers are based on the company's product pipeline, clinical trial results, and strategic initiatives as of 2022-02-22.

