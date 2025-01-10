import unittest
from datetime import datetime
from collections import Counter

class TestDatabaseSchemaModifications(unittest.TestCase):

    def setUp(self):
        self.employee_data = generate_employee_data(25)
        self.customer_data = generate_customer_data(25)

    def test_lastdate_column_in_employees(self):
        for employee in self.employee_data:
            self.assertIn("LastDate", employee)
            self.assertIsInstance(employee["LastDate"], datetime)
            self.assertEqual(employee["LastDate"], datetime.now().date())

    def test_categoryGroup_column_in_customers(self):
        valid_categories = {"VIP", "Regular", "New", "Uncategorized"}
        for customer in self.customer_data:
            self.assertIn("CategoryGroup", customer)
            self.assertIsInstance(customer["CategoryGroup"], str)
            self.assertIn(customer["CategoryGroup"], valid_categories)

    def test_default_categoryGroup_for_existing_customers(self):
        category_counts = Counter(cust["CategoryGroup"] for cust in self.customer_data)
        self.assertGreaterEqual(category_counts["Uncategorized"], 1)

if __name__ == '__main__':
    unittest.main()
