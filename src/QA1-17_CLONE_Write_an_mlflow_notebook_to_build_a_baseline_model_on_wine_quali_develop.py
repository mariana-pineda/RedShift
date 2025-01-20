# Databricks notebook source

# Import necessary libraries
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

# Load the dataset
data_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
df = pd.read_csv(data_path, sep=';')

# Transform the 'quality' column into a binary 'high_quality' column
df['high_quality'] = df['quality'] > 6

# Add a new column 'timestamp' with the current timestamp
df['timestamp'] = datetime.now()

# Drop the original 'quality' column
df.drop('quality', axis=1, inplace=True)

# Split the data into training, validation, and test sets
train, temp = train_test_split(df, test_size=0.4, random_state=42)
validate, test = train_test_split(temp, test_size=0.5, random_state=42)

# Define the features and target variable
features = df.columns.difference(['high_quality', 'timestamp'])
target = 'high_quality'

# Train a Random Forest model
with mlflow.start_run():
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(train[features], train[target])

    # Log the model
    mlflow.sklearn.log_model(rf, "random_forest_model")

    # Log the parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)

    # Validate the model
    validation_score = rf.score(validate[features], validate[target])
    mlflow.log_metric("validation_score", validation_score)

    # Test the model
    test_score = rf.score(test[features], test[target])
    mlflow.log_metric("test_score", test_score)

    # Set the experiment path
    mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
