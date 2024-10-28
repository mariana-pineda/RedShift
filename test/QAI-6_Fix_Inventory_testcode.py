import unittest
import datetime

class TestDatabaseSchema(unittest.TestCase):

    def setUp(self):
        self.employees_data = generate_employees_data(25)
        self.customers_data = generate_customers_data(25)

    def test_employees_lastdate_column(self):
        for employee in self.employees_data:
            lastdate = employee.get("LastDate")
            # lastdate should be None or a timestamp
            self.assertTrue(
                lastdate is None or isinstance(lastdate, datetime.datetime),
                f"LastDate validation failed for {lastdate}"
            )

    def test_customers_categoryGroup_column(self):
        for customer in self.customers_data:
            category_group = customer.get("CategoryGroup")
            # categoryGroup should be None or a string
            self.assertTrue(
                category_group is None or isinstance(category_group, str),
                f"CategoryGroup validation failed for {category_group}"
            )

if __name__ == '__main__':
    unittest.main()
