import random
import pandas as pd

# Generate test data with 'IS_CLICKED' and 'IS_OPENED' columns
def generate_test_data(num_records):
    data = []
    for _ in range(num_records):
        is_clicked = random.choice([True, False])
        # Conditions for IS_OPENED to ensure diverse data set while being logical
        # If clicked, then it can be opened or not, if not clicked then obviously not opened
        is_opened = random.choice([True, False]) if is_clicked else False
        not_opened_email = is_clicked and not is_opened  # Validating condition for NOT_OPENED_EMAIL
        data.append({'IS_CLICKED': is_clicked, 'IS_OPENED': is_opened, 'NOT_OPENED_EMAIL': not_opened_email})
    return pd.DataFrame(data)

# Generate 25 records
test_data_df = generate_test_data(25)

# Output the test data
print(test_data_df)

