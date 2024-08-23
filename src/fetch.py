"""
Fetches data from API's in config.yaml to send to compare class.

Uses requests yaml and json to scrape data.
"""

import json
import time
import requests
import yaml

def fetch_json_data(url, timeout=10, retries=3, backoff_factor=0.3):
    """
    Fetch JSON data from a given URL with a specified timeout and retry mechanism.

    Args:
        url (str): The URL to fetch the JSON data from.
        timeout (int): The timeout in seconds for the request. Default is 10 seconds.
        retries (int): Number of retries in case of failure. Default is 3 retries.
        backoff_factor (float): A backoff factor to apply between attempts after a failure.

    Returns:
        dict: The JSON data if the request is successful, None otherwise.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                sleep_time = backoff_factor * (2 ** attempt)
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                print("Max retries reached. Failed to fetch data.")
                return None
