import random
from datetime import datetime, timedelta
import string

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_employee_data(num_records):
    employees = []
    for _ in range(num_records):
        employee = {
            "EmployeeID": random.randint(1, 1000),
            "LastName": random_string(5),
            "FirstName": random_string(5),
            "Title": random.choice(["Manager", "Developer", "Analyst"]),
            "TitleOfCourtesy": random.choice(["Mr.", "Ms.", "Dr."]),
            "BirthDate": random_date(datetime(1950, 1, 1), datetime(2000, 12, 31)),
            "HireDate": random_date(datetime(2005, 1, 1), datetime(2023, 1, 1)),
            "Address": random_string(15),
            "City": random_string(10),
            "Region": random.choice(["East", "West", "North", "South"]),
            "PostalCode": random_string(5),
            "Country": random.choice(["USA", "Canada", "UK"]),
            "HomePhone": random_string(10),
            "Extension": random_string(4),
            "Photo": b'',
            "Notes": random_string(20),
            "ReportsTo": random.randint(1, 10),
            "PhotoPath": random_string(10),
            # Validate lastdate allows null values and is of type timestamp
            "LastDate": random.choice([random_date(datetime(2021, 1, 1), datetime(2023, 1, 1)), None])
        }
        employees.append(employee)
    return employees

def generate_customer_data(num_records):
    customers = []
    for _ in range(num_records):
        customer = {
            # Existing customer columns would be here
            # Validate categoryGroup allows null values and is of type string
            "CategoryGroup": random.choice([random_string(8), None])
        }
        customers.append(customer)
    return customers

# Generate test data
employee_data = generate_employee_data(25)
customer_data = generate_customer_data(25)

# Output the data if needed
#print(employee_data)
#print(customer_data)
