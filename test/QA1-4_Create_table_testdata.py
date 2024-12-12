import random
import datetime

# Generate test data for employees table with lastdate column
def generate_employees_data(num_records):
    employees_data = []
    for _ in range(num_records):
        # Generate random employee id
        employee_id = random.randint(1, 1000)
        
        # Generate random lastdate, allowing for potential NULL values
        if random.choice([True, False]):
            lastdate = None  # Testing condition where lastdate is NULL
        else:
            lastdate = datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))
        
        employees_data.append({
            "employee_id": employee_id,
            "lastdate": lastdate
        })
    return employees_data

# Generate test data for customers table with categoryGroup column
def generate_customers_data(num_records):
    customers_data = []
    category_groups = ["VIP", "Regular", "New"]  # Predefined categories
    
    for _ in range(num_records):
        # Generate random customer id
        customer_id = random.randint(1, 1000)
        
        # Randomly assign a category group, allowing for potential NULL values
        if random.choice([True, False]):
            category_group = None  # Testing condition where categoryGroup is NULL
        else:
            category_group = random.choice(category_groups)
        
        customers_data.append({
            "customer_id": customer_id,
            "categoryGroup": category_group
        })
    return customers_data

# Generate 20-30 records for each table
employees_test_data = generate_employees_data(25)
customers_test_data = generate_customers_data(25)

# Print the generated test data
print("Employees Test Data:")
for record in employees_test_data:
    print(record)

print("\nCustomers Test Data:")
for record in customers_test_data:
    print(record)
