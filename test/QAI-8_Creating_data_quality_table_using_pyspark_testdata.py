from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, regexp_extract
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Data Quality Checks") \
    .getOrCreate()

# Define schema for the DQ table
dq_schema = StructType([
    StructField("check_no", IntegerType(), False),
    StructField("check_name", StringType(), False),
    StructField("dq_result", StringType(), False)
])

# Create an empty DataFrame for the DQ table
dq_df = spark.createDataFrame([], dq_schema)

# Load the d_product_revenue table
d_product_revenue_df = spark.table("agilisium_playground.purgo_playground.d_product_revenue")

# Happy Path Test Data: Valid scenarios
# Test case: All column names are correct
column_names_check = d_product_revenue_df.columns == [
    'product_id', 'product_name', 'product_type', 'revenue', 'country', 
    'customer_id', 'purchased_date', 'invoice_date', 'invoice_number', 
    'is_returned', 'customer_satisfaction_score', 'product_details'
]
dq_df = dq_df.union(spark.createDataFrame([(1, "Column Name Validation", "Pass" if column_names_check else "Fail")], dq_schema))

# Edge Case Test Data: Boundary conditions
# Test case: Revenue is exactly zero
revenue_zero_check = d_product_revenue_df.filter(col("revenue") == 0).count() == 0
dq_df = dq_df.union(spark.createDataFrame([(2, "Revenue Value Check", "Pass" if revenue_zero_check else "Fail")], dq_schema))

# Error Case Test Data: Invalid inputs
# Test case: Negative revenue values
negative_revenue_check = d_product_revenue_df.filter(col("revenue") < 0).count() == 0
dq_df = dq_df.union(spark.createDataFrame([(3, "Revenue Value Check", "Pass" if negative_revenue_check else "Fail")], dq_schema))

# Special Character and Format Test Data
# Test case: Revenue with incorrect decimal places
decimal_precision_check = d_product_revenue_df.filter(~regexp_extract(col("revenue").cast("string"), r"^\d+\.\d{2}$", 0).isNull()).count() == 0
dq_df = dq_df.union(spark.createDataFrame([(4, "Decimal Precision Check", "Pass" if decimal_precision_check else "Fail")], dq_schema))

# Show the DQ results
dq_df.show()

# Save the DQ results to the dq_check_table
dq_df.write.mode("overwrite").saveAsTable("agilisium_playground.purgo_playground.dq_check_table")


This PySpark script performs data quality checks on the `d_product_revenue` table and logs the results in a Data Quality (DQ) table. The checks include:

1. **Column Name Validation**: Ensures all expected column names are present.
2. **Revenue Value Check**: Ensures no negative revenue values and checks for zero revenue as an edge case.
3. **Decimal Precision Check**: Ensures revenue values have exactly two decimal places.

The results are stored in the `dq_check_table` with columns `check_no`, `check_name`, and `dq_result`.