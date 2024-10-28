# Databricks notebook source

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and preprocess data
df = pd.read_csv('/dbfs/databricks-datasets/wine-quality/winequality-white.csv', sep=';')
df['high_quality'] = df['quality'] > 6
df.drop(columns='quality', inplace=True)

# Split data
train, temp = train_test_split(df, test_size=0.4, random_state=42)
validate, test = train_test_split(temp, test_size=0.5, random_state=42)

# Prepare training and validation data
X_train = train.drop(columns='high_quality')
y_train = train['high_quality']
X_validate = validate.drop(columns='high_quality')
y_validate = validate['high_quality']
X_test = test.drop(columns='high_quality')
y_test = test['high_quality']

# MLflow experiment setup
mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")

with mlflow.start_run():
    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Log model
    mlflow.sklearn.log_model(model, "random_forest_model")
    
    # Validation
    validate_score = model.score(X_validate, y_validate)
    test_score = model.score(X_test, y_test)
    
    # Log metrics
    mlflow.log_metric("validate_score", validate_score)
    mlflow.log_metric("test_score", test_score)
    
    # Output validation and test scores
    print("Validation Score:", validate_score)
    print("Test Score:", test_score)
