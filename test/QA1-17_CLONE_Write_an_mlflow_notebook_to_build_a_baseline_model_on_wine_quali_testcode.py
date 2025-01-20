# Databricks notebook source

# Import necessary libraries
import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from datetime import datetime
import mlflow
import mlflow.sklearn

class TestWineQualityModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the dataset
        cls.data_path = "/dbfs/databricks-datasets/wine-quality/winequality-white.csv"
        cls.df = pd.read_csv(cls.data_path, sep=';')
        
        # Transform the 'quality' column into a binary 'high_quality' column
        cls.df['high_quality'] = cls.df['quality'] > 6
        
        # Add a new column 'timestamp' with the current timestamp
        cls.df['timestamp'] = datetime.now()
        
        # Drop the original 'quality' column
        cls.df.drop('quality', axis=1, inplace=True)
        
        # Split the data into training, validation, and test sets
        cls.train, cls.temp = train_test_split(cls.df, test_size=0.4, random_state=42)
        cls.validate, cls.test = train_test_split(cls.temp, test_size=0.5, random_state=42)
        
        # Define the features and target variable
        cls.features = cls.df.columns.difference(['high_quality', 'timestamp'])
        cls.target = 'high_quality'

    def test_data_loading(self):
        # Test if data is loaded correctly
        self.assertFalse(self.df.empty, "Dataframe is empty after loading")
        self.assertIn('high_quality', self.df.columns, "'high_quality' column not found in dataframe")
        self.assertIn('timestamp', self.df.columns, "'timestamp' column not found in dataframe")

    def test_data_splitting(self):
        # Test if data is split correctly
        total_rows = len(self.df)
        self.assertEqual(len(self.train), int(0.6 * total_rows), "Training set size is incorrect")
        self.assertEqual(len(self.validate), int(0.2 * total_rows), "Validation set size is incorrect")
        self.assertEqual(len(self.test), int(0.2 * total_rows), "Test set size is incorrect")

    def test_random_forest_training(self):
        # Test if Random Forest model trains without errors
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(self.train[self.features], self.train[self.target])
        train_score = rf.score(self.train[self.features], self.train[self.target])
        self.assertGreater(train_score, 0.5, "Training accuracy is too low")

    def test_model_validation(self):
        # Test model validation
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(self.train[self.features], self.train[self.target])
        validation_score = rf.score(self.validate[self.features], self.validate[self.target])
        self.assertGreater(validation_score, 0.5, "Validation accuracy is too low")

    def test_model_testing(self):
        # Test model testing
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(self.train[self.features], self.train[self.target])
        test_score = rf.score(self.test[self.features], self.test[self.target])
        self.assertGreater(test_score, 0.5, "Test accuracy is too low")

    def test_mlflow_logging(self):
        # Test MLflow logging
        with mlflow.start_run():
            rf = RandomForestClassifier(n_estimators=100, random_state=42)
            rf.fit(self.train[self.features], self.train[self.target])
            mlflow.sklearn.log_model(rf, "random_forest_model")
            mlflow.log_param("n_estimators", 100)
            mlflow.log_param("random_state", 42)
            validation_score = rf.score(self.validate[self.features], self.validate[self.target])
            mlflow.log_metric("validation_score", validation_score)
            test_score = rf.score(self.test[self.features], self.test[self.target])
            mlflow.log_metric("test_score", test_score)
            mlflow.set_experiment("/Workspace/Shared/purgo_poc/winequality-experiement")
            self.assertTrue(True, "MLflow logging failed")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
