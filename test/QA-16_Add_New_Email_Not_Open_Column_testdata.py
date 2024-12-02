import random
import pandas as pd

# Function to generate test data
def generate_test_data(num_records):
    data = []
    for _ in range(num_records):
        is_clicked = random.choice([True, False, None])  # Randomly choose True, False, or None
        is_opened = random.choice([True, False, None])   # Randomly choose True, False, or None

        # Condition: Mark email as not opened when clicked but not opened
        if is_clicked == True and is_opened == False:
            not_opened_email = True
        # Condition: Do not mark email as not opened when not clicked
        elif is_clicked == False:
            not_opened_email = False
        # Condition: Do not mark email as not opened when opened
        elif is_opened == True:
            not_opened_email = False
        # Condition: Handle null or missing values in IS_CLICKED or IS_OPENED
        elif is_clicked is None or is_opened is None:
            not_opened_email = False
        # Condition: Handle both IS_CLICKED and IS_OPENED as false
        elif is_clicked == False and is_opened == False:
            not_opened_email = False
        else:
            not_opened_email = False  # Default case

        data.append({
            "IS_CLICKED": is_clicked,
            "IS_OPENED": is_opened,
            "NOT_OPENED_EMAIL": not_opened_email
        })
    
    return pd.DataFrame(data)

# Generate 20-30 records
test_data = generate_test_data(25)
print(test_data)
