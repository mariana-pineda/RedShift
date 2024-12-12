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

# Prepare features and labels
X_train = train_data.drop('high_quality', axis=1)
y_train = train_data['high_quality']
X_val = validation_data.drop('high_quality', axis=1)
y_val = validation_data['high_quality']
X_test = test_data.drop('high_quality', axis=1)
y_test = test_data['high_quality']

# Train the Random Forest Model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Validate the model
val_predictions = rf_model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_predictions)

# Test the model
test_predictions = rf_model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_predictions)

# Log the experiment
mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
with mlflow.start_run():
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("validation_accuracy", val_accuracy)
    mlflow.log_metric("test_accuracy", test_accuracy)
    mlflow.sklearn.log_model(rf_model, "random_forest_model")
