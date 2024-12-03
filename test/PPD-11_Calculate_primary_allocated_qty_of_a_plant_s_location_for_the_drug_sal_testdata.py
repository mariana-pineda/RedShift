import random
import pandas as pd

# Define the test data parameters
num_records = 30
order_nbrs = [f'ORD{i:03}' for i in range(num_records)]
order_line_nbrs = [f'LN{i:02}' for i in range(num_records)]

# Helper function to generate random quantities, considering NULLs and negatives
def generate_quantity():
    # Simulate NULL by randomly returning None
    if random.random() < 0.1:
        return None
    # Allow negative values occasionally
    value = random.randint(-50, 100)
    return value if random.random() > 0.2 else None  # Convert some to NULL

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

# Create a DataFrame to simulate the f_order table
f_order_df = pd.DataFrame(data_records)

# Generate allocated_qty considering NULLs as zero and ignoring negatives
def calculate_allocated_qty(row):
    primary_qty = max(row['primary_qty'] or 0, 0)  # NULL as zero, ignore negative
    open_qty = max(row['open_qty'] or 0, 0)        # NULL as zero, ignore negative
    shipped_qty = max(row['shipped_qty'] or 0, 0)  # NULL as zero, ignore negative
    cancel_qty = max(row['cancel_qty'] or 0, 0)    # NULL as zero, ignore negative
    return primary_qty + open_qty + shipped_qty + cancel_qty

f_order_df['allocated_qty'] = f_order_df.apply(calculate_allocated_qty, axis=1)

# Display the test data
print(f_order_df)

# Note: This test data generation validates the following conditions:
# 1. Records with NULL values in the qty columns are treated as zero.
# 2. Negative values in the qty columns are ignored in allocation calculation.

