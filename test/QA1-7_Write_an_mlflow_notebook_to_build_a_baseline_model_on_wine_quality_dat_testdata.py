# Databricks notebook source
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the dataset
data_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
df = pd.read_csv(data_path, sep=';')

# Transform the "quality" column into "high_quality"
df['high_quality'] = df['quality'] > 6

# Split the data into 60% training, 20% validation, and 20% testing sets
train, temp = train_test_split(df, test_size=0.4, random_state=42)
validate, test = train_test_split(temp, test_size=0.5, random_state=42)

# Generate test data
def generate_test_data():
    test_data = []
    for i in range(25):  # Generate 25 records
        record = {
            'fixed_acidity': np.random.uniform(4, 15),  # Random value between 4 and 15
            'volatile_acidity': np.random.uniform(0.1, 1.5),  # Random value between 0.1 and 1.5
            'citric_acid': np.random.uniform(0, 1),  # Random value between 0 and 1
            'residual_sugar': np.random.uniform(0.5, 15),  # Random value between 0.5 and 15
            'chlorides': np.random.uniform(0.01, 0.2),  # Random value between 0.01 and 0.2
            'free_sulfur_dioxide': np.random.uniform(1, 72),  # Random value between 1 and 72
            'total_sulfur_dioxide': np.random.uniform(6, 289),  # Random value between 6 and 289
            'density': np.random.uniform(0.990, 1.004),  # Random value between 0.990 and 1.004
            'pH': np.random.uniform(2.8, 4),  # Random value between 2.8 and 4
            'sulphates': np.random.uniform(0.22, 1.08),  # Random value between 0.22 and 1.08
            'alcohol': np.random.uniform(8, 14),  # Random value between 8 and 14
            'high_quality': np.random.choice([True, False])  # Randomly choose True or False
        }
        test_data.append(record)
    return pd.DataFrame(test_data)

# Generate and display the test data
test_data_df = generate_test_data()
print(test_data_df)
