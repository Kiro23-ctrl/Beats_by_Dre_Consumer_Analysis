# -*- coding: utf-8 -*-
"""Data_Mining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qpx4EBflluUC5crqBitFD2FoIqYicf7B
"""

import pandas as pd
import json
from datetime import datetime

# Header to set the requests as a browser requests
headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

json_file_paths = [
    '/content/B&W_PX8.json',
    '/content/BEATS_PRO_pg1-20.json',
    '/content/Bang_Olufsen_Beoplay_HX.json',
    '/content/Beats_Solo3.json',
    '/content/Bose_Headphones_700.json',
    '/content/Bose_QuietComfort.json',
    '/content/SEINHEISSER_MOM4_PG1_20.json',
    '/content/SONYXM5.json',
    '/content/SONY_XM4.json',
    '/content/Soundcore_Anker_Life_Q20.json'
]

# Initialize an empty list to hold DataFrames
dataframes = []

# Loop through each JSON file, convert to DataFrame, and append to the list
for json_file_path in json_file_paths:
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    reviews_data = []
    count = 0
    for result in data['results']:
        asin = result['content']["asin"]
        for review in result['content']['reviews']:
            count += 1
            try:
                review_info = {
                    'review_id': review['id'],
                    'product_id': asin,
                    'title': review['title'],
                    'author': review['author'],
                    'rating': review['rating'],
                    'content': review['content'],
                    'timestamp': review['timestamp'],
                    'profile_id': review['profile_id'],
                    'is_verified': review['is_verified'],
                    'helpful_count': review.get('helpful_count', 0),
                    'product_attributes': review['product_attributes']
                }
                reviews_data.append(review_info)
            except Exception as e:
                print(f"Error processing review {count}: {e}")
                continue

    reviews_df = pd.DataFrame(reviews_data)
    csv_file_path = json_file_path.replace('.json', '.csv')
    reviews_df.to_csv(csv_file_path, index=False)
    dataframes.append(reviews_df)

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_csv_file_path = '/content/Combined_Data_Products.csv'
combined_df.to_csv(combined_csv_file_path, index=False)

# Display the first few rows of the combined DataFrame
display(combined_df.head())

combined_df = pd.read_csv('/content/Combined_Data_Products.csv')

# Display the DataFrame
display(combined_df)