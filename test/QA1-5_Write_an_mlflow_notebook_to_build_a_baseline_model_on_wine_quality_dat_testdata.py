# Databricks notebook source
import pandas as pd
import numpy as np

# Load the dataset
file_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
data = pd.read_csv(file_path, sep=';')

# Transform the 'quality' column to 'high_quality'
data['high_quality'] = data['quality'] > 6

# Drop the original 'quality' column
data.drop('quality', axis=1, inplace=True)

# Split the data into 60% train, 20% validation, and 20% test
train_data, validate_data, test_data = np.split(
    data.sample(frac=1, random_state=42), 
    [int(.6*len(data)), int(.8*len(data))]
)

# Generate test data to validate conditions
def generate_test_data():
    test_data = []

    # Condition: quality > 6 should be high_quality = True
    test_data.append({
        'fixed acidity': 7.0,
        'volatile acidity': 0.27,
        'citric acid': 0.36,
        'residual sugar': 20.7,
        'chlorides': 0.045,
        'free sulfur dioxide': 45.0,
        'total sulfur dioxide': 170.0,
        'density': 1.001,
        'pH': 3.0,
        'sulphates': 0.45,
        'alcohol': 8.8,
        'high_quality': True  # quality > 6
    })

    # Condition: quality <= 6 should be high_quality = False
    test_data.append({
        'fixed acidity': 6.3,
        'volatile acidity': 0.3,
        'citric acid': 0.34,
        'residual sugar': 1.6,
        'chlorides': 0.049,
        'free sulfur dioxide': 14.0,
        'total sulfur dioxide': 132.0,
        'density': 0.994,
        'pH': 3.3,
        'sulphates': 0.49,
        'alcohol': 9.5,
        'high_quality': False  # quality <= 6
    })

    # Generate more test data records
    for _ in range(18):
        record = {
            'fixed acidity': np.random.uniform(5.0, 9.0),
            'volatile acidity': np.random.uniform(0.1, 0.5),
            'citric acid': np.random.uniform(0.0, 0.5),
            'residual sugar': np.random.uniform(0.5, 15.0),
            'chlorides': np.random.uniform(0.01, 0.1),
            'free sulfur dioxide': np.random.uniform(5.0, 50.0),
            'total sulfur dioxide': np.random.uniform(50.0, 200.0),
            'density': np.random.uniform(0.990, 1.005),
            'pH': np.random.uniform(2.8, 3.8),
            'sulphates': np.random.uniform(0.3, 0.8),
            'alcohol': np.random.uniform(8.0, 14.0),
            'high_quality': np.random.choice([True, False])
        }
        test_data.append(record)

    return pd.DataFrame(test_data)

# Generate the test data
test_data_df = generate_test_data()
