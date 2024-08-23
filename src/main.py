from src.fetch import fetch_component_data
from src.compare import compare_performance
from src.plot import plot_comparison

def main():
    data = fetch_component_data()
    comparison_results = compare_performance(data)
    plot_comparison(comparison_results)

if __name__ == "__main__":
    main()
