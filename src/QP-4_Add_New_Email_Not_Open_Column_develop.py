import pandas as pd
from datetime import datetime

def add_not_opened_email_and_timestamp(df):
    df['NOT_OPENED_EMAIL'] = df.apply(lambda row: row['IS_CLICKED'] and not row['IS_OPENED'], axis=1)
    df['TIMESTAMP'] = df.apply(lambda row: datetime.now().strftime("%Y-%m-%d %H:%M:%S") if row['NOT_OPENED_EMAIL'] else None, axis=1)
    return df

# Example usage, assuming df is your DataFrame
# df = pd.DataFrame({
#     'IS_CLICKED': [True, False, True, False],
#     'IS_OPENED': [False, False, True, False]
# })
# df = add_not_opened_email_and_timestamp(df)
