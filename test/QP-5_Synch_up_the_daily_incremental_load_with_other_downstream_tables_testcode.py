import pandas as pd

def validate_synchronization_delete(d_product_data, d_product_sk_data):
    expected_result = d_product_sk_data[~d_product_sk_data['prod_id'].isin(d_product_data['prod_id'])]
    actual_result = synchronize_delete(d_product_data, d_product_sk_data)
    assert actual_result.equals(expected_result), "Test failed for deletion logic"


def validate_synchronization_insert(d_product_data, d_product_sk_data):
    max_plant_key_sn = d_product_sk_data['plant_key_sn'].max()
    missing_records = d_product_data[~d_product_data['prod_id'].isin(d_product_sk_data['prod_id'])]
    new_entries = missing_records.assign(plant_key_sn=range(max_plant_key_sn + 1, max_plant_key_sn + 1 + len(missing_records)))
    expected_result = pd.concat([d_product_sk_data, new_entries[['prod_id', 'plant_key_sn']]])
    actual_result = synchronize_insert(d_product_data, d_product_sk_data)
    assert actual_result.equals(expected_result), "Test failed for insertion logic"


def validate_non_unique_prod_id_handling(d_product_data):
    try:
        handle_non_unique_prod_id(d_product_data)
    except Exception as e:
        assert False, f"Test failed due to exception: {e}"


def validate_error_logging():
    try:
        simulate_error_condition()
    except Exception as e:
        assert log_error(e), "Test failed for error logging"


def validate_performance_efficiency(d_product_data, d_product_sk_data):
    import time
    start_time = time.perf_counter()
    synchronize_process(d_product_data, d_product_sk_data)
    end_time = time.perf_counter()
    duration = end_time - start_time
    assert duration < expected_performance_threshold, "Performance test failed"


d_product_data_delete = generate_d_product_data(20)
d_product_sk_data_delete = generate_d_product_sk_data(10)
validate_synchronization_delete(d_product_data_delete, d_product_sk_data_delete)

d_product_data_insert = generate_d_product_data(30)
d_product_sk_data_insert = generate_d_product_sk_data(10)
validate_synchronization_insert(d_product_data_insert, d_product_sk_data_insert)

d_product_data_duplicate = generate_d_product_data(20)
for _ in range(5):
    d_product_data_duplicate = d_product_data_duplicate.append({'prod_id': 'P001', 'prod_id_sn': f'SN{random.randint(21, 30):03d}', 'last_refreshed': datetime.datetime.now()}, ignore_index=True)
validate_non_unique_prod_id_handling(d_product_data_duplicate)

validate_error_logging()

d_product_data_performance = generate_d_product_data(50)
d_product_sk_data_performance = generate_d_product_sk_data(50)
validate_performance_efficiency(d_product_data_performance, d_product_sk_data_performance)

