import unittest

class TestInventoryTransaction(unittest.TestCase):
    def setUp(self):
        self.test_data = generate_inventory_transaction_data(25)

    def test_transaction_id_range(self):
        for record in self.test_data:
            self.assertTrue(1000 <= record["transaction_id"] <= 9999, f"Transaction ID {record['transaction_id']} out of range")

    def test_item_id_range(self):
        for record in self.test_data:
            self.assertTrue(1 <= record["item_id"] <= 100, f"Item ID {record['item_id']} out of range")

    def test_quantity_range(self):
        for record in self.test_data:
            self.assertTrue(1 <= record["quantity"] <= 500, f"Quantity {record['quantity']} out of range")

    def test_transaction_type(self):
        for record in self.test_data:
            self.assertIn(record["transaction_type"], ["inbound", "outbound"], f"Invalid transaction type {record['transaction_type']}")

    def test_transaction_date_range(self):
        for record in self.test_data:
            self.assertTrue(datetime.date(2023, 1, 1) <= record["transaction_date"] <= datetime.date(2023, 12, 31), f"Transaction date {record['transaction_date']} out of range")

    def test_supplier_id_range(self):
        for record in self.test_data:
            self.assertTrue(1 <= record["supplier_id"] <= 50, f"Supplier ID {record['supplier_id']} out of range")

    def test_warehouse_id_range(self):
        for record in self.test_data:
            self.assertTrue(1 <= record["warehouse_id"] <= 10, f"Warehouse ID {record['warehouse_id']} out of range")

    def test_unit_price_range(self):
        for record in self.test_data:
            self.assertTrue(10.0 <= record["unit_price"] <= 100.0, f"Unit price {record['unit_price']} out of range")

    def test_total_value_calculation(self):
        for record in self.test_data:
            expected_total_value = record["quantity"] * record["unit_price"]
            self.assertAlmostEqual(record["total_value"], expected_total_value, places=2, msg=f"Total value {record['total_value']} does not match expected {expected_total_value}")

    def test_status_options(self):
        for record in self.test_data:
            self.assertIn(record["status"], ["pending", "completed", "cancelled"], f"Invalid status {record['status']}")

if __name__ == '__main__':
    unittest.main()
