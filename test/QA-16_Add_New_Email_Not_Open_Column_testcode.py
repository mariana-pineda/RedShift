import pandas as pd

# Function to validate the NOT_OPENED_EMAIL column
def validate_not_opened_email(test_data):
    for index, row in test_data.iterrows():
        is_clicked = row['IS_CLICKED']
        is_opened = row['IS_OPENED']
        expected_not_opened_email = row['NOT_OPENED_EMAIL']

        # Determine the expected value based on the conditions
        if is_clicked == True and is_opened == False:
            expected_value = True
        else:
            expected_value = False

        # Compare expected and actual values
        assert expected_not_opened_email == expected_value, (
            f"Row {index} failed: IS_CLICKED={is_clicked}, IS_OPENED={is_opened}, "
            f"Expected NOT_OPENED_EMAIL={expected_value}, "
            f"Actual NOT_OPENED_EMAIL={expected_not_opened_email}"
        )

# Validate the test data
validate_not_opened_email(test_data)
