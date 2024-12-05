import re
from datetime import datetime

def extract_product_size(product_description, product_id):
    # Regular expression to find dimensions in the format of numbers separated by 'x'
    size_pattern = re.compile(r'\b\d+x\d+x\d+\b')
    match = size_pattern.search(product_description)
    
    if match:
        product_size = match.group(0)
    elif product_id:
        product_size = f"Size from {product_id}"
    else:
        product_size = "Size not available"
    
    # Add timestamp
    timestamp = datetime.now().isoformat()
    
    return {
        "product_size": product_size,
        "timestamp": timestamp
    }
