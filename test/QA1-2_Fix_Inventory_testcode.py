import unittest
from datetime import datetime

class TestDatabaseModifications(unittest.TestCase):

    def setUp(self):
        # Assuming employees_data and customers_data are imported or available here
        self.employees_data = employees_data
        self.customers_data = customers_data

    def test_employees_lastdate_column(self):
        for employee in self.employees_data:
            with self.subTest(employee=employee):
                # Check if LastDate is a valid timestamp
                self.assertIsInstance(employee['LastDate'], datetime, "LastDate is not a valid timestamp")

    def test_customers_categoryGroup_column(self):
        valid_groups = ["GroupA", "GroupB", "GroupC", "GroupD"]
        for customer in self.customers_data:
            with self.subTest(customer=customer):
                # Check if CategoryGroup is a valid string and in valid_groups
                self.assertIn(customer['CategoryGroup'], valid_groups, "CategoryGroup is not valid")

if __name__ == '__main__':
    unittest.main()
