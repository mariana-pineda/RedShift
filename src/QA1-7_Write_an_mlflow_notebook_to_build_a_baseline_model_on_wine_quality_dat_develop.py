# Databricks notebook source
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn

# Load the dataset
data_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
df = pd.read_csv(data_path, sep=';')

# Transform the "quality" column into "high_quality"
df['high_quality'] = df['quality'] > 6

# Split the data into 60% training, 20% validation, and 20% testing sets
train, temp = train_test_split(df, test_size=0.4, random_state=42)
validate, test = train_test_split(temp, test_size=0.5, random_state=42)

# Prepare the data for training
X_train = train.drop(['quality', 'high_quality'], axis=1)
y_train = train['high_quality']
X_validate = validate.drop(['quality', 'high_quality'], axis=1)
y_validate = validate['high_quality']
X_test = test.drop(['quality', 'high_quality'], axis=1)
y_test = test['high_quality']

# Train the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Validate the model
y_validate_pred = rf_model.predict(X_validate)
validate_accuracy = accuracy_score(y_validate, y_validate_pred)
validate_precision = precision_score(y_validate, y_validate_pred)
validate_recall = recall_score(y_validate, y_validate_pred)
validate_f1 = f1_score(y_validate, y_validate_pred)

# Test the model
y_test_pred = rf_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
test_precision = precision_score(y_test, y_test_pred)
test_recall = recall_score(y_test, y_test_pred)
test_f1 = f1_score(y_test, y_test_pred)

# Log the experiment in MLflow
mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
with mlflow.start_run():
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("validate_accuracy", validate_accuracy)
    mlflow.log_metric("validate_precision", validate_precision)
    mlflow.log_metric("validate_recall", validate_recall)
    mlflow.log_metric("validate_f1", validate_f1)
    mlflow.log_metric("test_accuracy", test_accuracy)
    mlflow.log_metric("test_precision", test_precision)
    mlflow.log_metric("test_recall", test_recall)
    mlflow.log_metric("test_f1", test_f1)
    mlflow.sklearn.log_model(rf_model, "random_forest_model")

# Validation code
def validate_model():
    assert validate_accuracy > 0.5, "Validation accuracy is too low"
    assert test_accuracy > 0.5, "Test accuracy is too low"
    print("Validation and test accuracy are above threshold")

validate_model()
