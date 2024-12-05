import unittest
from datetime import datetime
from extract_dimensions import extract_product_size  # Assuming the function to test is named extract_product_size

class TestExtractProductSize(unittest.TestCase):

    def setUp(self):
        self.test_data = generate_test_data()

    def test_extract_product_size(self):
        for record in self.test_data:
            with self.subTest(record=record):
                description = record['product_description']
                product_id = record['product_id']
                expected_size = record['product_size']
                result = extract_product_size(description, product_id)
                self.assertEqual(result['product_size'], expected_size, f"Failed for description: {description}")
                self.assertTrue('timestamp' in result, "Timestamp not added")
                self.assertTrue(isinstance(result['timestamp'], str), "Timestamp is not a string")
                try:
                    datetime.fromisoformat(result['timestamp'])
                except ValueError:
                    self.fail("Timestamp is not in ISO format")

if __name__ == '__main__':
    unittest.main()
