import random

descriptions_with_size = [
    "This item has a size of 20x30x40.",              # Validate successful extraction
    "Dimensions are 15cm x 25cm x 35cm.",             # Validate successful extraction with cm
    "Size is 8.5 inches by 11 inches by 1 inch.",     # Validate extraction with inches
    "Measures approximately 10x20x30 units.",         # Validate approximate size
    "Dimension: Height 10 cm, Width 20 cm, Length 30 cm.",  # Validate mixed format
]

descriptions_without_size = [
    "No specific dimensions.",                        # Validate fallback to product ID
    "This product is dimensionless.",                 # Validate fallback to product ID
    "Size not available.",                            # Validate fallback to product ID
    "See product for dimensions.",                    # Validate fallback to product ID
    "Dimensions: N/A.",                               # Validate fallback to product ID
]

malformed_data = [
    "",                                               # Validate handling empty string
    "Dimensions: unknown",                            # Validate handling unknown dimensions
    "Dimensions: ???",                                # Validate handling malformed data
    "Incomplete dimensions.",                         # Validate handling incomplete information
    "Error retrieving dimensions.",                   # Validate handling error in dimensions
]

product_ids = [f'{random.randint(10000, 99999)}' for _ in range(30)]

test_data = []

# Generate test data for descriptions with size
for description in descriptions_with_size:
    test_data.append({
        "product_description": description,
        "expected_product_size": description.split(":")[1].strip(),
        "product_id": random.choice(product_ids),
    })

# Generate test data for descriptions without size, expect fallback on product ID
for description in descriptions_without_size:
    product_id = random.choice(product_ids)
    test_data.append({
        "product_description": description,
        "expected_product_size": None,
        "product_id": product_id,
        "expected_fallback_product_id": product_id,    # Validate fallback mechanism
    })

# Generate test data for malformed data
for description in malformed_data:
    product_id = random.choice(product_ids)
    test_data.append({
        "product_description": description,
        "expected_product_size": None,
        "product_id": product_id,
    })

for data in test_data:
    print(data)
