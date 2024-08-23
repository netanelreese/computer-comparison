import unittest
from src.compare import compare_performance

class TestComparePerformance(unittest.TestCase):
    def test_compare_performance(self):
        sample_data = {
            "cpu": {"Intel Core i5-12600K": {"performance": 95}},
            "gpu": {"Intel Arc A770": {"performance": 80}},
            "ssd": {"Samsung 970 EVO 1TB": {"performance": 90}},
            "ram": {"16GB DDR4": {"performance": 70}}
        }
        comparison = compare_performance(sample_data)
        self.assertIn("cpu", comparison)
        self.assertIn("current", comparison["cpu"])

if __name__ == '__main__':
    unittest.main()
