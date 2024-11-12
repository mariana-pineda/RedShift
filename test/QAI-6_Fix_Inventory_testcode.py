import unittest

class TestDatabaseUpdates(unittest.TestCase):
    def setUp(self):
        self.employees_test_data = employees_test_data
        self.customers_test_data = customers_test_data

    def test_employees_lastdate_column(self):
        for employee in self.employees_test_data:
            self.assertIn("lastdate", employee)
            self.assertTrue(isinstance(employee["lastdate"], (datetime, type(None))))

    def test_customers_categoryGroup_column(self):
        category_groups = ["Bronze", "Silver", "Gold", "Platinum"]
        for customer in self.customers_test_data:
            self.assertIn("categoryGroup", customer)
            if customer["categoryGroup"] is not None:
                self.assertIn(customer["categoryGroup"], category_groups)

if __name__ == '__main__':
    unittest.main()
