# Databricks notebook source

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from datetime import datetime

# Load the dataset
data_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
df = pd.read_csv(data_path, sep=';')

# Replace 'quality' column with 'high_quality' (True if quality > 6, else False)
df['high_quality'] = df['quality'] > 6
df.drop('quality', axis=1, inplace=True)

# Add a new column with the current timestamp
df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Split the data into train (60%), validation (20%), and test (20%) sets
train, temp = train_test_split(df, test_size=0.4, random_state=42)
validate, test = train_test_split(temp, test_size=0.5, random_state=42)

# Define features and target
features = df.columns.drop(['high_quality', 'timestamp'])
target = 'high_quality'

# Train the Random Forest model
with mlflow.start_run(experiment_id="/Workspace/Shared/purgo_poc/winequality-experiement"):
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(train[features], train[target])
    
    # Log the model
    mlflow.sklearn.log_model(rf_model, "random_forest_model")
    
    # Validate the model
    validation_score = rf_model.score(validate[features], validate[target])
    mlflow.log_metric("validation_score", validation_score)
    
    # Test the model
    test_score = rf_model.score(test[features], test[target])
    mlflow.log_metric("test_score", test_score)

# End of the notebook

