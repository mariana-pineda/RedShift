import random
from datetime import datetime, timedelta

# Predefined categories for categoryGroup
category_options = ["VIP", "Regular", "New", "Uncategorized"]

# Generate test data for employees table
employees_data = []
for i in range(20):
    employee = {
        "EmployeeID": i + 1,
        "LastName": f"LastName{i+1}",
        "FirstName": f"FirstName{i+1}",
        "Title": "Title",
        "TitleOfCourtesy": "Mr.",
        "BirthDate": datetime.now() - timedelta(days=random.randint(7000, 20000)),
        "HireDate": datetime.now() - timedelta(days=random.randint(1000, 7000)),
        "Address": f"Address {i+1}",
        "City": "City",
        "Region": "Region",
        "PostalCode": f"{10000 + i}",
        "Country": "Country",
        "HomePhone": f"(555) 000-{1000 + i}",
        "Extension": f"{100 + i}",
        "Photo": None,
        "Notes": "Notes",
        "ReportsTo": random.randint(1, 10),
        "PhotoPath": "Path",
        # Validate lastdate is of date type and default value is current date
        "lastdate": datetime.now().date()  # Default to current date
    }
    employees_data.append(employee)

# Generate test data for customers table
customers_data = []
for i in range(30):
    customer = {
        "CustomerID": i + 1,
        "CompanyName": f"CompanyName{i+1}",
        "ContactName": f"ContactName{i+1}",
        "ContactTitle": "ContactTitle",
        "Address": f"Address {i+1}",
        "City": "City",
        "Region": "Region",
        "PostalCode": f"{10000 + i}",
        "Country": "Country",
        "Phone": f"(555) 000-{1000 + i}",
        "Fax": f"(555) 000-{2000 + i}",
        # Validate categoryGroup is a string type with predefined categories
        "categoryGroup": random.choice(category_options)  # Ensure it only contains valid categories
    }
    customers_data.append(customer)

# Output the generated data (for verification, not part of the generation code)
print("Employees Data:")
for emp in employees_data:
    print(emp)

print("\nCustomers Data:")
for cust in customers_data:
    print(cust)
