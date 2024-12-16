# Databricks notebook source
import pandas as pd
import numpy as np

# Load the dataset
file_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
data = pd.read_csv(file_path, sep=';')

# Transform the quality column
data['high_quality'] = data['quality'] > 6

# Split the data
train_data = data.sample(frac=0.6, random_state=42)
remaining_data = data.drop(train_data.index)
validate_data = remaining_data.sample(frac=0.5, random_state=42)
test_data = remaining_data.drop(validate_data.index)

# Generate test data
def generate_test_data():
    test_data_records = []

    # Condition: Quality > 6 (high_quality = True)
    high_quality_data = data[data['quality'] > 6]
    for _ in range(10):
        record = high_quality_data.sample(n=1).to_dict(orient='records')[0]
        test_data_records.append(record)

    # Condition: Quality <= 6 (high_quality = False)
    low_quality_data = data[data['quality'] <= 6]
    for _ in range(10):
        record = low_quality_data.sample(n=1).to_dict(orient='records')[0]
        test_data_records.append(record)

    # Additional random samples to ensure variety
    for _ in range(10):
        record = data.sample(n=1).to_dict(orient='records')[0]
        test_data_records.append(record)

    return test_data_records

test_data_records = generate_test_data()
print(test_data_records)
