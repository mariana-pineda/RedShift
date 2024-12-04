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
            # Validate inbound inventory transaction
            "transaction_id": random.randint(1000, 9999),
            "item_id": random.randint(1, 100),
            "quantity": random.randint(1, 500),  # Validate quantity range
            "transaction_type": random.choice(["inbound", "outbound"]),  # Validate transaction type
            "transaction_date": random_date(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)),
            "supplier_id": random.randint(1, 50),  # Validate supplier ID range
            "warehouse_id": random.randint(1, 10),  # Validate warehouse ID range
            "unit_price": round(random.uniform(10.0, 100.0), 2),  # Validate unit price range
            "total_value": lambda record: record["quantity"] * record["unit_price"],  # Validate total value calculation
            "status": random.choice(["pending", "completed", "cancelled"])  # Validate status options
        }
        # Calculate total value based on quantity and unit price
        record["total_value"] = record["total_value"](record)
        data.append(record)
    return data

# Generate 20-30 records
test_data = generate_inventory_transaction_data(25)

# Print the generated test data
for record in test_data:
    print(record)
