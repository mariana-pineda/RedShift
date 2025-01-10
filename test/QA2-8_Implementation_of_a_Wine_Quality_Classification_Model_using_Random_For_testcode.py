import unittest
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

class TestWineQualityPipeline(unittest.TestCase):

    def setUp(self):
        # Generate synthetic data for testing
        np.random.seed(42)
        num_records = 30
        fixed_acidity = np.random.uniform(4, 15, num_records)
        volatile_acidity = np.random.uniform(0.1, 1.5, num_records)
        citric_acid = np.random.uniform(0, 1, num_records)
        residual_sugar = np.random.uniform(0.5, 15, num_records)
        chlorides = np.random.uniform(0.01, 0.2, num_records)
        free_sulfur_dioxide = np.random.uniform(1, 72, num_records)
        total_sulfur_dioxide = np.random.uniform(6, 289, num_records)
        density = np.random.uniform(0.990, 1.004, num_records)
        pH = np.random.uniform(2.8, 4, num_records)
        sulphates = np.random.uniform(0.2, 1.2, num_records)
        alcohol = np.random.uniform(8, 14, num_records)
        quality = np.random.randint(3, 10, num_records)
        high_quality = quality > 6

        self.test_data = pd.DataFrame({
            'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid,
            'residual_sugar': residual_sugar,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol,
            'high_quality': high_quality
        })

    def test_data_preprocessing(self):
        # Check if 'high_quality' is correctly converted
        expected_high_quality = self.test_data['quality'] > 6
        actual_high_quality = self.test_data['high_quality']
        pd.testing.assert_series_equal(expected_high_quality, actual_high_quality)

    def test_model_training_and_accuracy(self):
        # Split the data
        X = self.test_data.drop('high_quality', axis=1)
        y = self.test_data['high_quality']
        X_train, X_test, y_train, y_test = X[:20], X[20:], y[:20], y[20:]

        # Train the model
        rf_model = RandomForestClassifier(random_state=42)
        rf_model.fit(X_train, y_train)

        # Validate the model
        y_test_pred = rf_model.predict(X_test)
        test_accuracy = accuracy_score(y_test, y_test_pred)

        # Check if the model achieves at least 80% accuracy
        self.assertGreaterEqual(test_accuracy, 0.8)

    def test_mlflow_logging(self):
        # This is a placeholder for MLflow logging test
        # Assuming MLflow logging is done in the main pipeline
        # Here we would check if the logs are correctly recorded
        pass

if __name__ == '__main__':
    unittest.main()
