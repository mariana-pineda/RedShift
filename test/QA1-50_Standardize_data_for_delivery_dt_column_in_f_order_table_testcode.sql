-- Test Code for Databricks Environment

/* SQL Test for delivery_dt format validation */
-- Validate that delivery_dt is in the format yyyymmdd and is a DECIMAL(38, 0)
SELECT COUNT(*) AS invalid_count
FROM purgo_playground.f_order
WHERE CAST(delivery_dt AS STRING) NOT RLIKE '^[0-9]{8}$';

-- Assert that there are no invalid delivery_dt formats
SELECT CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END AS validation_result
FROM purgo_playground.f_order
WHERE CAST(delivery_dt AS STRING) NOT RLIKE '^[0-9]{8}$';



# PySpark Test for Schema Validation
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DecimalType, DoubleType, TimestampType

# Initialize Spark session
spark = SparkSession.builder.appName("DatabricksTest").getOrCreate()

# Define expected schema for f_order table
expected_schema = StructType([
    StructField("order_nbr", StringType(), True),
    StructField("order_type", DecimalType(38, 0), True),
    StructField("delivery_dt", DecimalType(38, 0), True),
    StructField("order_qty", DoubleType(), True),
    StructField("sched_dt", DecimalType(38, 0), True),
    StructField("expected_shipped_dt", DecimalType(38, 0), True),
    StructField("actual_shipped_dt", DecimalType(38, 0), True),
    StructField("order_line_nbr", StringType(), True),
    StructField("loc_tracker_id", StringType(), True),
    StructField("shipping_add", StringType(), True),
    StructField("primary_qty", DoubleType(), True),
    StructField("open_qty", DoubleType(), True),
    StructField("shipped_qty", DoubleType(), True),
    StructField("order_desc", StringType(), True),
    StructField("flag_return", StringType(), True),
    StructField("flag_cancel", StringType(), True),
    StructField("cancel_dt", DecimalType(38, 0), True),
    StructField("cancel_qty", DoubleType(), True),
    StructField("crt_dt", TimestampType(), True),
    StructField("updt_dt", TimestampType(), True)
])

# Load f_order table
f_order_df = spark.table("purgo_playground.f_order")

# Validate schema
assert f_order_df.schema == expected_schema, "Schema does not match expected schema"

# PySpark Test for Data Type Conversion
from pyspark.sql.functions import col, date_format

# Convert delivery_dt from timestamp to decimal yyyymmdd
converted_df = f_order_df.withColumn("converted_delivery_dt", date_format(col("crt_dt"), "yyyyMMdd").cast(DecimalType(38, 0)))

# Validate conversion
converted_df.show()

# Assert conversion correctness
assert converted_df.filter(col("converted_delivery_dt") != col("delivery_dt")).count() == 0, "Conversion from timestamp to decimal yyyymmdd failed"

# Cleanup operations
# PySpark Cleanup
f_order_df.unpersist()
