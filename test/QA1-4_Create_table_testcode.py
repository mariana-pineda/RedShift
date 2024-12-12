import unittest
import datetime
from sqlalchemy import create_engine, inspect, MetaData, Table, Column, Date, String

class TestDatabaseSchema(unittest.TestCase):

    def setUp(self):
        # Setup in-memory SQLite database for testing
        self.engine = create_engine('sqlite:///:memory:')
        self.metadata = MetaData()

        # Create employees table without lastdate column
        self.employees = Table('employees', self.metadata,
                               Column('employee_id', String, primary_key=True))
        self.metadata.create_all(self.engine)

        # Create customers table without categoryGroup column
        self.customers = Table('customers', self.metadata,
                               Column('customer_id', String, primary_key=True))
        self.metadata.create_all(self.engine)

    def test_add_lastdate_column_to_employees(self):
        # Add lastdate column to employees table
        with self.engine.connect() as conn:
            conn.execute('ALTER TABLE employees ADD COLUMN lastdate DATE DEFAULT "2023-01-01"')

        # Verify lastdate column is added
        inspector = inspect(self.engine)
        columns = inspector.get_columns('employees')
        column_names = [column['name'] for column in columns]
        self.assertIn('lastdate', column_names)

        # Verify data type of lastdate column
        lastdate_column = next(column for column in columns if column['name'] == 'lastdate')
        self.assertEqual(lastdate_column['type'].__class__, Date)

        # Verify default value for existing records
        with self.engine.connect() as conn:
            conn.execute('INSERT INTO employees (employee_id) VALUES ("1")')
            result = conn.execute('SELECT lastdate FROM employees WHERE employee_id = "1"').fetchone()
            self.assertEqual(result['lastdate'], datetime.date(2023, 1, 1))

    def test_add_categoryGroup_column_to_customers(self):
        # Add categoryGroup column to customers table
        with self.engine.connect() as conn:
            conn.execute('ALTER TABLE customers ADD COLUMN categoryGroup STRING DEFAULT "A"')

        # Verify categoryGroup column is added
        inspector = inspect(self.engine)
        columns = inspector.get_columns('customers')
        column_names = [column['name'] for column in columns]
        self.assertIn('categoryGroup', column_names)

        # Verify data type of categoryGroup column
        categoryGroup_column = next(column for column in columns if column['name'] == 'categoryGroup')
        self.assertEqual(categoryGroup_column['type'].__class__, String)

        # Verify default value for existing records
        with self.engine.connect() as conn:
            conn.execute('INSERT INTO customers (customer_id) VALUES ("1")')
            result = conn.execute('SELECT categoryGroup FROM customers WHERE customer_id = "1"').fetchone()
            self.assertEqual(result['categoryGroup'], "A")

if __name__ == '__main__':
    unittest.main()
