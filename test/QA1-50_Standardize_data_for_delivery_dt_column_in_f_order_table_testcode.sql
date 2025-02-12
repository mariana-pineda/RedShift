-- SQL Test Code for Databricks Environment

-- Test for delivery_dt format and type in f_order table
-- Ensure delivery_dt is 100% Decimal (38,0) and in yyyymmdd format

-- Check if delivery_dt is in the correct format
SELECT COUNT(*) AS invalid_count
FROM purgo_playground.f_order
WHERE CAST(delivery_dt AS STRING) NOT RLIKE '^[0-9]{8}$';

-- Check if delivery_dt is a valid date
SELECT COUNT(*) AS invalid_date_count
FROM purgo_playground.f_order
WHERE TRY_CAST(CAST(delivery_dt AS STRING) AS DATE) IS NULL;



# PySpark Test Code for Databricks Environment

# Import necessary libraries
# Ensure required libraries are installed
# MAGIC %pip install pytest

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pytest

# Initialize Spark session
spark = SparkSession.builder.appName("DatabricksTest").getOrCreate()

# Load f_order table
f_order_df = spark.table("purgo_playground.f_order")

# Test delivery_dt format
def test_delivery_dt_format():
    invalid_count = f_order_df.filter(~col("delivery_dt").cast("string").rlike("^[0-9]{8}$")).count()
    assert invalid_count == 0, "All delivery_dt values should be in yyyymmdd format"

# Test delivery_dt as valid date
def test_delivery_dt_valid_date():
    invalid_date_count = f_order_df.filter(col("delivery_dt").cast("string").cast("date").isNull()).count()
    assert invalid_date_count == 0, "All delivery_dt values should be valid dates"

# Run tests
pytest.main(["-v", "-s"])

# Cleanup operations
# Drop temporary views or tables if created during tests
