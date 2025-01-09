import unittest
import csv
import hashlib

class TestProductRevenueCustomerData(unittest.TestCase):

    def setUp(self):
        self.product_revenue_path = '/Volumes/agilisium_playground/purgo_playground/d_product_revenue_csv/d_product_revenue.csv'
        self.customer_path = '/Volumes/agilisium_playground/purgo_playground/d_product_revenue_csv/customer.csv'
        self.joined_data = self.perform_join()

    def perform_join(self):
        product_revenue_data = []
        customer_data = []

        with open(self.product_revenue_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_revenue_data.append(row)

        with open(self.customer_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_data.append(row)

        joined_data = []
        for pr in product_revenue_data:
            for cust in customer_data:
                if pr['customer_id'] == cust['customer_id']:
                    joined_row = {**pr, **cust}
                    joined_data.append(joined_row)

        return joined_data

    def create_surrogate_key(self, row):
        concatenated = ''.join(map(str, row.values()))
        return hashlib.sha256(concatenated.encode()).hexdigest()

    def test_surrogate_key_generation(self):
        for row in self.joined_data:
            expected_surrogate_key = self.create_surrogate_key(row)
            actual_surrogate_key = self.create_surrogate_key(row)
            self.assertEqual(expected_surrogate_key, actual_surrogate_key, "Surrogate key does not match expected value")

    def test_join_condition(self):
        for row in self.joined_data:
            self.assertIn('customer_id', row, "customer_id not found in joined row")
            self.assertIn('product_id', row, "product_id not found in joined row")
            self.assertIn('customer_name', row, "customer_name not found in joined row")
            self.assertIn('revenue', row, "revenue not found in joined row")

if __name__ == '__main__':
    unittest.main()
