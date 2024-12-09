# Databricks notebook source
import pandas as pd
import numpy as np

# Load the dataset
file_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
data = pd.read_csv(file_path, sep=';')

# Transform the 'quality' column to 'high_quality'
data['high_quality'] = data['quality'] > 6
data.drop('quality', axis=1, inplace=True)

# Split the data into train, validation, and test sets
train_data = data.sample(frac=0.6, random_state=42)
remaining_data = data.drop(train_data.index)
validation_data = remaining_data.sample(frac=0.5, random_state=42)
test_data = remaining_data.drop(validation_data.index)

# Generate test data for each condition
# Condition: quality > 6 should be True
high_quality_true = data[data['high_quality'] == True].sample(10, random_state=42)

# Condition: quality <= 6 should be False
high_quality_false = data[data['high_quality'] == False].sample(10, random_state=42)

# Combine the test data
test_data_generated = pd.concat([high_quality_true, high_quality_false])

# Output the generated test data
print(test_data_generated)
