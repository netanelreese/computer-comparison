"""
This module serves as the entry point for the computer performance comparison program.

It fetches component data, compares the performance of the current system
against potential new systems, and generates plots to visualize the results.
"""

from src.fetch import fetch_component_data
from src.compare import compare_performance
from src.plot import plot_comparison

def main():
    """
    Main function that orchestrates the fetching of component data,
    performance comparison, and plotting of results.
    """
           
    data = fetch_component_data()
    comparison_results = compare_performance(data)
    plot_comparison(comparison_results)

if __name__ == "__main__":
    main()
