import csv
import json
import time
import requests


with open('comments.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Extract the header and comments column
header = data[0]
comments = [row[1] for row in data[1:]]  

# Define API URL and headers
api_url = 'Enter api url' #aixplain pipeline
api_key = 'Enter api key'  #aixplain key
headers = {
    'x-api-key': api_key,
    'content-type': 'application/json'
}


def poll_for_results(url):
    while True:
        response = requests.get(url, headers=headers)
        results = response.json()
        if results.get('completed'):
            return results['data']
        time.sleep(5)


results = []
for comment in comments:

    input_data = json.dumps({"data": comment})
    response = requests.post(api_url, headers=headers, data=input_data)
    result_url = response.json().get('url')


    sentiment_result = poll_for_results(result_url)


    print("Sentiment Result:", sentiment_result)  

    if isinstance(sentiment_result, list) and sentiment_result:
        sentiment_label = sentiment_result[0]['label']  
    else:
        sentiment_label = "Unknown" 

    results.append([comment, sentiment_label])

with open('comments_with_sentiment.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header + ['Sentiment']) 
    writer.writerows(results)
