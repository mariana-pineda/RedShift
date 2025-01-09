import csv
import random
import hashlib

# Define the paths for the CSV files
product_revenue_path = '/Volumes/agilisium_playground/purgo_playground/d_product_revenue_csv/d_product_revenue.csv'
customer_path = '/Volumes/agilisium_playground/purgo_playground/d_product_revenue_csv/customer.csv'

# Define the number of records to generate
num_records = 25

# Generate test data for d_product_revenue.csv
with open(product_revenue_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['product_id', 'customer_id', 'revenue', 'product_name'])
    for _ in range(num_records):
        # Generate random data
        product_id = random.randint(1000, 9999)
        customer_id = random.randint(1, 100)  # Ensure some overlap with customer.csv
        revenue = round(random.uniform(1000, 10000), 2)
        product_name = f'Product_{random.randint(1, 100)}'
        writer.writerow([product_id, customer_id, revenue, product_name])

# Generate test data for customer.csv
with open(customer_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['customer_id', 'customer_name', 'customer_email'])
    for _ in range(num_records):
        # Generate random data
        customer_id = random.randint(1, 100)  # Ensure some overlap with d_product_revenue.csv
        customer_name = f'Customer_{random.randint(1, 100)}'
        customer_email = f'customer{random.randint(1, 100)}@example.com'
        writer.writerow([customer_id, customer_name, customer_email])

# Function to create surrogate key by concatenating and hashing
def create_surrogate_key(row):
    concatenated = ''.join(map(str, row))
    return hashlib.sha256(concatenated.encode()).hexdigest()

# Example of how surrogate key would be generated after join
# This is a placeholder to demonstrate the logic
example_joined_row = ['product_id', 'customer_id', 'revenue', 'product_name', 'customer_name', 'customer_email']
surrogate_key = create_surrogate_key(example_joined_row)
print(f'Surrogate Key Example: {surrogate_key}')
