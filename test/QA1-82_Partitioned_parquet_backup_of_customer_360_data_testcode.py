from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Customer360BackupTest") \
    .getOrCreate()

# Define schema for the customer_360_raw table
schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("state", StringType(), True),
    StructField("last_updated", TimestampType(), True)
])

# Sample data for testing
test_data = [
    ("1", "Alice", "CA", "2024-03-21T00:00:00"),
    ("2", "Bob", "NY", "2024-03-19T12:45:00"),
    ("3", "Charlie", "TX", "2023-12-31T23:59:59"),
    ("4", "Dave", "FL", "2024-01-01T00:00:00"),
    ("5", None, "WA", None),
    ("6", "Eve", None, "2024-01-01T00:00:00"),
    (None, "José", "ÑY", "2024-03-21T00:00:00")
]

# Create DataFrame using the defined schema and test data
df = spark.createDataFrame(test_data, schema)

# Display the test DataFrame
df.show(truncate=False)

# Store the DataFrame as compressed Parquet, partitioned by 'state'
df.write.mode("overwrite") \
    .partitionBy("state") \
    .parquet("/Volumes/agilisium_playground/purgo_playground/customer_360_raw_backup", compression="snappy")

# Cleanup operations for old records and perform VACUUM on the customer_360_raw table
# Assuming 'last_updated' column is to determine older records

# SQL command to delete records older than 30 days from the customer_360_raw table
spark.sql("""
    DELETE FROM agilisium_playground.purgo_playground.customer_360_raw
    WHERE last_updated < current_timestamp() - INTERVAL 30 DAYS
""")

# Perform VACUUM operation to clean up files
spark.sql("VACUUM agilisium_playground.purgo_playground.customer_360_raw RETAIN 720 HOURS")

# Stop Spark session
spark.stop()

