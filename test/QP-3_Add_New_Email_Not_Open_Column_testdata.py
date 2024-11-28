import pandas as pd
import numpy as np

# Generating test data for the email dataset
# This will create a DataFrame with 30 records to test every condition

# Function to generate random boolean values
def random_bool():
    return np.random.choice([True, False])

# Creating the initial dataset with IS_CLICKED and IS_OPENED columns
np.random.seed(0)  # For reproducibility
data = {
    "IS_CLICKED": [random_bool() for _ in range(30)],
    "IS_OPENED": [random_bool() for _ in range(30)]
}

df = pd.DataFrame(data)

# Adding the NOT_OPENED_EMAIL column based on conditions
# Condition 1: IS_CLICKED is True and IS_OPENED is False
df["NOT_OPENED_EMAIL"] = df.apply(
    lambda row: True if row["IS_CLICKED"] and not row["IS_OPENED"] else False, axis=1
)

# Adding the timestep column to the dataset.
# Assuming timestep is a sequential number for simplicity.
df["timestep"] = range(1, len(df) + 1)

# Display the generated dataset to validate test data
df
