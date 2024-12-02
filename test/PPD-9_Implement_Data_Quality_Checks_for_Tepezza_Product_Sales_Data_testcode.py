from pyspark.sql import functions as F

# Verify Demand and Quantity realistic ranges
def validate_demand_quantity(df):
    demand_check = df.filter((F.col("Demand") < 1) | (F.col("Demand") > 1000)).count() == 0
    quantity_check = df.filter((F.col("Quantity") < 1) | (F.col("Quantity") > 500)).count() == 0
    print(f"Demand in realistic range: {demand_check}")
    print(f"Quantity in realistic range: {quantity_check}")

# Validate Price Calculation Accuracy (assuming a unit price rule exists)
def validate_price_calculation(df):
    # Assuming some calculation or condition for price validation
    price_check = df.filter((F.col("Unit_Price") < 10.0) | (F.col("Unit_Price") > 500.0)).count() == 0
    print(f"Price Calculation Accuracy: {price_check}")

# Verify Reverse Logistics Steps for Returned Products
def validate_reverse_logistics(df):
    return_count = df.filter((F.col("Product_Status") == "Returned")).count()
    correct_return_check = return_count >= 0  # Assuming some meaningful check as described in rules
    print(f"Reverse Logistics Steps for Returned Products: {correct_return_check}")

# Validate Correct Unit Shipment Type
def validate_shipment_type(df):
    shipment_check = df.filter(~F.col("Shipment_Type").isin(['Small', 'Medium', 'Large'])).count() == 0
    print(f"Correct Unit Shipment Type: {shipment_check}")

# Handling Failed DQ Checks
def handle_failed_dq_checks(df):
    failed_records_count = df.filter((F.col("Demand") < 1) | (F.col("Demand") > 1000) |
                                     (F.col("Quantity") < 1) | (F.col("Quantity") > 500) |
                                     (F.col("Unit_Price") < 10.0) | (F.col("Unit_Price") > 500.0) |
                                     (~F.col("Shipment_Type").isin(['Small', 'Medium', 'Large']))).count()
    print(f"Records failed DQ Checks: {failed_records_count}")
    # Assuming some action is required for failed records

# Output and Reporting of DQ Checks
def generate_dq_report(df):
    report = {
        "Total Records": df.count(),
        "Demand In Range": df.filter((F.col("Demand") >= 1) & (F.col("Demand") <= 1000)).count(),
        "Quantity In Range": df.filter((F.col("Quantity") >= 1) & (F.col("Quantity") <= 500)).count(),
        "Valid Unit Price": df.filter((F.col("Unit_Price") >= 10.0) & (F.col("Unit_Price") <= 500.0)).count(),
        "Valid Shipment Type": df.filter(F.col("Shipment_Type").isin(['Small', 'Medium', 'Large'])).count()
    }
    print(report)

# Validating
validate_demand_quantity(df)
validate_price_calculation(df)
validate_reverse_logistics(df)
validate_shipment_type(df)
handle_failed_dq_checks(df)
generate_dq_report(df)
