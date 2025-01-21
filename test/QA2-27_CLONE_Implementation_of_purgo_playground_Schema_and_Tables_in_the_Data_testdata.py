import random
import string
from datetime import datetime, timedelta

# Helper functions
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_country_code():
    return random.choice(['US', 'CA', 'GB', 'FR', 'DE', 'JP', 'CN', 'IN', 'BR', 'AU'])

# Test Data Categories

# Happy path test data (valid, expected scenarios)
happy_path_data = [
    {
        "program_id": i,
        "program_name": f"Program {i}",
        "country_code": random_country_code(),
        "program_start_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1))
    }
    for i in range(1, 11)
]

# Edge case test data (boundary conditions)
edge_case_data = [
    {
        "program_id": 0,  # Minimum boundary for ID
        "program_name": "",  # Empty string for name
        "country_code": "ZZ",  # Non-existent country code
        "program_start_date": datetime(1970, 1, 1)  # Unix epoch start
    },
    {
        "program_id": 2**31-1,  # Maximum boundary for ID (assuming 32-bit integer)
        "program_name": random_string(256),  # Maximum length for name
        "country_code": "US",
        "program_start_date": datetime(9999, 12, 31)  # Far future date
    }
]

# Error case test data (invalid inputs)
error_case_data = [
    {
        "program_id": -1,  # Negative ID
        "program_name": None,  # Null name
        "country_code": "123",  # Numeric country code
        "program_start_date": "not-a-date"  # Invalid date format
    },
    {
        "program_id": "abc",  # Non-numeric ID
        "program_name": "Valid Name",
        "country_code": "USA",  # Invalid length for country code
        "program_start_date": None  # Null date
    }
]

# Special character and format test data
special_character_data = [
    {
        "program_id": 1001,
        "program_name": "Special!@#$%^&*()_+",
        "country_code": "UK",
        "program_start_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1))
    },
    {
        "program_id": 1002,
        "program_name": "Name with spaces",
        "country_code": "IN",
        "program_start_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1))
    }
]

# Combine all test data
test_data = happy_path_data + edge_case_data + error_case_data + special_character_data

# Output the test data
for data in test_data:
    print(data)
