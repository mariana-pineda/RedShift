import random
import datetime

# Sample product descriptions and IDs
product_descriptions = [
    "This is a large product with dimensions 10x20x30 cm.",  # Valid size
    "Compact and portable, size: 5x5x5 inches.",  # Valid size
    "Dimensions: 15x25x35 cm, perfect for travel.",  # Valid size
    "No size mentioned here.",  # No size
    "Multiple sizes: 10x10x10 cm and 20x20x20 cm.",  # Multiple sizes
    "Another product with no size info.",  # No size
    "Dimensions: 8x8x8 cm.",  # Valid size
    "Product size: 12x12x12 inches.",  # Valid size
    "Dimensions: 30x40x50 cm.",  # Valid size
    "Size: 7x7x7 cm.",  # Valid size
    "No dimensions available.",  # No size
    "Dimensions: 25x35x45 cm.",  # Valid size
    "Size: 9x9x9 inches.",  # Valid size
    "Dimensions: 50x60x70 cm.",  # Valid size
    "No size info here.",  # No size
    "Dimensions: 20x30x40 cm.",  # Valid size
    "Size: 6x6x6 inches.",  # Valid size
    "Dimensions: 45x55x65 cm.",  # Valid size
    "Size: 11x11x11 cm.",  # Valid size
    "No size mentioned.",  # No size
    "Dimensions: 35x45x55 cm.",  # Valid size
    "Size: 10x10x10 inches.",  # Valid size
    "Dimensions: 60x70x80 cm.",  # Valid size
    "No dimensions here.",  # No size
    "Dimensions: 40x50x60 cm.",  # Valid size
    "Size: 8x8x8 inches.",  # Valid size
    "Dimensions: 55x65x75 cm.",  # Valid size
    "Size: 13x13x13 cm.",  # Valid size
    "No size info.",  # No size
    "Dimensions: 70x80x90 cm."  # Valid size
]

product_ids = [
    "ID001", "ID002", "ID003", "ID004", "ID005", "ID006", "ID007", "ID008", "ID009", "ID010",
    "ID011", "ID012", "ID013", "ID014", "ID015", "ID016", "ID017", "ID018", "ID019", "ID020",
    "ID021", "ID022", "ID023", "ID024", "ID025", "ID026", "ID027", "ID028", "ID029", "ID030"
]

# Function to generate test data
def generate_test_data():
    test_data = []
    for i in range(30):
        description = product_descriptions[i]
        product_id = product_ids[i]
        timestamp = datetime.datetime.now().isoformat()

        # Extract product size from description
        size = None
        if "dimensions" in description.lower() or "size" in description.lower():
            size = description.split(" ")[-2]  # Extracting the first size found
            # Condition: Successfully extract product size from product description
        elif product_id:
            size = f"Size from {product_id}"  # Using product ID if size not in description
            # Condition: Extract product size using product ID when size is not in description
        else:
            size = "Size not available"
            # Condition: Handle missing product size and product ID

        # Add test data record
        test_data.append({
            "product_description": description,
            "product_id": product_id,
            "product_size": size,
            "timestamp": timestamp
        })

    return test_data

# Generate and print test data
test_data = generate_test_data()
for record in test_data:
    print(record)
