import random
from datetime import datetime, timedelta
import string

# Generate test data for employees table with lastdate
def generate_employee_data(num_records):
    employee_data = []
    for _ in range(num_records):
        # Randomly decide if lastdate should be null or not
        if random.choice([True, False]):
            lastdate = None  # Test nullability of lastdate
        else:
            # Generate a random date within the last 5 years
            lastdate = datetime.now() - timedelta(days=random.randint(0, 1825))
            lastdate = lastdate.strftime('%Y-%m-%d')  # Assuming lastdate is of DATE type

        employee_data.append({
            "employee_id": random.randint(1, 1000),
            "lastdate": lastdate
        })
    return employee_data

# Generate test data for customers table with categoryGroup
def generate_customer_data(num_records):
    category_groups = ['Retail', 'Wholesale', 'Online', 'Corporate', 'Government']
    customer_data = []
    for _ in range(num_records):
        # Randomly decide if categoryGroup should be null or not
        if random.choice([True, False]):
            category_group = None  # Test nullability of categoryGroup
        else:
            # Randomly assign a category group
            category_group = random.choice(category_groups)

        customer_data.append({
            "customer_id": random.randint(1, 1000),
            "categoryGroup": category_group
        })
    return customer_data

# Generate 20-30 records for each table
employee_test_data = generate_employee_data(25)
customer_test_data = generate_customer_data(25)

# Output the generated test data
print("Employee Test Data:")
for record in employee_test_data:
    print(record)

print("\nCustomer Test Data:")
for record in customer_test_data:
    print(record)
