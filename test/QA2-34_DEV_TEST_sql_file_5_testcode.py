import unittest
from datetime import datetime
from test_data import happy_path_data, edge_case_data, error_case_data, special_character_data

class TestJiraForgeApp(unittest.TestCase):

    def setUp(self):
        # Setup code if needed
        pass

    def tearDown(self):
        # Teardown code if needed
        pass

    # Test happy path scenarios
    def test_happy_path_data(self):
        for data in happy_path_data:
            # Simulate data insertion and retrieval
            result = self.simulate_database_interaction(data)
            # Assert expected vs actual
            self.assertEqual(result['program_id'], data['program_id'])
            self.assertEqual(result['program_name'], data['program_name'])
            self.assertEqual(result['country_code'], data['country_code'])
            self.assertEqual(result['program_start_date'], data['program_start_date'])

    # Test edge case scenarios
    def test_edge_case_data(self):
        for data in edge_case_data:
            # Simulate data insertion and retrieval
            result = self.simulate_database_interaction(data)
            # Assert expected vs actual
            self.assertEqual(result['program_id'], data['program_id'])
            self.assertEqual(result['program_name'], data['program_name'])
            self.assertEqual(result['country_code'], data['country_code'])
            self.assertEqual(result['program_start_date'], data['program_start_date'])

    # Test error case scenarios
    def test_error_case_data(self):
        for data in error_case_data:
            with self.assertRaises(ValueError):
                # Simulate data insertion that should raise an error
                self.simulate_database_interaction(data)

    # Test special character scenarios
    def test_special_character_data(self):
        for data in special_character_data:
            # Simulate data insertion and retrieval
            result = self.simulate_database_interaction(data)
            # Assert expected vs actual
            self.assertEqual(result['program_id'], data['program_id'])
            self.assertEqual(result['program_name'], data['program_name'])
            self.assertEqual(result['country_code'], data['country_code'])
            self.assertEqual(result['program_start_date'], data['program_start_date'])

    def simulate_database_interaction(self, data):
        # Simulate database interaction and return the data as if it was retrieved
        # This is a placeholder for actual database logic
        if data['program_id'] < 0 or not isinstance(data['program_id'], int):
            raise ValueError("Invalid program_id")
        if data['program_name'] is None or not isinstance(data['program_name'], str):
            raise ValueError("Invalid program_name")
        if data['country_code'] is None or not isinstance(data['country_code'], str):
            raise ValueError("Invalid country_code")
        if not isinstance(data['program_start_date'], datetime):
            raise ValueError("Invalid program_start_date")
        return data

if __name__ == '__main__':
    unittest.main()
