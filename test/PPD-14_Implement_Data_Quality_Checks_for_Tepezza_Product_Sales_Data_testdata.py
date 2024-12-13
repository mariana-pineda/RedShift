from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import lit

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Tepezza Sales Data Test Generation") \
    .getOrCreate()

# Define schema based on expected data quality rules
schema = StructType([
    StructField("sales_id", StringType(), True),  # Validate completeness: sales_id should be present
    StructField("product_name", StringType(), True),  # Validate completeness: product_name should be present
    StructField("quantity", IntegerType(), True),  # Validate accuracy: quantity should be an integer
    StructField("price", FloatType(), True),  # Validate accuracy: price should be a float
    StructField("sale_date", StringType(), True)  # Validate accuracy: sale_date should be a string in date format
])

# Generate test data
data = [
    ("1", "Tepezza", 10, 1500.0, "2023-01-01"),  # Valid record
    ("2", "Tepezza", 5, 750.0, "2023-01-02"),  # Valid record
    ("3", "Tepezza", None, 1500.0, "2023-01-03"),  # Validate completeness: missing quantity
    ("4", "Tepezza", 8, None, "2023-01-04"),  # Validate completeness: missing price
    ("5", "Tepezza", 12, 1800.0, None),  # Validate completeness: missing sale_date
    ("6", "Tepezza", "ten", 1500.0, "2023-01-06"),  # Validate accuracy: quantity not an integer
    ("7", "Tepezza", 7, "one thousand", "2023-01-07"),  # Validate accuracy: price not a float
    ("8", "Tepezza", 9, 1350.0, "01-08-2023"),  # Validate accuracy: sale_date not in expected format
    ("9", "Tepezza", 15, 2250.0, "2023-01-09"),  # Valid record
    ("10", "Tepezza", 20, 3000.0, "2023-01-10"),  # Valid record
    ("11", "Tepezza", 0, 0.0, "2023-01-11"),  # Validate consistency: quantity and price should be positive
    ("12", "Tepezza", -5, 750.0, "2023-01-12"),  # Validate consistency: negative quantity
    ("13", "Tepezza", 10, -1500.0, "2023-01-13"),  # Validate consistency: negative price
    ("14", "Tepezza", 10, 1500.0, "2023-01-14"),  # Valid record
    ("15", "Tepezza", 5, 750.0, "2023-01-15"),  # Valid record
    ("16", "Tepezza", 8, 1200.0, "2023-01-16"),  # Valid record
    ("17", "Tepezza", 12, 1800.0, "2023-01-17"),  # Valid record
    ("18", "Tepezza", 7, 1050.0, "2023-01-18"),  # Valid record
    ("19", "Tepezza", 9, 1350.0, "2023-01-19"),  # Valid record
    ("20", "Tepezza", 15, 2250.0, "2023-01-20"),  # Valid record
    ("21", "Tepezza", 20, 3000.0, "2023-01-21"),  # Valid record
    ("22", "Tepezza", 0, 0.0, "2023-01-22"),  # Validate consistency: quantity and price should be positive
    ("23", "Tepezza", -5, 750.0, "2023-01-23"),  # Validate consistency: negative quantity
    ("24", "Tepezza", 10, -1500.0, "2023-01-24"),  # Validate consistency: negative price
    ("25", "Tepezza", 10, 1500.0, "2023-01-25"),  # Valid record
    ("26", "Tepezza", 5, 750.0, "2023-01-26"),  # Valid record
    ("27", "Tepezza", 8, 1200.0, "2023-01-27"),  # Valid record
    ("28", "Tepezza", 12, 1800.0, "2023-01-28"),  # Valid record
    ("29", "Tepezza", 7, 1050.0, "2023-01-29"),  # Valid record
    ("30", "Tepezza", 9, 1350.0, "2023-01-30")  # Valid record
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show the generated test data
df.show(truncate=False)
