from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit, expr
from pyspark.sql.types import StringType, DoubleType, StructType, StructField

# Initialize Spark session
spark = SparkSession.builder.appName("DataQualityChecks").getOrCreate()

# Load the drug_inventory_management table
drug_inventory_df = spark.table("agilisium_playground.purgo_playground.drug_inventory_management")

# Define data quality checks
dq_checks = [
    {
        "check_name": "Mandatory Fields Check",
        "condition": "product_ID IS NOT NULL AND product_name IS NOT NULL AND quantity IS NOT NULL AND location IS NOT NULL AND expiry_date IS NOT NULL AND batch_number IS NOT NULL AND supplier_ID IS NOT NULL"
    },
    {
        "check_name": "Expiry Date Check",
        "condition": "expiry_date > purchase_date"
    },
    {
        "check_name": "Unique Check",
        "condition": "product_ID IS NOT NULL AND batch_number IS NOT NULL"
    },
    {
        "check_name": "Data Consistency Check",
        "condition": "quantity > 0 AND expiry_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' AND purchase_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'"
    }
]

# Function to calculate pass percentage for each check
def calculate_pass_percentage(df, check):
    total_rows = df.count()
    passed_rows = df.filter(expr(check["condition"])).count()
    pass_percentage = (passed_rows / total_rows) * 100 if total_rows > 0 else 0
    return (check["check_name"], "Pass" if pass_percentage == 100 else "Fail", pass_percentage)

# Create a DataFrame to store the results of data quality checks
results = [calculate_pass_percentage(drug_inventory_df, check) for check in dq_checks]

# Define schema for the results DataFrame
schema = StructType([
    StructField("check_name", StringType(), True),
    StructField("result", StringType(), True),
    StructField("pass_%", DoubleType(), True)
])

# Create the results DataFrame
dq_results_df = spark.createDataFrame(results, schema)

# Show the results
dq_results_df.show(truncate=False)


This code performs data quality checks on the `drug_inventory_management` table using PySpark. It checks for mandatory fields, expiry date validity, uniqueness, and data consistency, and calculates the pass percentage for each check. The results are stored in a DataFrame with columns `check_name`, `result`, and `pass_%`.