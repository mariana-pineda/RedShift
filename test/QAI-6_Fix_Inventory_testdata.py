import random
from datetime import datetime, timedelta
import string

# Generate random date within the past 10 years
def random_date():
    start_date = datetime.now() - timedelta(days=365*10)
    end_date = datetime.now()
    return start_date + (end_date - start_date) * random.random()

# Generate random string
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Test data for qa.employees table
employees_test_data = []
for _ in range(25):  # Generate 25 records
    employee = {
        "EmployeeID": random.randint(1, 1000),
        "LastName": random_string(5),
        "FirstName": random_string(5),
        "Title": random_string(10),
        "TitleOfCourtesy": random.choice(["Mr.", "Ms.", "Mrs.", "Dr."]),
        "BirthDate": random_date(),
        "HireDate": random_date(),
        "Address": random_string(15),
        "City": random_string(7),
        "Region": random_string(5),
        "PostalCode": random_string(6),
        "Country": random_string(7),
        "HomePhone": f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}",
        "Extension": random_string(4),
        "Photo": b'\x00\x01',
        "Notes": random_string(20),
        "ReportsTo": random.randint(1, 100),
        "PhotoPath": random_string(15),
        "lastdate": random_date() if random.choice([True, False]) else None  # Test nullable constraint
    }
    employees_test_data.append(employee)

# Test data for qa.customers table
customers_test_data = []
category_groups = ["Bronze", "Silver", "Gold", "Platinum"]
for _ in range(25):  # Generate 25 records
    customer = {
        "CustomerID": random.randint(1, 1000),
        "CompanyName": random_string(10),
        "ContactName": random_string(8),
        "ContactTitle": random_string(10),
        "Address": random_string(15),
        "City": random_string(7),
        "Region": random_string(5),
        "PostalCode": random_string(6),
        "Country": random_string(7),
        "Phone": f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}",
        "Fax": f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}",
        "categoryGroup": random.choice(category_groups) if random.choice([True, False]) else None  # Test nullable constraint
    }
    customers_test_data.append(customer)

# Print the generated test data
print("Employees Test Data:")
for data in employees_test_data:
    print(data)

print("\nCustomers Test Data:")
for data in customers_test_data:
    print(data)
