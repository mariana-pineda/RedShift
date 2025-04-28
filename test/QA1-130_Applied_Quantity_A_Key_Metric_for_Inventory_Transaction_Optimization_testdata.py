# Commented out SparkSession initialization and import statement
# from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DecimalType
from pyspark.sql import functions as F

# Sample data as per the requirements, including happy path, edge cases, and error handling
data = [
    # Happy path: Valid cases where apl_qty is calculated correctly
    ("1", 50.0, 100.0, 90.0, 50.0, 40.0, 30.0, 40.0),
    ("2", -10.0, 80.0, 70.0, 40.0, 50.0, 45.0, -10.0),
    ("3", 20.0, 60.0, 100.0, 30.0, 30.0, 25.0, 30.0),
    
    # Edge case: Test boundary conditions
    ("4", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, None),  # Default case with all zeros
    ("5", 100.0, 1000.0, 1000.0, 123.456, 1000.0, 1000.0, 100.0),  # Large values
    
    # Errors: Invalid input scenarios
    ("6", -999.9, 10.0, 0.0, 0.0, 100.0, 100.0, None),  # Bandwidth < 0 without valid condition
    ("7", 9000.0, None, None, 45.0, 50.0, 45.0, None),  # Missing data Scenario
    
    # Special cases: Special characters and multi-byte
    ("8", 50.0, 75.0, 90.0, 50.0, 40.0, 30.0, 40.0),  # Regular rRef
    # NULL handling and special characters
    ("9", None, 100.0, "90☃".decode('utf-8', 'ignore'), 50.0, 40.0, 30.0, None),
    ("10", 20.0, 80.0, 100.0, None, None, None, None),
]

# Schema definition for the DataFrame, aligned with the target table schema
schema = StructType([
    StructField("txn_id", StringType(), True),
    StructField("ref_txn_qty", DecimalType(3, 1), True),
    StructField("cumulative_txn_qty", DecimalType(4, 1), True),
    StructField("cumulative_ref_ord_sched_qty", DecimalType(4, 1), True),
    StructField("ref_ord_sched_qty", DecimalType(3, 1), True),
    StructField("prior_cumulative_txn_qty", DecimalType(3, 1), True),
    StructField("prior_cumulative_ref_ord_sched_qty", DecimalType(3, 1), True),
    StructField("apl_qty", DecimalType(5, 1), True)
])

# Create DataFrame with the sample data
# Commented out SparkSession initialization since it's already available
# spark = SparkSession.builder.appName("Test Data Generation").getOrCreate()
df = spark.createDataFrame(data, schema)

# Show generated test data
df.show()

# Commented out spark.stop() since it can cause issues in Databricks
# spark.stop()

