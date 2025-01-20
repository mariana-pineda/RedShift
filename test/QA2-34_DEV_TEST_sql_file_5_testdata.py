import random
import string
from datetime import datetime, timedelta

# Helper functions
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_timestamp():
    return datetime.now() - timedelta(days=random.randint(0, 365))

# Test Data Categories

# Happy path test data
happy_path_data = [
    {
        "program_id": random.randint(1, 1000),
        "program_name": random_string(15),
        "country_code": random_string(3),
        "program_start_date": random_timestamp()
    } for _ in range(10)
]

# Edge case test data
edge_case_data = [
    {
        "program_id": 0,  # Minimum boundary for ID
        "program_name": "",  # Empty string for name
        "country_code": "ZZZ",  # Uncommon country code
        "program_start_date": datetime(1970, 1, 1)  # Epoch time
    },
    {
        "program_id": 2147483647,  # Maximum boundary for INT
        "program_name": random_string(256),  # Maximum length for VARCHAR
        "country_code": "US",  # Common country code
        "program_start_date": datetime(9999, 12, 31)  # Far future date
    }
]

# Error case test data
error_case_data = [
    {
        "program_id": -1,  # Invalid negative ID
        "program_name": None,  # None value for name
        "country_code": "123",  # Numeric country code
        "program_start_date": "InvalidDate"  # Invalid date format
    },
    {
        "program_id": "ABC",  # Non-numeric ID
        "program_name": random_string(10),
        "country_code": "",  # Empty country code
        "program_start_date": None  # None value for date
    }
]

# Special character and format test data
special_character_data = [
    {
        "program_id": random.randint(1, 1000),
        "program_name": "Special!@#$%^&*()",
        "country_code": "UK",
        "program_start_date": random_timestamp()
    },
    {
        "program_id": random.randint(1, 1000),
        "program_name": "NameWith\nNewLine",
        "country_code": "FR",
        "program_start_date": random_timestamp()
    }
]

# Combine all test data
test_data = happy_path_data + edge_case_data + error_case_data + special_character_data

# Output the test data
for record in test_data:
    print(record)


This code generates test data for a hypothetical database table `programs` with fields `program_id`, `program_name`, `country_code`, and `program_start_date`. It includes happy path, edge case, error case, and special character test data.