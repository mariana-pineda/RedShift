import unittest
from datetime import datetime

class TestDatabaseSchemaUpdates(unittest.TestCase):

    def setUp(self):
        # Assuming these functions are defined to interact with the database
        self.employee_test_data = generate_employee_data(25)
        self.customer_test_data = generate_customer_data(25)

    def test_lastdate_column_in_employees(self):
        for record in self.employee_test_data:
            employee_id = record['employee_id']
            lastdate = record['lastdate']
            
            # Fetch the record from the database
            db_record = fetch_employee_record(employee_id)
            
            # Validate the lastdate column exists
            self.assertIn('lastdate', db_record)
            
            # Validate the data type of lastdate
            if lastdate is not None:
                self.assertIsInstance(db_record['lastdate'], datetime)
                self.assertEqual(db_record['lastdate'].strftime('%Y-%m-%d'), lastdate)
            else:
                self.assertIsNone(db_record['lastdate'])

    def test_categoryGroup_column_in_customers(self):
        for record in self.customer_test_data:
            customer_id = record['customer_id']
            category_group = record['categoryGroup']
            
            # Fetch the record from the database
            db_record = fetch_customer_record(customer_id)
            
            # Validate the categoryGroup column exists
            self.assertIn('categoryGroup', db_record)
            
            # Validate the data type of categoryGroup
            if category_group is not None:
                self.assertIsInstance(db_record['categoryGroup'], str)
                self.assertEqual(db_record['categoryGroup'], category_group)
            else:
                self.assertIsNone(db_record['categoryGroup'])

def fetch_employee_record(employee_id):
    # Placeholder function to simulate fetching a record from the database
    # This should be replaced with actual database interaction code
    return {
        "employee_id": employee_id,
        "lastdate": datetime.now() if random.choice([True, False]) else None
    }

def fetch_customer_record(customer_id):
    # Placeholder function to simulate fetching a record from the database
    # This should be replaced with actual database interaction code
    return {
        "customer_id": customer_id,
        "categoryGroup": random.choice(['Retail', 'Wholesale', 'Online', 'Corporate', 'Government', None])
    }

if __name__ == '__main__':
    unittest.main()
