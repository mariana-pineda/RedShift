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

# Transform the quality column
data['high_quality'] = data['quality'] > 6

# Split the data
train_data = data.sample(frac=0.6, random_state=42)
remaining_data = data.drop(train_data.index)
validate_data = remaining_data.sample(frac=0.5, random_state=42)
test_data = remaining_data.drop(validate_data.index)

# Prepare features and labels
X_train = train_data.drop(columns=['quality', 'high_quality'])
y_train = train_data['high_quality']
X_validate = validate_data.drop(columns=['quality', 'high_quality'])
y_validate = validate_data['high_quality']
X_test = test_data.drop(columns=['quality', 'high_quality'])
y_test = test_data['high_quality']

# Train the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Validate the model
y_validate_pred = rf_model.predict(X_validate)
validate_accuracy = accuracy_score(y_validate, y_validate_pred)

# Test the model
y_test_pred = rf_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)

# Log the experiment in MLflow
mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("validate_accuracy", validate_accuracy)
    mlflow.log_metric("test_accuracy", test_accuracy)
    mlflow.sklearn.log_model(rf_model, "model")
