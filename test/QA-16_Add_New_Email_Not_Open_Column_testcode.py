import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

class TestEmailTrackingData(unittest.TestCase):

    def setUp(self):
        # Generate test data
        self.test_data = generate_test_data()

    def test_not_opened_email_column(self):
        # Validate NOT_OPENED_EMAIL logic
        for index, row in self.test_data.iterrows():
            expected_value = row['IS_CLICKED'] and not row['IS_OPENED']
            actual_value = row['NOT_OPENED_EMAIL']
            self.assertEqual(expected_value, actual_value, f"Row {index} failed: Expected NOT_OPENED_EMAIL to be {expected_value} but got {actual_value}")

    def test_timestamps_column(self):
        # Validate _timestamps_ column is present and in seconds
        self.assertIn('_timestamps_', self.test_data.columns, "_timestamps_ column is missing")
        for index, timestamp in enumerate(self.test_data['_timestamps_']):
            self.assertIsInstance(timestamp, int, f"Row {index} failed: _timestamps_ is not an integer")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
