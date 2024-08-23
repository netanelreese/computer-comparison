import unittest
from src.plot import plot_comparison

class TestPlotComparison(unittest.TestCase):
    def test_plot_comparison(self):
        sample_comparison = {
            "cpu": {"current": {"performance": 95}, "potential": {"performance": 100}},
            "gpu": {"current": {"performance": 80}, "potential": {"performance": 85}},
        }
        # Plotting does not return anything, so just ensure no exceptions are raised
        plot_comparison(sample_comparison)

if __name__ == '__main__':
    unittest.main()
