import unittest

class TestInventoryTransaction(unittest.TestCase):

    def setUp(self):
        self.test_data = generate_inventory_transaction_data(25)

    def test_inbound_inventory_recording(self):
        for record in self.test_data:
            self.assertIn(record['transaction_type'], ["inbound", "outbound"])
            self.assertGreaterEqual(record['quantity'], 1)
            self.assertLessEqual(record['quantity'], 500)

    def test_data_discrepancies(self):
        for record in self.test_data:
            self.assertIn(record['source_system'], ["Redshift", "Databricks"])
            self.assertIsInstance(record['discrepancy_flag'], bool)

    def test_error_handling(self):
        for record in self.test_data:
            self.assertIsInstance(record['error_logged'], bool)

    def test_output_format_and_reporting(self):
        for record in self.test_data:
            self.assertIsInstance(record['report_generated'], bool)

    def test_transaction_date_range(self):
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 12, 31)
        for record in self.test_data:
            self.assertGreaterEqual(record['transaction_date'], start_date)
            self.assertLessEqual(record['transaction_date'], end_date)

if __name__ == '__main__':
    unittest.main()
