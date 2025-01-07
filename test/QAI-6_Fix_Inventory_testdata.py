import random
from datetime import datetime, timedelta
import string

# Generate test data for employees table with lastdate
def generate_employee_data(num_records):
    employee_data = []
    for _ in range(num_records):
        # Randomly decide if lastdate should be NULL or a valid date
        if random.choice([True, False]):
            lastdate = None  # Test condition: lastdate allows NULL values
        else:
            # Generate a random date within the last 10 years
            lastdate = datetime.now() - timedelta(days=random.randint(0, 3650))
            lastdate = lastdate.strftime('%Y-%m-%d')  # Test condition: lastdate is a valid DATE

        employee_data.append({
            "employee_id": random.randint(1, 1000),
            "lastdate": lastdate
        })
    return employee_data

# Generate test data for customers table with categoryGroup
def generate_customer_data(num_records):
    category_groups = ['Retail', 'Wholesale', 'Online', 'Corporate']  # Test condition: predefined category groups
    customer_data = []
    for _ in range(num_records):
        # Randomly decide if categoryGroup should be NULL or a valid category
        if random.choice([True, False]):
            category_group = None  # Test condition: categoryGroup allows NULL values
        else:
            category_group = random.choice(category_groups)  # Test condition: categoryGroup is a valid category

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
