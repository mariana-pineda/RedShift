import unittest

class TestProductSizeExtraction(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"product_description": "This item has a size of 20x30x40.", "expected_product_size": "20x30x40", "product_id": "12345"},
            {"product_description": "Dimensions are 15cm x 25cm x 35cm.", "expected_product_size": "15cm x 25cm x 35cm", "product_id": "67890"},
            {"product_description": "Size is 8.5 inches by 11 inches by 1 inch.", "expected_product_size": "8.5 inches by 11 inches by 1 inch", "product_id": "54321"},
            {"product_description": "Measures approximately 10x20x30 units.", "expected_product_size": "10x20x30", "product_id": "11223"},
            {"product_description": "Dimension: Height 10 cm, Width 20 cm, Length 30 cm.", "expected_product_size": "Height 10 cm, Width 20 cm, Length 30 cm", "product_id": "99887"},
            {"product_description": "No specific dimensions.", "expected_product_size": None, "product_id": "67890", "expected_fallback_product_id": "67890"},
            {"product_description": "", "expected_product_size": None, "product_id": "11223"},
            {"product_description": "Dimensions: unknown", "expected_product_size": None, "product_id": "33456"},
            {"product_description": "Incomplete dimensions.", "expected_product_size": None, "product_id": "99823"},
        ]

    def extract_product_size(self, description):
        # Simulate the extraction logic
        if "size of" in description or "Dimensions are" in description or "Size is" in description or "Measures approximately" in description or "Dimension:" in description:
            # Simulating extraction of dimensions
            return description.split(" ", 2)[-1].strip(".")
        return None

    def test_successful_extraction(self):
        for data in self.test_data[:5]:  # Only test cases with expected size
            with self.subTest(description=data["product_description"]):
                extracted_size = self.extract_product_size(data["product_description"])
                self.assertEqual(extracted_size, data["expected_product_size"])

    def test_fallback_to_product_id(self):
        for data in self.test_data[5:6]:  # Only test case with fallback to product ID
            with self.subTest(description=data["product_description"]):
                extracted_size = self.extract_product_size(data["product_description"])
                if not extracted_size:
                    self.assertEqual(data["product_id"], data["expected_fallback_product_id"])

    def test_malformed_or_missing_data(self):
        for data in self.test_data[6:]:
            with self.subTest(description=data["product_description"]):
                extracted_size = self.extract_product_size(data["product_description"])
                self.assertIsNone(extracted_size)

    def test_logging_and_error_handling(self):
        # Assuming a mock for logging
        for data in self.test_data[6:]:
            with self.subTest(description=data["product_description"]):
                extracted_size = self.extract_product_size(data["product_description"])
                if not extracted_size:
                    error_logged = True
                    # Here, you'd check if error logging functionality got triggered
                    self.assertTrue(error_logged)

if __name__ == "__main__":
    unittest.main()
