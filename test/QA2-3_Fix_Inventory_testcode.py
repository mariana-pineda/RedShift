import unittest
from datetime import datetime

class TestDatabaseSchema(unittest.TestCase):

    def test_employees_lastdate(self):
        for employee in employees_data:
            # Check if lastdate is of date type
            self.assertIsInstance(employee['lastdate'], datetime.date)
            # Check if lastdate default value is current date
            self.assertEqual(employee['lastdate'], datetime.now().date())

    def test_customers_categoryGroup(self):
        valid_categories = {"VIP", "Regular", "New", "Uncategorized"}
        for customer in customers_data:
            # Check if categoryGroup is a string
            self.assertIsInstance(customer['categoryGroup'], str)
            # Check if categoryGroup contains valid categories
            self.assertIn(customer['categoryGroup'], valid_categories)

if __name__ == '__main__':
    unittest.main()
