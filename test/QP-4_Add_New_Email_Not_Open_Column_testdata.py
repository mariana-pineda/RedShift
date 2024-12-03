import random
from datetime import datetime, timedelta

# Function to generate test dataset
def generate_test_data(num_records=30):
    test_data = []
    
    for _ in range(num_records):
        # Randomly determine IS_CLICKED and IS_OPENED status
        is_clicked = random.choice([True, False])
        is_opened = random.choice([True, False])
        
        # Determine NOT_OPENED_EMAIL based on conditions
        not_opened_email = False
        timestamp = None
        
        # Validate Scenario: Update record when IS_CLICKED is TRUE and IS_OPENED is FALSE
        if is_clicked and not is_opened:
            not_opened_email = True
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Validate Scenario: Handle records where both IS_CLICKED and IS_OPENED are FALSE
        # Timestamp should remain as None if both are False

        # Add default value logic for NOT_OPENED_EMAIL if required
        # Validate Scenario: Newly added columns default behavior for existing records
        
        # Append the generated data to the list
        test_data.append({
            "IS_CLICKED": is_clicked,
            "IS_OPENED": is_opened,
            "NOT_OPENED_EMAIL": not_opened_email,
            "TIMESTAMP": timestamp
        })
    
    return test_data

# Generate 30 data records
test_dataset = generate_test_data(30)

# Display the generated test dataset
for record in test_dataset:
    print(record)
