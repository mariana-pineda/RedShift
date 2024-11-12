import unittest

class TestDatabaseSchemaUpdates(unittest.TestCase):

    def setUp(self):
        # Assuming `employees_test_data` and `customers_test_data` are already available from the test data code
        self.employees_test_data = employees_test_data
        self.customers_test_data = customers_test_data

    def test_employees_lastdate_column(self):
        for employee in self.employees_test_data:
            self.assertIn("lastdate", employee, "The 'lastdate' column is missing in the employees data.")
            self.assertTrue(isinstance(employee["lastdate"], (datetime, type(None))), 
                            "The 'lastdate' should be of type 'timestamp' or 'None'.")

    def test_customers_categoryGroup_column(self):
        for customer in self.customers_test_data:
            self.assertIn("categoryGroup", customer, "The 'categoryGroup' column is missing in the customers data.")
            self.assertTrue(isinstance(customer["categoryGroup"], (str, type(None))), 
                            "The 'categoryGroup' should be of type 'string' or 'None'.")

if __name__ == '__main__':
    unittest.main()
