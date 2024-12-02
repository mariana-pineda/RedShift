import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

class TestEmailStatusColumns(unittest.TestCase):

    def setUp(self):
        self.test_data = generate_test_data()

    def test_not_opened_email_column(self):
        # Validate NOT_OPENED_EMAIL logic
        for index, row in self.test_data.iterrows():
            expected_value = row['IS_CLICKED'] and not row['IS_OPENED']
            actual_value = row['NOT_OPENED_EMAIL']
            self.assertEqual(expected_value, actual_value, f"Row {index} failed: Expected {expected_value}, got {actual_value}")

    def test_timestamps_column(self):
        # Validate _timestamps_ column is in seconds
        for index, row in self.test_data.iterrows():
            self.assertIsInstance(row['_timestamps_'], int, f"Row {index} failed: _timestamps_ is not an integer")

    def test_data_integrity(self):
        # Ensure no data is lost or altered unexpectedly
        expected_columns = ['IS_CLICKED', 'IS_OPENED', 'NOT_OPENED_EMAIL', '_timestamps_']
        actual_columns = list(self.test_data.columns)
        self.assertListEqual(expected_columns, actual_columns, f"Expected columns {expected_columns}, but got {actual_columns}")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
