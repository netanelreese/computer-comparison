import requests
import yaml
import json

def fetch_component_data():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    data = {}
    for component, url in config['api_endpoints'].items():
        response = requests.get(url)
        if response.status_code == 200:
            data[component] = response.json()
        else:
            print(f"Failed to fetch data for {component}.")

    with open('data/components_data.json', 'w') as json_file:
        json.dump(data, json_file)

    return data
