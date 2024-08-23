"""
This module compares different components of different PC's or standalone parts.

It takes data from fetch and compares it to eachother.
"""

import yaml

def compare_performance(data):
    """
    Compares performance of CPU to CPU, GPU to GPU, etc.
    """

    with open('config/config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    current_system = config['current_system']
    comparison_results = {}

    for component in current_system.keys():
        current_value = data[component].get(current_system[component], {})
        comparison_results[component] = {
            "current": current_value,
            "potential": data[component]
        }

    return comparison_results
