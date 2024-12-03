import unittest

class TestAllocatedQtyCalculation(unittest.TestCase):

    def setUp(self):
        # Simulate the f_order_df DataFrame preparation
        num_records = 30
        order_nbrs = [f'ORD{i:03}' for i in range(num_records)]
        order_line_nbrs = [f'LN{i:02}' for i in range(num_records)]
        
        # Helper function to generate random quantities, considering NULLs and negatives
        def generate_quantity():
            if random.random() < 0.1:
                return None
            value = random.randint(-50, 100)
            return value if random.random() > 0.2 else None
        
        # Generate the test data
        data_records = []
        for i in range(num_records):
            order_nbr = random.choice(order_nbrs)
            order_line_nbr = random.choice(order_line_nbrs)
            primary_qty = generate_quantity()
            open_qty = generate_quantity()
            shipped_qty = generate_quantity()
            cancel_qty = generate_quantity()
            record = {
                'order_nbr': order_nbr,
                'order_line_nbr': order_line_nbr,
                'primary_qty': primary_qty,
                'open_qty': open_qty,
                'shipped_qty': shipped_qty,
                'cancel_qty': cancel_qty
            }
            data_records.append(record)

        self.f_order_df = pd.DataFrame(data_records)

    def test_calculate_allocated_qty(self):
        # Expected allocated_qty calculation method
        def calculate_expected_allocated_qty(row):
            primary_qty = max(row['primary_qty'] or 0, 0)
            open_qty = max(row['open_qty'] or 0, 0)
            shipped_qty = max(row['shipped_qty'] or 0, 0)
            cancel_qty = max(row['cancel_qty'] or 0, 0)
            return primary_qty + open_qty + shipped_qty + cancel_qty

        # Apply the expected calculation
        self.f_order_df['expected_allocated_qty'] = self.f_order_df.apply(calculate_expected_allocated_qty, axis=1)
        
        # Validate each row's allocated_qty
        for index, row in self.f_order_df.iterrows():
            expected_value = row['expected_allocated_qty']
            self.assertEqual(row['allocated_qty'], expected_value, 
                             f"Mismatch in allocated_qty for order_nbr: {row['order_nbr']}, expected: {expected_value}, actual: {row['allocated_qty']}")
        
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
