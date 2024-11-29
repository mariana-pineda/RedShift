import random
import datetime
import pandas as pd

# Generate data for d_product table
def generate_d_product_data(num_records=30):
    d_product_data = []
    for i in range(1, num_records + 1):
        prod_id = f'P{i:03d}'
        prod_id_sn = f'SN{i:03d}'
        d_product_data.append({'prod_id': prod_id, 'prod_id_sn': prod_id_sn, 'last_refreshed': datetime.datetime.now()})
    return pd.DataFrame(d_product_data)

# Generate data for d_product_sk table
def generate_d_product_sk_data(num_records=20):
    d_product_sk_data = []
    for i in range(1, num_records + 1):
        prod_id = f'P{i:03d}'
        plant_key_sn = i + 1000    # Start plant_key_sn from 1001 for existing records
        d_product_sk_data.append({'prod_id': prod_id, 'plant_key_sn': plant_key_sn})
    return pd.DataFrame(d_product_sk_data)

# Test Data for "Delete records in d_product_sk that exist in d_product"
d_product_data_delete = generate_d_product_data(20)  # Condition: d_product table has refreshed data
d_product_sk_data_delete = generate_d_product_sk_data(10)  # Records with matching prod_id will be deleted

# Test Data for "Insert missing records into d_product_sk"
d_product_data_insert = generate_d_product_data(30)  # Condition: d_product table has refreshed data
d_product_sk_data_insert = generate_d_product_sk_data(10)  # Insert non-matching prod_id and increment plant_key_sn

# Test Data for "Handle non-unique prod_id in d_product"
d_product_data_duplicate = generate_d_product_data(20)
# Introduce duplicate prod_id entries
for _ in range(5):
    d_product_data_duplicate = d_product_data_duplicate.append({'prod_id': 'P001', 'prod_id_sn': f'SN{random.randint(21, 30):03d}', 'last_refreshed': datetime.datetime.now()}, ignore_index=True)

# Test Data for "Log errors during synchronization"
d_product_data_error = generate_d_product_data(5)  # Data to simulate error condition

# Test Data for "Ensure performance efficiency"
d_product_data_performance = generate_d_product_data(50)  # Simulate larger table sizes
d_product_sk_data_performance = generate_d_product_sk_data(50)

# Output test data frames for verification purposes during testing
print("d_product_data_delete:\n", d_product_data_delete)
print("d_product_sk_data_delete:\n", d_product_sk_data_delete)
print("d_product_data_insert:\n", d_product_data_insert)
print("d_product_sk_data_insert:\n", d_product_sk_data_insert)
print("d_product_data_duplicate:\n", d_product_data_duplicate)
print("d_product_data_error:\n", d_product_data_error)
print("d_product_data_performance:\n", d_product_data_performance)
print("d_product_sk_data_performance:\n", d_product_sk_data_performance)

