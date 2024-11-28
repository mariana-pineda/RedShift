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

# Scenario: Adding timestep column to the email dataset
df['timestep'] = range(1, num_records + 1)

print(df)
