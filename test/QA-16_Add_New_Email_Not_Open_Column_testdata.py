import random
import time
import pandas as pd

# Generate test data
def generate_test_data(num_records=30):
    data = []
    for _ in range(num_records):
        is_clicked = random.choice([True, False])
        is_opened = random.choice([True, False]) if is_clicked else False  # If not clicked, cannot be opened
        not_opened_email = is_clicked and not is_opened  # Condition: IS_CLICKED = TRUE and IS_OPENED = FALSE
        timestamp = int(time.time())  # Current time in seconds

        # Append the record to the data list
        data.append({
            'IS_CLICKED': is_clicked,
            'IS_OPENED': is_opened,
            'NOT_OPENED_EMAIL': not_opened_email,  # Validate NOT_OPENED_EMAIL logic
            '_timestamps_': timestamp  # Add _timestamps_ column
        })

    return pd.DataFrame(data)

# Generate and print the test data
test_data = generate_test_data()
print(test_data)
