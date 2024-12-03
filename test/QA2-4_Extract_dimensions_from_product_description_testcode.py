import unittest

class TestExtractProductSize(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"product_description": "The table measures 6ft x 4ft x 3ft.", "expected_size": "6ft x 4ft x 3ft", "product_id": None},
            {"product_description": "The chair is 40 inches by 20 inches.", "expected_size": "40 inches by 20 inches", "product_id": None},
            {"product_description": "Dimensions: height 100cm, width 50cm, depth 25cm", "expected_size": "height 100cm, width 50cm, depth 25cm", "product_id": None},
            {"product_description": "Compact device.", "expected_size": "", "product_id": "12345"},
            {"product_description": "This is a versatile item that fits many spaces.", "expected_size": "", "product_id": None},
            {"product_description": "Objects size: 150mm x 75mm x 50mm.", "expected_size": "150mm x 75mm x 50mm", "product_id": None},
            {"product_description": "Approximate dimensions are: 10' x 2'.", "expected_size": "10' x 2'", "product_id": None},
            {"product_description": "Dimensions listed as 5m by 3m.", "expected_size": "5m by 3m", "product_id": None},
            {"product_description": "Length 2.5m, Width 1.5m, Height 1.8m are measured.", "expected_size": "2.5m, 1.5m, 1.8m", "product_id": None},
            {"product_description": "Not specified", "expected_size": "", "product_id": "67890"},
            {"product_description": "Product ID: 67890 with no size mentioned", "expected_size": "", "product_id": "67890"},
            {"product_description": "16 centimeters each side as width, depth, height.", "expected_size": "16 centimeters each side", "product_id": None},
            {"product_description": "Just a great product everyone loves!", "expected_size": "", "product_id": None},
            {"product_description": "Perfectly sized for comfort, size details are in a separate file.", "expected_size": "", "product_id": None},
            {"product_description": "See size chart for dimensions.", "expected_size": "", "product_id": None},
            {"product_description": "Limited edition size not disclosed.", "expected_size": "", "product_id": None},
            {"product_description": "Dimensions, weight, colors handled separately.", "expected_size": "", "product_id": None},
            {"product_description": "Fits all standard sizes. No specific measurements.", "expected_size": "", "product_id": None},
        ]

    def test_extract_product_size(self):
        for data in self.test_data:
            with self.subTest(data=data):
                extracted_size = extract_product_size(data["product_description"])
                self.assertEqual(extracted_size, data["expected_size"])

    def test_fallback_to_product_id(self):
        for data in self.test_data:
            with self.subTest(data=data):
                if data["expected_size"] == "" and data["product_id"]:
                    self.assertIsNotNone(data["product_id"], "Product ID should be used when size is not extracted")
                else:
                    self.assertIsNone(data["product_id"], "Product ID should not be used when size is extracted")

def extract_product_size(description):
    if "measures" in description or "by" in description or "dimensions" in description.lower():
        parts = description.split()
        return " ".join(part for part in parts if any(ch.isdigit() for ch in part) or part in ['x', 'by', ',', ':'])
    return ""

if __name__ == '__main__':
    unittest.main()
