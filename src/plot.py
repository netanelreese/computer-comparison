import matplotlib.pyplot as plt

def plot_comparison(comparison_results):
    for component, result in comparison_results.items():
        plt.figure(figsize=(10, 5))
        plt.title(f"{component.upper()} Performance Comparison")
        plt.bar(["Current", "Potential"], [result["current"].get("performance", 0), result["potential"].get("performance", 0)])
        plt.ylabel("Performance")
        plt.xlabel("Configuration")
        plt.show()
