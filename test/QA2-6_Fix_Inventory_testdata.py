import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Test Data Categories

# Happy path test data (valid, expected scenarios)
# Employees with valid lastdate
happy_path_employees = [
    {"employee_id": 1, "lastdate": datetime.now().date()},
    {"employee_id": 2, "lastdate": datetime.now().date() - timedelta(days=1)},
    {"employee_id": 3, "lastdate": datetime.now().date() - timedelta(days=30)},
]

# Customers with valid categoryGroup
happy_path_customers = [
    {"customer_id": 1, "categoryGroup": "VIP"},
    {"customer_id": 2, "categoryGroup": "Regular"},
    {"customer_id": 3, "categoryGroup": "New"},
]

# Edge case test data (boundary conditions)
# Employees with boundary lastdate values
edge_case_employees = [
    {"employee_id": 4, "lastdate": datetime(1970, 1, 1).date()},  # Unix epoch start
    {"employee_id": 5, "lastdate": datetime(9999, 12, 31).date()},  # Far future date
]

# Customers with boundary categoryGroup values
edge_case_customers = [
    {"customer_id": 4, "categoryGroup": "Uncategorized"},  # Default value
]

# Error case test data (invalid inputs)
# Employees with invalid lastdate
error_case_employees = [
    {"employee_id": 6, "lastdate": "invalid_date"},  # Invalid date format
    {"employee_id": 7, "lastdate": None},  # Null value
]

# Customers with invalid categoryGroup
error_case_customers = [
    {"customer_id": 5, "categoryGroup": "InvalidCategory"},  # Not a predefined category
    {"customer_id": 6, "categoryGroup": ""},  # Empty string
]

# Special character and format test data
# Employees with special character handling in lastdate
special_char_employees = [
    {"employee_id": 8, "lastdate": "2023-02-29"},  # Non-leap year date
]

# Customers with special character handling in categoryGroup
special_char_customers = [
    {"customer_id": 7, "categoryGroup": "VIP\n"},  # Newline character
    {"customer_id": 8, "categoryGroup": "Regular\t"},  # Tab character
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

