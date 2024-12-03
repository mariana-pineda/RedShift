import random
from datetime import datetime

def update_dataset_with_not_opened_email(dataset):
    for record in dataset:
        not_opened_email = False
        timestamp = None
        
        if record['IS_CLICKED'] and not record['IS_OPENED']:
            not_opened_email = True
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        record["NOT_OPENED_EMAIL"] = not_opened_email
        record["TIMESTAMP"] = timestamp
    
    return dataset

# Sample dataset to apply the logic
sample_dataset = [
    {"IS_CLICKED": True, "IS_OPENED": False},
    {"IS_CLICKED": False, "IS_OPENED": False},
    {"IS_CLICKED": True, "IS_OPENED": True},
    {"IS_CLICKED": False, "IS_OPENED": True}
]

# Update the dataset with new columns
updated_dataset = update_dataset_with_not_opened_email(sample_dataset)

# Display the updated dataset
for record in updated_dataset:
    print(record)
