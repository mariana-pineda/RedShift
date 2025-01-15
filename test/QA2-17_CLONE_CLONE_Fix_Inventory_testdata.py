import random
import datetime

# Test Data Generation for Employees Table
# Happy Path Test Data: Valid scenarios for 'lastdate' column
happy_path_employees = [
    {"EmployeeID": 1, "LastName": "Smith", "FirstName": "John", "lastdate": datetime.date.today()},
    {"EmployeeID": 2, "LastName": "Doe", "FirstName": "Jane", "lastdate": datetime.date.today()},
    {"EmployeeID": 3, "LastName": "Brown", "FirstName": "Charlie", "lastdate": datetime.date.today()},
]

# Edge Case Test Data: Boundary conditions for 'lastdate' column
edge_case_employees = [
    {"EmployeeID": 4, "LastName": "Edge", "FirstName": "Case", "lastdate": datetime.date(1900, 1, 1)},  # Oldest possible date
    {"EmployeeID": 5, "LastName": "Future", "FirstName": "Date", "lastdate": datetime.date(9999, 12, 31)},  # Farthest future date
]

# Error Case Test Data: Invalid inputs for 'lastdate' column
error_case_employees = [
    {"EmployeeID": 6, "LastName": "Invalid", "FirstName": "Date", "lastdate": "NotADate"},  # Invalid date format
    {"EmployeeID": 7, "LastName": "Null", "FirstName": "Value", "lastdate": None},  # Null value
]

# Special Character and Format Test Data: Special characters in names
special_char_employees = [
    {"EmployeeID": 8, "LastName": "O'Neil", "FirstName": "Shaun", "lastdate": datetime.date.today()},
    {"EmployeeID": 9, "LastName": "Smith-Jones", "FirstName": "Anna", "lastdate": datetime.date.today()},
]

# Test Data Generation for Customers Table
# Happy Path Test Data: Valid scenarios for 'categoryGroup' column
happy_path_customers = [
    {"CustomerID": "C001", "CompanyName": "Acme Corp", "categoryGroup": "VIP"},
    {"CustomerID": "C002", "CompanyName": "Beta Inc", "categoryGroup": "Regular"},
    {"CustomerID": "C003", "CompanyName": "Gamma LLC", "categoryGroup": "New"},
]

# Edge Case Test Data: Boundary conditions for 'categoryGroup' column
edge_case_customers = [
    {"CustomerID": "C004", "CompanyName": "Delta Co", "categoryGroup": "Uncategorized"},  # Default value
]

# Error Case Test Data: Invalid inputs for 'categoryGroup' column
error_case_customers = [
    {"CustomerID": "C005", "CompanyName": "Epsilon Ltd", "categoryGroup": "InvalidCategory"},  # Invalid category
    {"CustomerID": "C006", "CompanyName": "Zeta Group", "categoryGroup": None},  # Null value
]

# Special Character and Format Test Data: Special characters in company names
special_char_customers = [
    {"CustomerID": "C007", "CompanyName": "O'Reilly Media", "categoryGroup": "Regular"},
    {"CustomerID": "C008", "CompanyName": "Smith & Sons", "categoryGroup": "VIP"},
]

# Combine all test data
all_test_data = {
    "employees": happy_path_employees + edge_case_employees + error_case_employees + special_char_employees,
    "customers": happy_path_customers + edge_case_customers + error_case_customers + special_char_customers
}

# Output the test data
print(all_test_data)


This code generates test data for the `employees` and `customers` tables, covering happy path, edge cases, error cases, and special character scenarios. Each test case is designed to validate the new columns `lastdate` and `categoryGroup` according to the specified requirements.