import random
from datetime import datetime, timedelta
import string

# Generate random date
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Test data generation for qa.employees table including lastdate
employees_data = []

# Conditions:
# - lastdate should be a valid timestamp
# - lastdate should be the last working day of the employee
for i in range(20):
    employee = {
        "EmployeeID": i + 1,
        "LastName": ''.join(random.choices(string.ascii_uppercase, k=5)),
        "FirstName": ''.join(random.choices(string.ascii_uppercase, k=5)),
        "Title": "Title" + str(random.randint(1, 5)),
        "TitleOfCourtesy": random.choice(["Mr.", "Ms.", "Mrs.", "Dr."]),
        "BirthDate": random_date(datetime(1960, 1, 1), datetime(1990, 12, 31)),
        "HireDate": random_date(datetime(1990, 1, 1), datetime(2020, 12, 31)),
        "Address": "Address" + str(random.randint(1, 100)),
        "City": "City" + str(random.randint(1, 50)),
        "Region": "Region" + str(random.randint(1, 5)),
        "PostalCode": ''.join(random.choices(string.digits, k=5)),
        "Country": "Country" + str(random.randint(1, 10)),
        "HomePhone": ''.join(random.choices(string.digits, k=10)),
        "Extension": ''.join(random.choices(string.digits, k=4)),
        "Photo": b'',
        "Notes": "Notes" + str(random.randint(1, 10)),
        "ReportsTo": random.randint(1, 5),
        "PhotoPath": "Path" + str(random.randint(1, 10)),
        "LastDate": random_date(datetime(2021, 1, 1), datetime(2023, 12, 31))
    }
    employees_data.append(employee)

# Test data generation for qa.customers table including categoryGroup
customers_data = []

# Conditions:
# - categoryGroup should be a valid string representing the grouping category
for i in range(20):
    customer = {
        "CustomerID": i + 1,
        "CompanyName": "Company" + str(random.randint(1, 100)),
        "ContactName": "Contact" + str(random.randint(1, 100)),
        "ContactTitle": "ContactTitle" + str(random.randint(1, 10)),
        "Address": "Address" + str(random.randint(1, 100)),
        "City": "City" + str(random.randint(1, 50)),
        "Region": "Region" + str(random.randint(1, 5)),
        "PostalCode": ''.join(random.choices(string.digits, k=5)),
        "Country": "Country" + str(random.randint(1, 10)),
        "Phone": ''.join(random.choices(string.digits, k=10)),
        "Fax": ''.join(random.choices(string.digits, k=10)),
        "CategoryGroup": random.choice(["GroupA", "GroupB", "GroupC", "GroupD"])
    }
    customers_data.append(customer)

# Output data for verification
print("Employees Data:")
for emp in employees_data:
    print(emp)

print("\nCustomers Data:")
for cust in customers_data:
    print(cust)
