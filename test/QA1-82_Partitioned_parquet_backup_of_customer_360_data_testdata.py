from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, expr
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, LongType, DoubleType, DecimalType

# Create Spark session
spark = SparkSession.builder.appName("TestDataGeneration").getOrCreate()

# Define schema for test data matching the structure of the customer_360_raw table
schema = StructType([
    StructField("id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("state", StringType(), True),
    StructField("last_updated", TimestampType(), True)
])

# Generate test data
data = [
    # Happy path data
    (1, "Alice", "CA", "2024-03-21T00:00:00.000+0000"),
    (2, "Bob", "NY", "2024-03-20T10:10:10.000+0000"),

    # Edge cases
    (3, "Charlie", "TX", "2023-12-31T23:59:59.999+0000"),
    (4, "Dave", "FL", "2024-01-01T00:00:00.000+0000"),

    # Error cases
    (5, None, "INVALID_STATE", "2024-01-01T00:00:00.000+0000"),
    (6, "Eve", "WA", None),

    # NULL handling
    (7, None, None, "2024-01-01T00:00:00.000+0000"),

    # Special and multi-byte characters
    (8, "José", "ÑY", "2024-03-21T00:00:00.000+0000"),
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show(truncate=False)

# Store as compressed parquet file, partitioned by state
df.write.mode("overwrite") \
    .partitionBy("state") \
    .parquet("/Volumes/agilisium_playground/purgo_playground/customer_360_raw_backup", compression="snappy")

# Vacuum operation to remove records older than 30 days
customer_360_raw_table = "agilisium_playground.purgo_playground.customer_360_raw" 

# Assuming a column 'last_updated' is used for filtering
spark.sql(f"""
    DELETE FROM {customer_360_raw_table}
    WHERE last_updated < current_timestamp() - INTERVAL 30 DAYS
""")

# Perform vacuum
spark.sql(f"VACUUM {customer_360_raw_table} RETAIN 720 HOURS")

# Stop Spark session
spark.stop()