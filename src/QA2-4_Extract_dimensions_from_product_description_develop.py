import re

class ProductSizeExtractor:
    def __init__(self, description, product_id):
        self.description = description
        self.product_id = product_id

    def extract_product_size(self):
        # Define a regex pattern to capture dimension strings
        patterns = [
            r"\b\d+(\.\d+)?\s*(?:x|by)\s*\d+(\.\d+)?\s*(?:x|by)\s*\d+(\.\d+)?\b",  # "X x Y x Z" or "X by Y by Z"
            r"(?:Height|Width|Length)\s*\d+\s*(?:cm|inches|units)",  # Height/Width/Length format
        ]

        for pattern in patterns:
            match = re.search(pattern, self.description, re.IGNORECASE)
            if match:
                return match.group().strip()

        return None

    def get_product_size_or_fallback(self):
        size = self.extract_product_size()
        return size if size else self.product_id

if __name__ == "__main__":
    # Simulating how this logic would be used
    sample_descriptions = [
        "This item has a size of 20x30x40.",
        "Dimensions are 15cm x 25cm x 35cm.",
        "Size is 8.5 inches by 11 inches by 1 inch.",
        "Measures approximately 10x20x30 units.",
        "Dimension: Height 10 cm, Width 20 cm, Length 30 cm.",
        "No specific dimensions.",
        ""
    ]

    sample_ids = ["12345", "67890", "54321", "11223", "99887", "67890"]

    for desc, product_id in zip(sample_descriptions, sample_ids):
        extractor = ProductSizeExtractor(desc, product_id)
        size_or_id = extractor.get_product_size_or_fallback()
        print(f"Description: {desc} => Size or Fallback ID: {size_or_id}")
