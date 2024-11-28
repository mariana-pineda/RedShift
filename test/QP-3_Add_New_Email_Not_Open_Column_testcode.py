import pandas as pd
import numpy as np

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

# Expected values based on conditions
expected_not_opened_email = df.apply(
    lambda row: True if row["IS_CLICKED"] and not row["IS_OPENED"] else False, axis=1
)
expected_timestep = list(range(1, len(df) + 1))

# Adding the NOT_OPENED_EMAIL column based on conditions
df["NOT_OPENED_EMAIL"] = df.apply(
    lambda row: True if row["IS_CLICKED"] and not row["IS_OPENED"] else False, axis=1
)

# Adding the timestep column to the dataset
df["timestep"] = range(1, len(df) + 1)

# Validation
not_opened_email_test = (df["NOT_OPENED_EMAIL"] == expected_not_opened_email).all()
timestep_test = (df["timestep"] == expected_timestep).all()

print(f"NOT_OPENED_EMAIL column validation: {'Passed' if not_opened_email_test else 'Failed'}")
print(f"Timestep column validation: {'Passed' if timestep_test else 'Failed'}")

