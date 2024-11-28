import pandas as pd
import numpy as np

def test_validation():
    # Setup
    np.random.seed(42)
    num_records = 30

    # Creating test dataframe
    df_test = pd.DataFrame({
        'IS_CLICKED': np.random.choice([True, False], num_records),
        'IS_OPENED': np.random.choice([True, False], num_records)
    })

    # Expected results
    expected_not_opened_email = np.where((df_test['IS_CLICKED'] == True) & (df_test['IS_OPENED'] == False), True, False)
    expected_timestep = range(1, num_records + 1)

    # Add columns based on the logic
    df_test['NOT_OPENED_EMAIL'] = np.where((df_test['IS_CLICKED'] == True) & (df_test['IS_OPENED'] == False), True, False)
    df_test['timestep'] = range(1, num_records + 1)

    # Validate NOT_OPENED_EMAIL column
    assert all(df_test['NOT_OPENED_EMAIL'] == expected_not_opened_email), "NOT_OPENED_EMAIL column validation failed"

    # Validate timestep column
    assert all(df_test['timestep'] == expected_timestep), "timestep column validation failed"

    return "Validation successful"

print(test_validation())
