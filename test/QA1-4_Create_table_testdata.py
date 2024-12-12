import random
import datetime

# Generate test data for employees table with lastdate column
def generate_employees_data(num_records):
    employees_data = []
    for _ in range(num_records):
        employee_id = random.randint(1, 1000)
        # Randomly choose to include a lastdate or not to test NULL condition
        if random.choice([True, False]):
            lastdate = datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))
        else:
            lastdate = None  # Test NULL condition for lastdate
        employees_data.append({
            "employee_id": employee_id,
            "lastdate": lastdate
        })
    return employees_data

# Generate test data for customers table with categoryGroup column
def generate_customers_data(num_records):
    category_options = ["VIP", "Regular", "New"]
    customers_data = []
    for _ in range(num_records):
        customer_id = random.randint(1, 1000)
        # Randomly choose to include a categoryGroup or not to test NULL condition
        if random.choice([True, False]):
            categoryGroup = random.choice(category_options)
        else:
            categoryGroup = None  # Test NULL condition for categoryGroup
        customers_data.append({
            "customer_id": customer_id,
            "categoryGroup": categoryGroup
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
