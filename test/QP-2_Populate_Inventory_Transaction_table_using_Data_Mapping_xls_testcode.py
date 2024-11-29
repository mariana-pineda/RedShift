import unittest

class TestInventoryTransaction(unittest.TestCase):
    
    def setUp(self):
        # Setup test data
        self.test_data = [
            {
                "transaction_id": "1",
                "expired_dt": datetime(2023, 1, 10),
                "cancel_dt": datetime(2023, 1, 5),
                "financial_qty": 10,
                "net_qty": 2,
                "item_nbr": "item_1",
                "unit_cost": 12.34,
                "expired_qt": 5,
                "crt_dt": datetime(2022, 5, 1),
                "updt_dt": datetime(2022, 6, 1),
            },
            # Add more test records if needed
        ]

    def test_unique_transaction_id(self):
        transaction_ids = [record["transaction_id"] for record in self.test_data]
        self.assertEqual(len(transaction_ids), len(set(transaction_ids)))
        
    def test_data_type_consistency(self):
        for record in self.test_data:
            self.assertIsInstance(record["expired_dt"], datetime)
            self.assertIsInstance(record["cancel_dt"], datetime)
            self.assertIsInstance(record["expired_qt"], (int, type(None)))
            self.assertIsInstance(record["crt_dt"], datetime)
            self.assertIsInstance(record["updt_dt"], datetime)

    def test_financial_qty_and_net_qty_conditions(self):
        for record in self.test_data:
            self.assertGreaterEqual(record["financial_qty"], record["net_qty"])

    def test_item_nbr_transformation(self):
        valid_items = [f"item_{i}" for i in range(1, 21)]
        for record in self.test_data:
            self.assertIn(record["item_nbr"], valid_items)

    def test_unit_cost_transformation(self):
        valid_unit_costs = [round(i, 2) for i in range(1, 101)]
        for record in self.test_data:
            self.assertIn(record["unit_cost"], valid_unit_costs)

    def test_handle_null_values(self):
        for record in self.test_data:
            if record["expired_qt"] is not None:
                self.assertIsInstance(record["expired_qt"], int)

    def test_timestamps_sequence(self):
        for record in self.test_data:
            self.assertLessEqual(record["crt_dt"], record["updt_dt"])

if __name__ == "__main__":
    unittest.main()
