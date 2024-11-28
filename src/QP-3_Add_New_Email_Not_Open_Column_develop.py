import pandas as pd
import numpy as np

# Function to generate random boolean values
def random_bool():
    return np.random.choice([True, False])

# Initial dataset creation with IS_CLICKED and IS_OPENED columns
np.random.seed(0)  # For reproducibility
data = {
    "IS_CLICKED": [random_bool() for _ in range(30)],
    "IS_OPENED": [random_bool() for _ in range(30)]
}

df = pd.DataFrame(data)

# Adding the NOT_OPENED_EMAIL column based on conditions
df["NOT_OPENED_EMAIL"] = df.apply(
    lambda row: row["IS_CLICKED"] and not row["IS_OPENED"], axis=1
)

# Adding the timestep column to the dataset
df["timestep"] = range(1, len(df) + 1)

# Display the dataset
print(df)

