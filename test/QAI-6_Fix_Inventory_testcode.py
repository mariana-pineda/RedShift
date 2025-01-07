import unittest
from datetime import datetime

class TestDatabaseSchema(unittest.TestCase):

    def test_employees_table_lastdate(self):
        # Assuming we have a function get_employee_schema() that returns the schema of the employees table
        schema = get_employee_schema()
        self.assertIn('lastdate', schema, "Column 'lastdate' should exist in employees table")
        self.assertIn(schema['lastdate']['type'], ['DATE', 'DATETIME'], "Column 'lastdate' should be of type DATE or DATETIME")
        self.assertTrue(schema['lastdate']['nullable'] or 'default' in schema['lastdate'], "Column 'lastdate' should allow NULL values or have a default value")

    def test_customers_table_categoryGroup(self):
        # Assuming we have a function get_customer_schema() that returns the schema of the customers table
        schema = get_customer_schema()
        self.assertIn('categoryGroup', schema, "Column 'categoryGroup' should exist in customers table")
        self.assertIn(schema['categoryGroup']['type'], ['VARCHAR', 'INT'], "Column 'categoryGroup' should be of type VARCHAR or INT")
        self.assertTrue(schema['categoryGroup']['nullable'] or 'default' in schema['categoryGroup'], "Column 'categoryGroup' should allow NULL values or have a default value")
        self.assertTrue('possible_values' in schema['categoryGroup'], "Possible values for 'categoryGroup' should be defined and documented")

    def test_employee_data(self):
        employee_test_data = generate_employee_data(25)
        for record in employee_test_data:
            if record['lastdate'] is not None:
                try:
                    datetime.strptime(record['lastdate'], '%Y-%m-%d')
                except ValueError:
                    self.fail(f"lastdate '{record['lastdate']}' is not a valid DATE format")

    def test_customer_data(self):
        customer_test_data = generate_customer_data(25)
        category_groups = ['Retail', 'Wholesale', 'Online', 'Corporate']
        for record in customer_test_data:
            if record['categoryGroup'] is not None:
                self.assertIn(record['categoryGroup'], category_groups, f"categoryGroup '{record['categoryGroup']}' is not a valid category")

if __name__ == '__main__':
    unittest.main()
