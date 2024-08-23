"""
Reads JSON data.

Parses it for the requests.
"""

import requests

def fetch_json_data(url):
    """
    Plots the data points from the comparison class.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
