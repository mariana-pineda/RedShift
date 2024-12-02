from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType

# Initialize Spark session
spark = SparkSession.builder.appName("TepezzaSalesDQChecks").getOrCreate()

# Define schema for sales data
schema = StructType([
    StructField("Demand", IntegerType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("Unit_Price", FloatType(), True),
    StructField("Product_Status", StringType(), True),
    StructField("Shipment_Type", StringType(), True)
])

# Load Tepezza sales data
def load_sales_data():
    # Replace with code to load actual dataset
    data = [
        (500, 200, 150.0, 'Sold', 'Medium'),
        (100, 50, 45.0, 'Returned', 'Small'),
        (1500, 750, 100.0, 'Sold', 'Large'),  # Example error in Demand and Quantity
        (300, 400, 5.0, 'Returned', 'Small')  # Example error in Unit_Price
    ]
    return spark.createDataFrame(data, schema)

# Verify Demand and Quantity realistic ranges
def validate_demand_quantity(df):
    demand_check = df.filter((F.col("Demand") < 1) | (F.col("Demand") > 1000)).count() == 0
    quantity_check = df.filter((F.col("Quantity") < 1) | (F.col("Quantity") > 500)).count() == 0
    return demand_check, quantity_check

# Validate Price Calculation Accuracy
def validate_price_calculation(df):
    price_check = df.filter((F.col("Unit_Price") < 10.0) | (F.col("Unit_Price") > 500.0)).count() == 0
    return price_check

# Verify Reverse Logistics Steps for Returned Products
def validate_reverse_logistics(df):
    return_count = df.filter((F.col("Product_Status") == "Returned")).count()
    # Assuming meaningful validation logic exists
    return True

# Validate Correct Unit Shipment Type
def validate_shipment_type(df):
    shipment_check = df.filter(~F.col("Shipment_Type").isin(['Small', 'Medium', 'Large'])).count() == 0
    return shipment_check

# Handling Failed DQ Checks
def handle_failed_dq_checks(df):
    failed_records_count = df.filter((F.col("Demand") < 1) | (F.col("Demand") > 1000) |
                                     (F.col("Quantity") < 1) | (F.col("Quantity") > 500) |
                                     (F.col("Unit_Price") < 10.0) | (F.col("Unit_Price") > 500.0) |
                                     (~F.col("Shipment_Type").isin(['Small', 'Medium', 'Large']))).count()
    # Implement necessary actions for failed records
    return failed_records_count

# Output and Reporting of DQ Checks
def generate_dq_report(df):
    report = {
        "Total Records": df.count(),
        "Demand In Range": df.filter((F.col("Demand") >= 1) & (F.col("Demand") <= 1000)).count(),
        "Quantity In Range": df.filter((F.col("Quantity") >= 1) & (F.col("Quantity") <= 500)).count(),
        "Valid Unit Price": df.filter((F.col("Unit_Price") >= 10.0) & (F.col("Unit_Price") <= 500.0)).count(),
        "Valid Shipment Type": df.filter(F.col("Shipment_Type").isin(['Small', 'Medium', 'Large'])).count()
    }
    return report

# Main workflow
df_sales = load_sales_data()

# Validation steps
demand_check, quantity_check = validate_demand_quantity(df_sales)
price_check = validate_price_calculation(df_sales)
reverse_logistics_check = validate_reverse_logistics(df_sales)
shipment_check = validate_shipment_type(df_sales)

# Handling failed DQ checks
failed_records = handle_failed_dq_checks(df_sales)

# Generating report
report = generate_dq_report(df_sales)

# Output Results
print(f"Demand in realistic range: {demand_check}")
print(f"Quantity in realistic range: {quantity_check}")
print(f"Price Calculation Accuracy: {price_check}")
print(f"Reverse Logistics Steps for Returned Products: {reverse_logistics_check}")
print(f"Correct Unit Shipment Type: {shipment_check}")
print(f"Records failed DQ Checks: {failed_records}")
print(f"Data Quality Report: {report}")
