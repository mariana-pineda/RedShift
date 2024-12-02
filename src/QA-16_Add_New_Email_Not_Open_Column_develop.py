import pandas as pd
import time

def add_columns_to_email_tracking(df):
    # Add NOT_OPENED_EMAIL column
    df['NOT_OPENED_EMAIL'] = df.apply(lambda row: row['IS_CLICKED'] and not row['IS_OPENED'], axis=1)
    
    # Add _timestamps_ column
    df['_timestamps_'] = int(time.time())
    
    return df

# Example usage
# Assuming df is your existing DataFrame with 'IS_CLICKED' and 'IS_OPENED' columns
# df = pd.DataFrame({'IS_CLICKED': [True, False, True], 'IS_OPENED': [False, False, True]})
# df = add_columns_to_email_tracking(df)
# print(df)
