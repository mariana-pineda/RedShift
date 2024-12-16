import random
import datetime

# Function to generate random date
def random_date(start, end):
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))

# Function to generate random inventory transaction data
def generate_inventory_transaction_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            # Validate inbound inventory recording
            "transaction_id": random.randint(1000, 9999),
            "item_id": random.randint(1, 100),
            "quantity": random.randint(1, 500),
            "transaction_type": random.choice(["inbound", "outbound"]),
            "transaction_date": random_date(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)),
            "source_system": random.choice(["Redshift", "Databricks"]),
            # Validate data discrepancies between Redshift and Databricks
            "discrepancy_flag": random.choice([True, False]),
            # Validate error handling during SQL logic execution
            "error_logged": random.choice([True, False]),
            # Validate output format and reporting requirements
            "report_generated": random.choice([True, False])
        }
        data.append(record)
    return data

# Generate 20-30 records
test_data = generate_inventory_transaction_data(25)

# Print the generated test data
for record in test_data:
    print(record)
