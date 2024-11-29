# Databricks notebook source

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = '/dbfs/databricks-datasets/wine-quality/winequality-white.csv'
# The data is read from the CSV file with ';' as the separator
wine_data = pd.read_csv(file_path, sep=';')

# Convert the 'quality' column to 'high_quality'
# The condition where quality > 6 is set to True, otherwise False
wine_data['high_quality'] = wine_data['quality'] > 6

# Drop the original 'quality' column as it is no longer needed
wine_data.drop('quality', axis=1, inplace=True)

# Split the dataset: 60% train, 20% validation, 20% test
# The condition ensures that the datasets are split correctly according to the required percentages
train_data, temp_data = train_test_split(wine_data, test_size=0.4, random_state=123) # 60% train data
validate_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=123) # 20% validate, 20% test data

# Print the number of records in each dataset to validate the conditions
print(f"Train data records: {len(train_data)}")  # Expect around 60% of the data
print(f"Validation data records: {len(validate_data)}")  # Expect around 20% of the data
print(f"Test data records: {len(test_data)}")  # Expect around 20% of the data

# Output samples to ensure correctness
print(train_data.head())
print(validate_data.head())
print(test_data.head())

