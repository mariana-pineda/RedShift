import csv
import random

# Sample data for product descriptions and product IDs
product_descriptions = [
    "This is a large t-shirt with a size of L.",
    "Medium-sized jacket available in M.",
    "Small socks, size S.",
    "Extra-large pants, XL size.",
    "Size not mentioned here.",
    "Contains multiple sizes: S, M, L.",
    "No size information available.",
    "Size: XXL for this coat.",
    "Product with size L and XL.",
    "Size: M, but also available in S.",
    "Size: S, M, L, XL, XXL.",
    "Size: L",
    "Size: M",
    "Size: S",
    "Size: XL",
    "Size: XXL",
    "Size: XS",
    "Size: 3XL",
    "Size: 4XL",
    "Size: 5XL",
    "Size: 6XL",
    "Size: 7XL",
    "Size: 8XL",
    "Size: 9XL",
    "Size: 10XL",
    "Size: 11XL",
    "Size: 12XL",
    "Size: 13XL",
    "Size: 14XL",
    "Size: 15XL"
]

product_ids = [
    "ID12345", "ID67890", "ID54321", "ID09876", "ID11223",
    "ID44556", "ID77889", "ID99000", "ID11122", "ID33344",
    "ID55566", "ID77788", "ID99900", "ID22233", "ID44455",
    "ID66677", "ID88899", "ID00011", "ID22244", "ID33355",
    "ID44466", "ID55577", "ID66688", "ID77799", "ID88800",
    "ID99911", "ID00022", "ID11133", "ID22255", "ID33366"
]

# Generate test data
with open('product_desc_new.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["product_id", "product_description"])  # Header

    for i in range(30):
        product_description = random.choice(product_descriptions)
        product_id = random.choice(product_ids)
        writer.writerow([product_id, product_description])

# Conditions being validated:
# 1. Extracting size from product description when available.
# 2. Using product ID as a fallback when size is not in description.
# 3. Handling multiple sizes in a single product description.
# 4. Generating a variety of product descriptions to test different scenarios.
