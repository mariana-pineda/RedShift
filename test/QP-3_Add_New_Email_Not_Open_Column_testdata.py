import pandas as pd
import numpy as np

# Generate random test data
np.random.seed(42)  # For reproducibility
num_records = 30

# Create a DataFrame with 'IS_CLICKED' and 'IS_OPENED' columns
data = {
    'IS_CLICKED': np.random.choice([True, False], num_records),
    'IS_OPENED': np.random.choice([True, False], num_records)
}

df = pd.DataFrame(data)

# Scenario: Add NOT_OPENED_EMAIL column for emails that have been clicked but not opened
df['NOT_OPENED_EMAIL'] = np.where((df['IS_CLICKED'] == True) & (df['IS_OPENED'] == False), True, False)
# Explanation: Marks email as not opened when it is clicked but not opened

# Scenario: Adding timestep column to the email dataset
df['timestep'] = range(1, num_records + 1)
# Explanation: Add timestep column with incremental values to track changes

print(df)


This script generates a DataFrame with random test data to validate the conditions mentioned in the user story. The `NOT_OPENED_EMAIL` column is computed based on the logic: emails that have been clicked but not opened are marked as True. Additionally, a `timestep` column is added to the dataset to simulate a progression or order of records.