# Databricks notebook source
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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

# Train Random Forest Model
X_train = train_data.drop('high_quality', axis=1)
y_train = train_data['high_quality']
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Validate the model
X_validate = validate_data.drop('high_quality', axis=1)
y_validate = validate_data['high_quality']
y_pred_validate = model.predict(X_validate)
validation_accuracy = accuracy_score(y_validate, y_pred_validate)

# Test the model
X_test = test_data.drop('high_quality', axis=1)
y_test = test_data['high_quality']
y_pred_test = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred_test)

# Validation Code
def validate_transformation(test_data_df):
    for index, row in test_data_df.iterrows():
        expected = row['high_quality']
        actual = row['quality'] > 6
        assert expected == actual, f"Row {index} failed: expected {expected}, got {actual}"

# Validate transformation logic
validate_transformation(test_data_df)

# Print results
print(f"Validation Accuracy: {validation_accuracy}")
print(f"Test Accuracy: {test_accuracy}")
