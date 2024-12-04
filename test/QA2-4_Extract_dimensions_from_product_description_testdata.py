import random
import pandas as pd

# Define possible patterns in product descriptions
dimension_patterns = [
    "x", "inches", "cm", "pounds", "kg", "foot", "feet"
]

# Generate random product descriptions based on defined patterns
def generate_product_descriptions():
    descriptions = []
    for _ in range(25): # Generating 25 test data records
        size_type = random.choice(["dimensions pattern", "single dimension pattern", "unknown"])
        if size_type == "dimensions pattern":
            length = random.randint(1, 20)
            width = random.randint(1, 20)
            height = random.randint(1, 20)
            unit = random.choice(dimension_patterns)
            description = f"This is a product with size {length}x{width}x{height} {unit}."
            expected_size = f"{length}x{width}x{height} {unit}"
        elif size_type == "single dimension pattern":
            dimension = random.choice(["length", "width", "height"])
            value = random.randint(1, 20)
            unit = random.choice(dimension_patterns)
            description = f"A product with {dimension} of {value} {unit}."
            expected_size = f"{value} {unit}"
        else: # Unknown pattern where size cannot be extracted
            description = "This description has no size information."
            expected_size = "N/A"
        
        product_id = random.randint(10000, 99999)
        descriptions.append((description, size_type, expected_size, product_id))
    return descriptions

# Generate data in a list of dictionaries to convert into CSV later
test_data = generate_product_descriptions()

# Create a DataFrame for better visualization or storage in a CSV file
df = pd.DataFrame(test_data, columns=["product_description", "format", "expected_product_size", "product_id"])

# Output the generated data
print(df)

# Sample comments to understand conditions:
# For dimensions pattern: validates multiple dimensions extraction
# For single dimension pattern: checks single attribute extraction
# For unknown pattern: tests fallback to product_id when no dimensions found
