# Databricks notebook source
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

# Load data
data_path = '/dbfs/databricks-datasets/wine-quality/winequality-white.csv'
data = pd.read_csv(data_path, sep=';')

# Preprocess data
data['high_quality'] = data['quality'] > 6
data.drop('quality', axis=1, inplace=True)

# Split data
train, temp = train_test_split(data, test_size=0.4, random_state=42)
validate, test = train_test_split(temp, test_size=0.5, random_state=42)

# Train model
X_train = train.drop('high_quality', axis=1)
y_train = train['high_quality']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Validate model
X_validate = validate.drop('high_quality', axis=1)
y_validate = validate['high_quality']
validation_score = model.score(X_validate, y_validate)

# Log experiment
mlflow.set_experiment('/Workspace/Shared/purgo_poc/winequality-experiment')
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_metric("validation_score", validation_score)
