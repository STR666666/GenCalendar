"""
File: gold_api.py
Description: Make api call to get all classes and save the response in api_responses.json
"""
import requests
import json
from constants import *

def call_api(api_key, api_endpoint, quarter, page_size=100):
    headers = {
        'ucsb-api-key': api_key,
        'Content-Type': 'application/json'
    }

    all_results = []

    try:
        page_number = 1

        while True:
            response = requests.get(api_endpoint, headers=headers, params={'quarter': quarter, 'pageNumber': page_number, 'pageSize': page_size, 'includeClassSections': 'true'})

            if response.status_code == 200:
                data = response.json()

                if not data["classes"]: break

                all_results.extend(data['classes'])
                page_number += 1
            else:
                print(f"Error: API call failed with status code {response.status_code}")
                print(f"Response Content: {response.text}")
                break

        with open('api_responses.json', 'w') as json_file:
            json.dump(all_results, json_file, indent=4)

        print(f"All API calls successful. Results saved to 'api_responses.json'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    api_key = CONSUMER_KEY
    api_endpoint = CLASSES_ENDPOINT
    quarter = '20201'  # Specify the quarter when calling the function

    call_api(api_key, api_endpoint, quarter)
