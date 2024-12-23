# Databricks notebook source
import pandas as pd
import numpy as np

# Load the dataset
file_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
data = pd.read_csv(file_path, sep=';')

# Transform the "quality" column into "high_quality"
data['high_quality'] = data['quality'] > 6

# Split the data into 60% training, 20% validation, and 20% test sets
train_data = data.sample(frac=0.6, random_state=42)
remaining_data = data.drop(train_data.index)
validation_data = remaining_data.sample(frac=0.5, random_state=42)
test_data = remaining_data.drop(validation_data.index)

# Generate test data for each condition
def generate_test_data():
    test_data_records = []

    # Condition: quality > 6 (high_quality = True)
    high_quality_data = data[data['quality'] > 6]
    test_data_records.extend(high_quality_data.sample(n=10, random_state=42).to_dict(orient='records'))

    # Condition: quality <= 6 (high_quality = False)
    low_quality_data = data[data['quality'] <= 6]
    test_data_records.extend(low_quality_data.sample(n=10, random_state=42).to_dict(orient='records'))

    # Condition: Check data split ratios
    assert len(train_data) / len(data) == 0.6, "Training data split ratio is incorrect"
    assert len(validation_data) / len(data) == 0.2, "Validation data split ratio is incorrect"
    assert len(test_data) / len(data) == 0.2, "Test data split ratio is incorrect"

    return test_data_records

# Generate and print test data
test_data_records = generate_test_data()
print(test_data_records)
