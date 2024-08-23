import yaml

def compare_performance(data):
    with open('config/config.yaml', 'r') as file:
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
