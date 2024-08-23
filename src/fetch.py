"""
Fetches data from API's in config.yaml to send to compare class.

Uses requests yaml and json to scrape data.
"""

import json
import requests
import yaml

def fetch_component_data():
    """
    Fetches data from API's in config.yaml to send to compare class.
    """

    with open('config/config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    data = {}
    for component, url in config['api_endpoints'].items():
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data[component] = response.json()
        else:
            print(f"Failed to fetch data for {component}.")

    with open('config/config.yaml', 'r', encoding='utf-8') as json_file:
        json.dump(data, json_file)

    return data
