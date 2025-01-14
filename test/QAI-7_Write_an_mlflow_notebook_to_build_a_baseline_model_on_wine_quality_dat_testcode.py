# Databricks notebook source
import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

class TestWineQualityModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load data
        cls.data_path = '/dbfs/databricks-datasets/wine-quality/winequality-white.csv'
        cls.data = pd.read_csv(cls.data_path, sep=';')
        # Preprocess data
        cls.data['high_quality'] = cls.data['quality'] > 6
        cls.data.drop('quality', axis=1, inplace=True)
        # Split data
        cls.train, cls.temp = train_test_split(cls.data, test_size=0.4, random_state=42)
        cls.validate, cls.test = train_test_split(cls.temp, test_size=0.5, random_state=42)

    def test_data_loading(self):
        # Test if data is loaded correctly
        self.assertFalse(self.data.empty, "Data should not be empty after loading")
        self.assertIn('high_quality', self.data.columns, "Data should have 'high_quality' column after preprocessing")

    def test_data_splitting(self):
        # Test if data is split correctly
        total_rows = len(self.data)
        train_rows = len(self.train)
        validate_rows = len(self.validate)
        test_rows = len(self.test)
        self.assertAlmostEqual(train_rows / total_rows, 0.6, delta=0.05, msg="Training set should be approximately 60% of total data")
        self.assertAlmostEqual(validate_rows / total_rows, 0.2, delta=0.05, msg="Validation set should be approximately 20% of total data")
        self.assertAlmostEqual(test_rows / total_rows, 0.2, delta=0.05, msg="Test set should be approximately 20% of total data")

    def test_model_training(self):
        # Test if model trains without errors
        X_train = self.train.drop('high_quality', axis=1)
        y_train = self.train['high_quality']
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        self.assertIsNotNone(model, "Model should be trained and not None")

    def test_model_validation(self):
        # Test if model validation score is reasonable
        X_validate = self.validate.drop('high_quality', axis=1)
        y_validate = self.validate['high_quality']
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(self.train.drop('high_quality', axis=1), self.train['high_quality'])
        validation_score = model.score(X_validate, y_validate)
        self.assertGreater(validation_score, 0.5, "Validation score should be greater than 0.5")

    def test_experiment_logging(self):
        # Test if experiment logs correctly
        mlflow.set_experiment('/Workspace/Shared/purgo_poc/winequality-experiment')
        with mlflow.start_run():
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(self.train.drop('high_quality', axis=1), self.train['high_quality'])
            mlflow.sklearn.log_model(model, "model")
            mlflow.log_metric("validation_score", model.score(self.validate.drop('high_quality', axis=1), self.validate['high_quality']))
            run_id = mlflow.active_run().info.run_id
            self.assertIsNotNone(run_id, "Run ID should not be None after logging experiment")

    @classmethod
    def tearDownClass(cls):
        # Clean up resources if needed
        pass

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
