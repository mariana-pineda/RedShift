import random
from datetime import datetime

# Test data generation for qa.employees with lastdate column

# Function to generate random date
def random_date():
    return datetime.now().strftime('%Y-%m-%d')

# Employee data records with lastdate added
employees_data = [
    {
        "EmployeeID": i,
        "LastName": f"LastName{i}",
        "FirstName": f"FirstName{i}",
        "Title": "Title",
        "TitleOfCourtesy": "Mr.",
        "BirthDate": "1970-01-01 00:00:00",
        "HireDate": "2000-01-01 00:00:00",
        "Address": f"Address{i}",
        "City": "City",
        "Region": "Region",
        "PostalCode": "12345",
        "Country": "Country",
        "HomePhone": "123-456-7890",
        "Extension": "1234",
        "Photo": None,
        "Notes": "Notes",
        "ReportsTo": 1,
        "PhotoPath": "/path/to/photo",
        # Validating lastdate default value as current date
        "LastDate": random_date()
    }
    for i in range(20)
]

# Test data generation for qa.customers with categoryGroup column

# Predefined categories
categories = ["VIP", "Regular", "New", "Uncategorized"]

# Function to generate random category
def random_category():
    return random.choice(["VIP", "Regular", "New"])

# Customer data records with categoryGroup added
customers_data = [
    {
        "CustomerID": i,
        "CustomerName": f"CustomerName{i}",
        "ContactName": f"ContactName{i}",
        "Country": "Country",
        # Validating predefined categories and default Uncategorized
        "CategoryGroup": random_category() if i < 15 else "Uncategorized"
    }
    for i in range(30)
]

# Print generated test data
print(employees_data)
print(customers_data)
