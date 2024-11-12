import random
import datetime
import string

# Generate random date between two dates
def random_date(start, end):
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))

# Generate random string of fixed length
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Test data generation for qa.employees table
employees_data = []
for i in range(25):
    employee = {
        "EmployeeID": i + 1,
        "LastName": random_string(8),
        "FirstName": random_string(6),
        "Title": random_string(10),
        "TitleOfCourtesy": random.choice(["Mr.", "Ms.", "Mrs.", "Dr."]),
        "BirthDate": random_date(datetime.date(1960, 1, 1), datetime.date(2000, 12, 31)),
        "HireDate": random_date(datetime.date(1990, 1, 1), datetime.date(2020, 12, 31)),
        "Address": random_string(15),
        "City": random_string(10),
        "Region": random_string(5),
        "PostalCode": ''.join(random.choices(string.digits, k=5)),
        "Country": random.choice(["USA", "Canada", "UK", "Australia"]),
        "HomePhone": ''.join(random.choices(string.digits, k=10)),
        "Extension": ''.join(random.choices(string.digits, k=4)),
        "Photo": b'\x00\x01',  # Placeholder binary data
        "Notes": random_string(20),
        "ReportsTo": random.randint(1, 5),
        "PhotoPath": f"/images/{random_string(5)}.jpg",
        # lastdate is nullable, so it can be None
        "lastdate": random.choice([random_date(datetime.date(2020, 1, 1), datetime.date(2023, 10, 1)), None])
    }
    employees_data.append(employee)

# Test data generation for qa.customers table
customers_data = []
for i in range(25):
    customer = {
        "CustomerID": i + 1,
        "CompanyName": random_string(12),
        "ContactName": random_string(10),
        "ContactTitle": random_string(8),
        "Address": random_string(15),
        "City": random_string(10),
        "Region": random_string(5),
        "PostalCode": ''.join(random.choices(string.digits, k=5)),
        "Country": random.choice(["USA", "Canada", "UK", "Australia"]),
        "Phone": ''.join(random.choices(string.digits, k=10)),
        "Fax": ''.join(random.choices(string.digits, k=10)),
        # categoryGroup is nullable, so it can be None
        "categoryGroup": random.choice(["Gold", "Silver", "Bronze", None])
    }
    customers_data.append(customer)

# Output the generated test data
print("Employees Test Data:")
for employee in employees_data:
    print(employee)

print("\nCustomers Test Data:")
for customer in customers_data:
    print(customer)
