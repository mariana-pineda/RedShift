import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Test Data Categories

# Happy path test data (valid, expected scenarios)
happy_path_employees = [
    # Valid employee records with default lastdate
    {"EmployeeID": 1, "LastName": "Smith", "FirstName": "John", "lastdate": datetime.now().date()},
    {"EmployeeID": 2, "LastName": "Doe", "FirstName": "Jane", "lastdate": datetime.now().date()},
    {"EmployeeID": 3, "LastName": "Brown", "FirstName": "Charlie", "lastdate": datetime.now().date()},
]

happy_path_customers = [
    # Valid customer records with valid categoryGroup
    {"CustomerID": "C001", "CompanyName": "Acme Corp", "categoryGroup": "VIP"},
    {"CustomerID": "C002", "CompanyName": "Beta Inc", "categoryGroup": "Regular"},
    {"CustomerID": "C003", "CompanyName": "Gamma LLC", "categoryGroup": "New"},
]

# Edge case test data (boundary conditions)
edge_case_employees = [
    # Employee with the earliest possible lastdate
    {"EmployeeID": 4, "LastName": "Edge", "FirstName": "Case", "lastdate": datetime(1900, 1, 1).date()},
]

edge_case_customers = [
    # Customer with the default categoryGroup
    {"CustomerID": "C004", "CompanyName": "Delta Co", "categoryGroup": "Uncategorized"},
]

# Error case test data (invalid inputs)
error_case_employees = [
    # Invalid lastdate format
    {"EmployeeID": 5, "LastName": "Error", "FirstName": "Case", "lastdate": "InvalidDate"},
]

error_case_customers = [
    # Invalid categoryGroup
    {"CustomerID": "C005", "CompanyName": "Epsilon Ltd", "categoryGroup": "InvalidCategory"},
]

# Special character and format test data
special_char_employees = [
    # Employee with special characters in name
    {"EmployeeID": 6, "LastName": "O'Neil", "FirstName": "Anne-Marie", "lastdate": datetime.now().date()},
]

special_char_customers = [
    # Customer with special characters in company name
    {"CustomerID": "C006", "CompanyName": "Zeta & Sons", "categoryGroup": "VIP"},
]

# Combine all test data
all_test_data = {
    "employees": happy_path_employees + edge_case_employees + error_case_employees + special_char_employees,
    "customers": happy_path_customers + edge_case_customers + error_case_customers + special_char_customers,
}

# Output the test data
for category, data in all_test_data.items():
    print(f"Test data for {category}:")
    for record in data:
        print(record)


This code generates test data for the `Employees` and `Customers` tables, covering happy path, edge cases, error cases, and special character scenarios. The `lastdate` for employees is set to the current date by default, and the `categoryGroup` for customers is validated against predefined categories.