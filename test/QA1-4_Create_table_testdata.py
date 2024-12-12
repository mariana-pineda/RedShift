import random
from datetime import datetime, timedelta
import string

# Predefined categories for categoryGroup
predefined_categories = ['Retail', 'Wholesale', 'Online', 'Corporate']

# Generate test data for Employees table
def generate_employees_data(num_records):
    employees_data = []
    for _ in range(num_records):
        # Validate lastdate as TIMESTAMP and default to current date
        lastdate = datetime.now() - timedelta(days=random.randint(0, 365))
        employees_data.append({
            'lastdate': lastdate.strftime('%Y-%m-%d %H:%M:%S')  # TIMESTAMP format
        })
    return employees_data

# Generate test data for Customers table
def generate_customers_data(num_records):
    customers_data = []
    for _ in range(num_records):
        # Validate categoryGroup as VARCHAR with max length 255 and predefined categories
        categoryGroup = random.choice(predefined_categories)
        customers_data.append({
            'categoryGroup': categoryGroup
        })
    return customers_data

# Generate 20-30 records for each table
employees_test_data = generate_employees_data(25)
customers_test_data = generate_customers_data(25)

# Output the generated test data
print("Employees Test Data:")
for record in employees_test_data:
    print(record)

print("\nCustomers Test Data:")
for record in customers_test_data:
    print(record)
