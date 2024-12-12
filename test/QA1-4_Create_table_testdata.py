import random
import datetime

# Generate test data for employees table with lastdate column
def generate_employees_data(num_records):
    employees_data = []
    for _ in range(num_records):
        employee_id = random.randint(1, 1000)
        # Assuming lastdate is a date type, generating random dates
        lastdate = datetime.date(2023, random.randint(1, 12), random.randint(1, 28))
        employees_data.append({
            "employee_id": employee_id,
            "lastdate": lastdate
        })
    return employees_data

# Generate test data for customers table with categoryGroup column
def generate_customers_data(num_records):
    category_groups = ['A', 'B', 'C', 'D']  # Assuming categoryGroup is a string type
    customers_data = []
    for _ in range(num_records):
        customer_id = random.randint(1, 1000)
        category_group = random.choice(category_groups)
        customers_data.append({
            "customer_id": customer_id,
            "categoryGroup": category_group
        })
    return customers_data

# Generate 20-30 records for each table
employees_test_data = generate_employees_data(25)  # Validating default value and presence of lastdate
customers_test_data = generate_customers_data(25)  # Validating default value and presence of categoryGroup

# Output the generated test data
print("Employees Test Data:")
for record in employees_test_data:
    print(record)

print("\nCustomers Test Data:")
for record in customers_test_data:
    print(record)
