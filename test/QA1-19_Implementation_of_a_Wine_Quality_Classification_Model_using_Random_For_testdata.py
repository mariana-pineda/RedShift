import random
import string
import pandas as pd
from datetime import datetime, timedelta

# Helper functions
def random_date(start, end):
    """Generate a random date between start and end."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def random_boolean():
    """Generate a random boolean value."""
    return random.choice([True, False])

# Test Data Categories

# Happy path test data (valid, expected scenarios)
happy_path_data = [
    {
        "order_nbr": random_string(10),
        "order_type": random.randint(1, 5),
        "delivery_dt": int(random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime('%Y%m%d')),
        "order_qty": round(random.uniform(1.0, 100.0), 2),
        "sched_dt": int(random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime('%Y%m%d')),
        "flag_return": random_boolean(),
        "flag_cancel": random_boolean()
    } for _ in range(10)
]

# Edge case test data (boundary conditions)
edge_case_data = [
    {
        "order_nbr": random_string(256),  # Max length for order_nbr
        "order_type": 0,  # Minimum valid order type
        "delivery_dt": 20230101,  # Earliest valid date
        "order_qty": 0.0,  # Minimum valid quantity
        "sched_dt": 20231231,  # Latest valid date
        "flag_return": False,
        "flag_cancel": False
    },
    {
        "order_nbr": random_string(256),
        "order_type": 9999999999,  # Hypothetical maximum order type
        "delivery_dt": 20231231,
        "order_qty": 999999.99,  # Hypothetical maximum quantity
        "sched_dt": 20230101,
        "flag_return": True,
        "flag_cancel": True
    }
]

# Error case test data (invalid inputs)
error_case_data = [
    {
        "order_nbr": "",  # Invalid empty string
        "order_type": -1,  # Invalid negative order type
        "delivery_dt": 20231301,  # Invalid date
        "order_qty": -10.0,  # Invalid negative quantity
        "sched_dt": 20231301,  # Invalid date
        "flag_return": "yes",  # Invalid boolean
        "flag_cancel": "no"  # Invalid boolean
    }
]

# Special character and format test data
special_char_data = [
    {
        "order_nbr": "!@#$%^&*()",  # Special characters
        "order_type": 1,
        "delivery_dt": 20230101,
        "order_qty": 50.0,
        "sched_dt": 20230101,
        "flag_return": False,
        "flag_cancel": False
    },
    {
        "order_nbr": "1234567890",
        "order_type": 2,
        "delivery_dt": 20231231,
        "order_qty": 75.5,
        "sched_dt": 20231231,
        "flag_return": True,
        "flag_cancel": True
    }
]

# Combine all test data
test_data = happy_path_data + edge_case_data + error_case_data + special_char_data

# Convert to DataFrame for easier manipulation and export
df_test_data = pd.DataFrame(test_data)

# Output the test data
print(df_test_data)


This code generates test data for a hypothetical `f_order` table, covering happy path, edge cases, error cases, and special character scenarios. The data is structured to include a variety of scenarios for each field, ensuring comprehensive coverage of potential inputs.