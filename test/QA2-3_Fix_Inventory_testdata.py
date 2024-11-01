import random
import string
import datetime

# Helper functions
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date(start_year=1990, end_year=2023):
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    return start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

def random_phone():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

# Generate test data for the employees table
employees_data = []
for _ in range(25):  # Generate 25 records
    employee = {
        "EmployeeID": random.randint(1, 1000),
        "LastName": random_string(8),
        "FirstName": random_string(8),
        "Title": random_string(10),
        "TitleOfCourtesy": random.choice(["Mr.", "Ms.", "Mrs.", "Dr."]),
        "BirthDate": random_date(),
        "HireDate": random_date(1990, 2022),
        "Address": random_string(15),
        "City": random_string(10),
        "Region": random_string(5),
        "PostalCode": random_string(6),
        "Country": random_string(10),
        "HomePhone": random_phone(),
        "Extension": str(random.randint(100, 999)),
        "Photo": b'\x00\x01\x02',  # Dummy binary data
        "Notes": random_string(20),
        "ReportsTo": random.randint(1, 100),
        "PhotoPath": random_string(20),
        # Validate the "lastdate" column with timestamp data type
        "LastDate": random_date(2000, 2023)
    }
    employees_data.append(employee)

# Generate test data for the customers table
customers_data = []
for _ in range(25):  # Generate 25 records
    customer = {
        "CustomerID": random_string(5),
        "CompanyName": random_string(12),
        "ContactName": random_string(8),
        "ContactTitle": random_string(10),
        "Address": random_string(15),
        "City": random_string(10),
        "Region": random_string(5),
        "PostalCode": random_string(6),
        "Country": random_string(10),
        "Phone": random_phone(),
        "Fax": random_phone(),
        # Validate the "categoryGroup" column with string data type
        "CategoryGroup": random.choice(["Retail", "Wholesale", "Online", "Direct"])
    }
    customers_data.append(customer)

# Test data output
print("Employees Test Data:")
for employee in employees_data:
    print(employee)

print("\nCustomers Test Data:")
for customer in customers_data:
    print(customer)
