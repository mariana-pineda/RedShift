import pandas as pd
import time

def add_columns_to_dataframe(df):
    # Add NOT_OPENED_EMAIL column
    df['NOT_OPENED_EMAIL'] = df.apply(lambda row: row['IS_CLICKED'] and not row['IS_OPENED'], axis=1)
    
    # Add _timestamps_ column
    df['_timestamps_'] = int(time.time())
    
    return df

# Example usage
data = {
    'IS_CLICKED': [True, False, True, True],
    'IS_OPENED': [False, False, True, False]
}

df = pd.DataFrame(data)
df = add_columns_to_dataframe(df)
print(df)
