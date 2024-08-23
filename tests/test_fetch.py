import unittest
from src.fetch import fetch_component_data

class TestFetchData(unittest.TestCase):
    def test_fetch_component_data(self):
        data = fetch_component_data()
        self.assertIsInstance(data, dict)
        self.assertIn("cpu", data)

if __name__ == '__main__':
    unittest.main()
