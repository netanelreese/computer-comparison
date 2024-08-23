"""
Reads JSON data.

Parses it for the requests.
"""

import requests

def fetch_json_data(url, timeout=10):
    """
    Plots the data points from the comparison class.
    """

    try:
        response = requests.get(url, timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
