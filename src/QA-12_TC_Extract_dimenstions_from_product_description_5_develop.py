import csv

def extract_product_size(product_id, product_description):
    try:
        if product_description:
            parts = product_description.split('-')
            if len(parts) >= 3:
                return parts[-3] + '-' + parts[-2] + '-' + parts[-1]
        
        if product_id:
            parts = product_id.split('-')
            if len(parts) >= 3:
                return parts[-3] + '-' + parts[-2] + '-' + parts[-1]
    except Exception as e:
        print(f"Error extracting size: {e}")

    return None

def process_product_data():
    with open('product_desc_new.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_id = row['product_id']
            product_description = row['product_description']
            expected_size = row['product_size']

            actual_size = extract_product_size(product_id, product_description)
            
            if actual_size is None and row['dimension_1'] and row['dimension_2'] and row['dimension_3']:
                actual_size = f"{row['dimension_1']}-{row['dimension_2']}-{row['dimension_3']}"

            # Output or further processing of actual_size here

process_product_data()
