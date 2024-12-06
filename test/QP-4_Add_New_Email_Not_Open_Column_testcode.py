import unittest
from datetime import datetime

class TestEmailNotOpenedColumn(unittest.TestCase):
    
    def setUp(self):
        self.test_data = generate_test_data(30)
    
    def test_not_opened_email_column(self):
        for record in self.test_data:
            is_clicked = record["IS_CLICKED"]
            is_opened = record["IS_OPENED"]
            not_opened_email = record["NOT_OPENED_EMAIL"]
            timestamp = record["TIMESTAMP"]
            
            # Scenario: Update record when IS_CLICKED is TRUE and IS_OPENED is FALSE
            if is_clicked and not is_opened:
                self.assertTrue(not_opened_email, "NOT_OPENED_EMAIL should be TRUE when IS_CLICKED is TRUE and IS_OPENED is FALSE")
                self.assertIsNotNone(timestamp, "TIMESTAMP should not be None when IS_CLICKED is TRUE and IS_OPENED is FALSE")
            
            # Scenario: Handle records where both IS_CLICKED and IS_OPENED are FALSE
            if not is_clicked and not is_opened:
                self.assertFalse(not_opened_email, "NOT_OPENED_EMAIL should be FALSE when both IS_CLICKED and IS_OPENED are FALSE")
                self.assertIsNone(timestamp, "TIMESTAMP should be None when both IS_CLICKED and IS_OPENED are FALSE")
    
    def test_default_behavior_for_existing_records(self):
        for record in self.test_data:
            # Ensure default value logic for NOT_OPENED_EMAIL and TIMESTAMP
            self.assertIn("NOT_OPENED_EMAIL", record, "NOT_OPENED_EMAIL column should exist in the record")
            self.assertIn("TIMESTAMP", record, "TIMESTAMP column should exist in the record")
    
    def test_columns_added_to_dataset(self):
        # Assuming the dataset is a list of dictionaries
        for record in self.test_data:
            self.assertIn("NOT_OPENED_EMAIL", record, "NOT_OPENED_EMAIL column should be added to the dataset")
            self.assertIn("TIMESTAMP", record, "TIMESTAMP column should be added to the dataset")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
