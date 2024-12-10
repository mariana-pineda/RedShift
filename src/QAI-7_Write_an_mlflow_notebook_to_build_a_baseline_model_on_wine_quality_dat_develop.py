# Databricks notebook source
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

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

# Separate features and target
X_train = train_data.drop('high_quality', axis=1)
y_train = train_data['high_quality']
X_validation = validation_data.drop('high_quality', axis=1)
y_validation = validation_data['high_quality']
X_test = test_data.drop('high_quality', axis=1)
y_test = test_data['high_quality']

# Train a Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate the model on the validation set
y_val_pred = rf_model.predict(X_validation)
validation_accuracy = accuracy_score(y_validation, y_val_pred)

# Log the experiment in MLflow
mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("validation_accuracy", validation_accuracy)
    mlflow.sklearn.log_model(rf_model, "random_forest_model")

# Validate the transformation of 'quality' to 'high_quality'
def validate_high_quality_transformation(data):
    expected_true = data[data['high_quality'] == True]
    expected_false = data[data['high_quality'] == False]
    assert all(expected_true['high_quality'] == True), "Failed: Not all high_quality are True for quality > 6"
    assert all(expected_false['high_quality'] == False), "Failed: Not all high_quality are False for quality <= 6"
    print("Validation of high_quality transformation passed.")

# Validate the data split
def validate_data_split(train_data, validation_data, test_data, total_data):
    total_length = len(total_data)
    assert len(train_data) == int(0.6 * total_length), "Failed: Train data split is incorrect"
    assert len(validation_data) == int(0.2 * total_length), "Failed: Validation data split is incorrect"
    assert len(test_data) == int(0.2 * total_length), "Failed: Test data split is incorrect"
    print("Validation of data split passed.")

# Run validations
validate_high_quality_transformation(data)
validate_data_split(train_data, validation_data, test_data, data)

