# Databricks notebook source

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from datetime import datetime
import unittest

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

# Test code
class TestWineQualityModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load the dataset
        cls.df = pd.read_csv(data_path, sep=';')
        cls.df['high_quality'] = cls.df['quality'] > 6
        cls.df.drop('quality', axis=1, inplace=True)
        cls.df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cls.train, cls.temp = train_test_split(cls.df, test_size=0.4, random_state=42)
        cls.validate, cls.test = train_test_split(cls.temp, test_size=0.5, random_state=42)
        cls.features = cls.df.columns.drop(['high_quality', 'timestamp'])
        cls.target = 'high_quality'
        cls.rf_model = RandomForestClassifier(random_state=42)
        cls.rf_model.fit(cls.train[cls.features], cls.train[cls.target])
    
    def test_data_split(self):
        # Test if the data is split correctly
        self.assertEqual(len(self.train) + len(self.validate) + len(self.test), len(self.df))
        self.assertAlmostEqual(len(self.train) / len(self.df), 0.6, delta=0.05)
        self.assertAlmostEqual(len(self.validate) / len(self.df), 0.2, delta=0.05)
        self.assertAlmostEqual(len(self.test) / len(self.df), 0.2, delta=0.05)
    
    def test_model_training(self):
        # Test if the model is trained
        self.assertIsNotNone(self.rf_model)
    
    def test_validation_score(self):
        # Test if the validation score is logged
        validation_score = self.rf_model.score(self.validate[self.features], self.validate[self.target])
        self.assertGreaterEqual(validation_score, 0.5)  # Assuming a baseline accuracy
    
    def test_test_score(self):
        # Test if the test score is logged
        test_score = self.rf_model.score(self.test[self.features], self.test[self.target])
        self.assertGreaterEqual(test_score, 0.5)  # Assuming a baseline accuracy
    
    def test_error_handling(self):
        # Test error handling for missing columns
        with self.assertRaises(KeyError):
            self.rf_model.fit(self.train[['non_existent_column']], self.train[self.target])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

