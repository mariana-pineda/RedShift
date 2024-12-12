import unittest
import sqlite3

class TestDatabaseSchema(unittest.TestCase):

    def setUp(self):
        # Set up an in-memory SQLite database for testing
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        
        # Create employees and customers tables
        self.cursor.execute('''
            CREATE TABLE employees (
                employee_id INTEGER PRIMARY KEY,
                lastdate DATE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE customers (
                customer_id INTEGER PRIMARY KEY,
                categoryGroup TEXT
            )
        ''')
        self.connection.commit()

    def tearDown(self):
        # Close the database connection after each test
        self.connection.close()

    def test_employees_table_has_lastdate_column(self):
        # Check if the lastdate column exists in the employees table
        self.cursor.execute("PRAGMA table_info(employees)")
        columns = [column[1] for column in self.cursor.fetchall()]
        self.assertIn('lastdate', columns, "lastdate column is missing in employees table")

    def test_customers_table_has_categoryGroup_column(self):
        # Check if the categoryGroup column exists in the customers table
        self.cursor.execute("PRAGMA table_info(customers)")
        columns = [column[1] for column in self.cursor.fetchall()]
        self.assertIn('categoryGroup', columns, "categoryGroup column is missing in customers table")

    def test_employees_data_insertion(self):
        # Insert test data into employees table and validate
        employees_test_data = generate_employees_data(25)
        for record in employees_test_data:
            self.cursor.execute('''
                INSERT INTO employees (employee_id, lastdate) VALUES (?, ?)
            ''', (record['employee_id'], record['lastdate']))
        self.connection.commit()

        # Validate data insertion
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 25, "Not all employees test data were inserted")

    def test_customers_data_insertion(self):
        # Insert test data into customers table and validate
        customers_test_data = generate_customers_data(25)
        for record in customers_test_data:
            self.cursor.execute('''
                INSERT INTO customers (customer_id, categoryGroup) VALUES (?, ?)
            ''', (record['customer_id'], record['categoryGroup']))
        self.connection.commit()

        # Validate data insertion
        self.cursor.execute("SELECT * FROM customers")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 25, "Not all customers test data were inserted")

if __name__ == '__main__':
    unittest.main()
