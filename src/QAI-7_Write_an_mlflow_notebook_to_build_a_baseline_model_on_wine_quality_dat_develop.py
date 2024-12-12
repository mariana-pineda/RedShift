# Databricks notebook source
import pandas as pd
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

# Test the model on the test set
y_test_pred = rf_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)

# Log test accuracy
with mlflow.start_run():
    mlflow.log_metric("test_accuracy", test_accuracy)
