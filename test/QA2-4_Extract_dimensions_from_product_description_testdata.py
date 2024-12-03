import random

def generate_test_data():
    descriptions = [
        "The table measures 6ft x 4ft x 3ft.", # Product size can be extracted
        "The chair is 40 inches by 20 inches.", # Product size can be extracted
        "Dimensions: height 100cm, width 50cm, depth 25cm", # Ustructured but extractable
        "Compact device.", # Unable to extract
        "This is a versatile item that fits many spaces.", # Unable to extract
        "Objects size: 150mm x 75mm x 50mm.", # Extractable in different unit
        "Approximate dimensions are: 10' x 2'.", # Extractable sizes in both single and double quote
        "Dimensions listed as 5m by 3m.", # Extractable in meters
        "Length 2.5m, Width 1.5m, Height 1.8m are measured.", # Extractable with measurements embedded
        "Not specified", # Unable to extract
        "Product ID: 67890 with no size mentioned", # Unable to extract, product_id condition
        "16 centimeters each side as width, depth, height.", # Extractable when unit is part of description
        # Intentionally vague or irrelevant text
        "Just a great product everyone loves!", # Unable to extract
        "Perfectly sized for comfort, size details are in a separate file.", # Unable to extract
        "See size chart for dimensions.", # Unable to extract
        "Limited edition size not disclosed.", # Unable to extract
        "Dimensions, weight, colors handled separately.", # Unable to extract
        "Fits all standard sizes. No specific measurements.", # Unable to extract
    ]
    
    product_ids = [12345, 67890, 24680, 13579, 98765] # Sample product IDs

    data = []

    for i in range(20): # Generate 20-30 records
        description = random.choice(descriptions)
        product_id = random.choice(product_ids) if "unable" in description.lower() or "not specified" in description.lower() else None
        product_size = extract_product_size(description) if "dimensions" in description.lower() else "" # Simulate extraction function

        data.append({
            "product_description": description,
            "product_size": product_size,
            "product_id": product_id if not product_size else ""
        })
    
    return data

def extract_product_size(description):
    # Simulated extraction logic
    if "dimensions" in description.lower() or "measures" in description.lower() or "by" in description:
        extracted = " ".join(description.split()[1:]) # Simplified logic
        return extracted
    return ""

# Print the generated test data
generated_data = generate_test_data()
for record in generated_data:
    print(record)

This script generates synthetic test data for evaluating the extraction of product size from product descriptions according to various conditions specified in the user story. It simulates both extractable descriptions and those that necessitate fallback to a product ID or receive no size data.