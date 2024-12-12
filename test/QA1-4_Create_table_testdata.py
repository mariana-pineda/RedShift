import random
import datetime

# Generate test data for employees table with lastdate column
def generate_employees_data(num_records):
    employees_data = []
    for _ in range(num_records):
        # Generate random employee ID
        employee_id = random.randint(1, 1000)
        
        # Generate random lastdate (validate date format and range)
        lastdate = datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))
        
        # Append to employees data list
        employees_data.append({
            "employee_id": employee_id,
            "lastdate": lastdate
        })
    
    # Add test case for NULL lastdate (validate NULL handling)
    employees_data.append({
        "employee_id": random.randint(1001, 1100),
        "lastdate": None
    })
    
    return employees_data

# Generate test data for customers table with categoryGroup column
def generate_customers_data(num_records):
    category_groups = ["VIP", "Regular", "New"]
    customers_data = []
    for _ in range(num_records):
        # Generate random customer ID
        customer_id = random.randint(1, 1000)
        
        # Randomly assign a category group (validate predefined categories)
        category_group = random.choice(category_groups)
        
        # Append to customers data list
        customers_data.append({
            "customer_id": customer_id,
            "categoryGroup": category_group
        })
    
    # Add test case for NULL categoryGroup (validate NULL handling)
    customers_data.append({
        "customer_id": random.randint(1001, 1100),
        "categoryGroup": None
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
