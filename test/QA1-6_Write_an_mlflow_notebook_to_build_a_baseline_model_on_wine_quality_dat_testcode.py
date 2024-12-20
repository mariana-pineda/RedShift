# Databricks notebook source
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Load the dataset
data_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
data = pd.read_csv(data_path, sep=';')

# Transform the quality column
data['high_quality'] = data['quality'] > 6

# Split the data
train_data, temp_data = train_test_split(data, test_size=0.4, random_state=42)
validate_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Prepare features and labels
X_train = train_data.drop(columns=['quality', 'high_quality'])
y_train = train_data['high_quality']
X_validate = validate_data.drop(columns=['quality', 'high_quality'])
y_validate = validate_data['high_quality']

# Train the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_model.predict(X_validate)
accuracy = accuracy_score(y_validate, y_pred)

# Log the experiment in MLflow
mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(rf_model, "model")

# Validation code
def validate_model(test_data_records):
    X_test = pd.DataFrame(test_data_records).drop(columns=['quality', 'high_quality'])
    y_test = pd.DataFrame(test_data_records)['high_quality']
    y_test_pred = rf_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print(f"Test Accuracy: {test_accuracy}")

# Validate the model with test data
validate_model(test_data_records)
