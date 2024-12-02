import random
import string
import datetime

# Function to generate random SKU codes
def generate_sku():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Function to generate transaction types (e.g., 'receipt', 'shipment')
def generate_transaction_type():
    return random.choice(['Receipt', 'Shipment', 'Adjustment'])

# Function to generate random quantities (validate boundary conditions: zero and negative)
def generate_quantity():
    return random.choice([0, -5, random.randint(1, 1000)])

# Function to generate random dates in the past month
def generate_date():
    start_date = datetime.datetime.now() - datetime.timedelta(days=30)
    random_date = start_date + datetime.timedelta(days=random.randint(0, 30))
    return random_date.strftime('%Y-%m-%d')

# Function to generate random supplier IDs (For unique constraint validation)
def generate_supplier_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# Function to generate boolean for discrepancy status (validation for data discrepancies handling)
def generate_discrepancy_flag():
    return random.choice([True, False])

# Generate 20-30 test data records
inventory_transactions = []

for _ in range(25):
    transaction = {
        "SKU": generate_sku(),  # Unique SKU code
        "TransactionType": generate_transaction_type(),  # Tests different possible transaction types
        "Quantity": generate_quantity(),  # Tests boundary conditions (zero and negative)
        "TransactionDate": generate_date(),  # Random date check
        "SupplierID": generate_supplier_id(),  # Ensures unique constraints on suppliers
        "DiscrepancyFlag": generate_discrepancy_flag(),  # Data discrepancies handling
    }
    inventory_transactions.append(transaction)

# Print the generated test data
for transaction in inventory_transactions:
    print(transaction)
