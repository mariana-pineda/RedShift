import pandas as pd
import pytest
import numpy as np

# Sample data for testing
data = {
    "IS_CLICKED": [True, False, True, False, True],
    "IS_OPENED": [False, True, True, False, False]
}

expected_not_opened_email = [True, False, False, False, True]

# Test function to validate NOT_OPENED_EMAIL and timestep columns
def test_add_columns():
    df = pd.DataFrame(data)
    
    # Apply the logic to add the NOT_OPENED_EMAIL column
    df["NOT_OPENED_EMAIL"] = df.apply(
        lambda row: True if row["IS_CLICKED"] and not row["IS_OPENED"] else False, axis=1
    )
    
    # Assert each condition for NOT_OPENED_EMAIL
    assert df["NOT_OPENED_EMAIL"].tolist() == expected_not_opened_email
    
    # Applying the timestep logic to validate the addition of the column
    df["timestep"] = range(1, len(df) + 1)
    
    # Assert that timestep column is added correctly
    expected_timestep = list(range(1, len(df) + 1))
    assert df["timestep"].tolist() == expected_timestep

# If running through pytest, this would be automatically discovered and executed
if __name__ == "__main__":
    pytest.main([__file__])
