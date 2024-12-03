import unittest
from datetime import datetime

class TestEmailNotOpenedColumn(unittest.TestCase):

    def setUp(self):
        self.test_data = generate_test_data(30)
        self.default_timestamp_format = "%Y-%m-%d %H:%M:%S"

    def test_update_record_when_is_clicked_true_and_is_opened_false(self):
        for record in self.test_data:
            if record['IS_CLICKED'] and not record['IS_OPENED']:
                self.assertTrue(record["NOT_OPENED_EMAIL"], "NOT_OPENED_EMAIL should be TRUE")
                self.assertIsNotNone(record["TIMESTAMP"], "Timestamp should not be None")
                # Verify timestamp format
                try:
                    datetime.strptime(record["TIMESTAMP"], self.default_timestamp_format)
                except ValueError:
                    self.fail("Timestamp is not in the correct format")

    def test_handle_records_where_both_is_clicked_and_is_opened_false(self):
        for record in self.test_data:
            if not record['IS_CLICKED'] and not record['IS_OPENED']:
                self.assertFalse(record["NOT_OPENED_EMAIL"], "NOT_OPENED_EMAIL should be FALSE")
                self.assertIsNone(record["TIMESTAMP"], "Timestamp should be None")

    def test_newly_added_columns_default_behavior_for_existing_records(self):
        for record in self.test_data:
            if not (record['IS_CLICKED'] and not record['IS_OPENED']):
                self.assertIsInstance(record["NOT_OPENED_EMAIL"], bool, "Default value should be a boolean")
                if record['IS_CLICKED'] or record['IS_OPENED']:
                    self.assertIsNone(record["TIMESTAMP"], "Timestamp should remain None for existing records not matching")

    def test_ensure_new_columns_are_in_the_intended_dataset(self):
        for record in self.test_data:
            self.assertIn("NOT_OPENED_EMAIL", record, "NOT_OPENED_EMAIL column is missing")
            self.assertIn("TIMESTAMP", record, "TIMESTAMP column is missing")

# Run the tests
if __name__ == '__main__':
    unittest.main()
