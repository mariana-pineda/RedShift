import pandas as pd
from datetime import datetime

def add_not_opened_email_column(df):
    # Add NOT_OPENED_EMAIL and TIMESTAMP columns with default values
    df['NOT_OPENED_EMAIL'] = False
    df['TIMESTAMP'] = None
    
    # Update values where IS_CLICKED is True and IS_OPENED is False
    mask = (df['IS_CLICKED'] == True) & (df['IS_OPENED'] == False)
    df.loc[mask, 'NOT_OPENED_EMAIL'] = True
    df.loc[mask, 'TIMESTAMP'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return df

# Sample DataFrame creation
data = {
    'IS_CLICKED': [True, False, True, False],
    'IS_OPENED': [False, False, True, False]
}
df = pd.DataFrame(data)

# Apply function to add columns
df = add_not_opened_email_column(df)

# Display the updated DataFrame
print(df)
