import unittest
import datetime
import psycopg2

class TestDatabaseSchema(unittest.TestCase):
    
    def setUp(self):
        # Set up database connection
        self.connection = psycopg2.connect(
            dbname='qa',
            user='user',
            password='password',
            host='localhost'
        )
        self.cursor = self.connection.cursor()

    def test_lastdate_column_in_employees(self):
        # Check if lastdate column exists and is of date type
        self.cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='employees' AND column_name='lastdate'")
        column = self.cursor.fetchone()
        self.assertIsNotNone(column)
        self.assertEqual(column[1], 'date')
        
        # Check default value of lastdate
        self.cursor.execute("SELECT column_default FROM information_schema.columns WHERE table_name='employees' AND column_name='lastdate'")
        default_value = self.cursor.fetchone()
        self.assertIsNotNone(default_value)
        self.assertIn("now()", default_value[0])

        # Check existing records have default lastdate
        self.cursor.execute("SELECT lastdate FROM employees")
        records = self.cursor.fetchall()
        for record in records:
            self.assertEqual(record[0], datetime.date.today())

    def test_categoryGroup_column_in_customers(self):
        # Check if categoryGroup column exists and is of string type
        self.cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='customers' AND column_name='categorygroup'")
        column = self.cursor.fetchone()
        self.assertIsNotNone(column)
        self.assertEqual(column[1], 'character varying')

        # Validate default value for categoryGroup
        self.cursor.execute("SELECT column_default FROM information_schema.columns WHERE table_name='customers' AND column_name='categorygroup'")
        default_value = self.cursor.fetchone()
        self.assertIsNotNone(default_value)
        self.assertEqual(default_value[0], "'Uncategorized'::character varying")

        # Validate predefined categories
        valid_categories = {"VIP", "Regular", "New"}
        self.cursor.execute("SELECT DISTINCT categorygroup FROM customers")
        categories = self.cursor.fetchall()
        for category in categories:
            self.assertIn(category[0], valid_categories.union({"Uncategorized"}))

    def tearDown(self):
        # Close database connection
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
