import pandas as pd

def add_columns_to_email_dataset(df):
    # Add NOT_OPENED_EMAIL column based on conditions
    df["NOT_OPENED_EMAIL"] = df.apply(
        lambda row: True if row["IS_CLICKED"] and not row["IS_OPENED"] else False, axis=1
    )

    # Add timestep column to the dataset
    df["timestep"] = range(1, len(df) + 1)

    return df
