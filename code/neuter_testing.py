#Slide 7 in the Deck

from openai import OpenAI
from dotenv import load_dotenv
from utils import key_to_seed
from neuter_mdas import entity_neutering_prompt
from guess_info import guessing_info_prompt

load_dotenv()
client = OpenAI()

prompt1 = """Available this holiday season in the United States, Zune includes a 30GB digital media player, the Zune Marketplace music service and a foundation for an online community that will enable music fans to discover new music. The Zune device features wireless technology, a built-in FM tuner and a bright, 3-inch screen that allows users to not only show off music, pictures and video, but also to customize the experience with personal pictures or themes to truly make the device their own. Zune comes in three colors: black, brown and white."""
prompt2 = """Diamond Multimedia Systems, Inc., (Nasdaq: DIMD), a leader in interactive multimedia and PC entertainment, today unveiled the Rio PMP300, a portable music player that stores and plays-back up to sixty minutes of digital quality music for under $200.
Based on the most popular Internet music format, MP3 compression, and flash memory technology, Diamond's Rio PMP300 portable music player is like a Walkman or MiniDisk player, only much lighter and smaller. Rio also has no moving parts, which means no skipping, even when subjected to heavy vibration and movement such as during extreme sports activities. Additionally, the Rio PMP300 includes Jukebox MP3 software licensed from MusicMatch Corporation and Xing Technology Corporation, allowing users to convert CD tracks from their personal music collection into MP3 format using their PC. Users can then create a customized mix of music that can be played back on the Rio PMP300 or on their PC. Rio is expected to ship to online music resellers and select retailers in October for an estimated retail price (ERP) of $199.95. Customers can also pre-order the Rio PMP300, starting today, through Diamond Multimedia's online store."""

prompt2_output = """Company_1, (Nasdaq: ticker_x), a leader in product_type_1 and product_type_2, today unveiled product_x, a portable product_type_3 that stores and plays back up to number_a minutes of digital quality product_type_4 for under number_b. Based on the most popular Internet product_type_5 format, product_type_6 compression, and product_type_7 technology, Company_1's product_x portable product_type_3 is like a product_type_8 or product_type_9 player, only much lighter and smaller. product_x also has no moving parts, which means no skipping, even when subjected to heavy vibration and movement such as during product_type_10 activities. Additionally, the product_x includes product_type_11 software licensed from Company_2 and Company_3, allowing users to convert product_type_12 tracks from their personal product_type_13 collection into product_type_5 format using their product_type_14. Users can then create a customized mix of product_type_4 that can be played back on the product_x or on their product_type_14. product_x is expected to ship to online product_type_15 and select product_type_16 in time_x for an estimated retail price (ERP) of number_c. Customers can also pre-order the product_x, starting today, through Company_1's online store."""


for run in range(5):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": guessing_info_prompt}, 
                {"role": "user", "content": prompt2_output}],
        temperature=0, 
        seed=key_to_seed(prompt2 + str(run)),
    )

    print(response.choices[0].message.content)
    print("--------------------------------")