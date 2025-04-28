# Commented out SparkSession initialization as it's already available in Databricks
# from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit
from pyspark.sql.types import StructType, StructField, StringType, DecimalType

# Commented out SparkSession, since spark is already initialized in Databricks
# spark = SparkSession.builder.appName("TestDataGeneration").getOrCreate()

# Defining the schema for the target table f_inv_movmnt_apl_qty
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

# Sample test data generation covering different scenarios
data = [
    # Happy path scenarios
    ("1", 50.0, 100.0, 90.0, 50.0, 40.0, 30.0, 30.0),  # Condition 1: Valid
    ("2", 20.0, 60.0, 100.0, 30.0, 30.0, 25.0, 20.0),  # Condition 2: Valid
    ("3", -10.0, 80.0, 70.0, 40.0, 50.0, 45.0, -10.0),  # Condition 3: Valid
    # Edge cases with zero and boundary values
    ("4", 0.0, 50.0, 50.0, 25.0, 45.0, 45.0, None),   # Default: No condition met
    ("5", 1.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.5),        # Boundary Condition 1
    ("6", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, None),       # All zeros
    # Error cases
    ("7", 1000.0, -800.0, 70.0, 40.0, 50.0, 45.0, None),  # Invalid: Negative cumulative txn qty
    ("8", -20.0, -60.0, -100.0, 30.0, 30.0, 25.0, None), # Invalid: All negative values
    # Special characters and multibyte characters
    ("9", 10.0, 20.0, 50.0, 10.0, 5.0, 5.0, 10.0),  # Regular condition
    ("10", 10.0, 20.0, 50.0, 10.0, 5.0, 5.0, 10.0), # Similar test, different txn_id
    ("11", 15.0, 20.0, 15.0, 12.0, 7.0, 7.0, 15.0), # Multibyte character representation
]

# Creating a DataFrame with the sample data
test_df = spark.createDataFrame(data, schema)

# Display the generated test data
test_df.show(truncate=False)