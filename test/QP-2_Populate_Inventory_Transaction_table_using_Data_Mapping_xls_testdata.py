import random
from datetime import datetime, timedelta
import uuid

# Define possible sources for items and unit cost to simulate transformations
items = [f"item_{i}" for i in range(1, 21)]  # 20 unique items
unit_costs = [round(random.uniform(1.0, 100.0), 2) for _ in range(20)]

# Generate test data records
test_data_records = []

for _ in range(25):  # Create 25 records
    record = {
        # Validate: Ensure unique identifiers and fields assumed to be unique (e.g., transaction ID)
        "transaction_id": str(uuid.uuid4()),

        # Validate: Data type consistency for dates
        "expired_dt": datetime.now() - timedelta(days=random.randint(1, 100)),
        "cancel_dt": datetime.now() - timedelta(days=random.randint(1, 50)),

        # Validate: Ensure calculations for financial_qty and net_qty without conflict
        "financial_qty": random.randint(5, 100),
        "net_qty": random.randint(1, 5),  # Smaller quantities to simulate computation scenarios

        # Validate: Implement transformations for item_nbr and unit_cost
        "item_nbr": random.choice(items),  # Simulate transformation from source
        "unit_cost": random.choice(unit_costs),  # Simulate transformation from source

        # Validate: Handling null values and discrepancies
        "expired_qt": (random.choice([None, random.randint(0, 50)])  # Randomly introduce nulls

                        if random.random() < 0.2 else random.randint(0, 50)),  # 20% chance null

        # Validate: Manage timestamps for creation and updates
        "crt_dt": datetime.now() - timedelta(days=random.randint(1, 200)),
        "updt_dt": datetime.now() - timedelta(days=random.randint(1, 100)),
    }

    # Automatically ensure that updt_dt is after crt_dt
    if record["updt_dt"] < record["crt_dt"]:
        record["updt_dt"] = record["crt_dt"] + timedelta(days=random.randint(1, 10))

    test_data_records.append(record)

# Print generated test data
for record in test_data_records:
    print(record)
