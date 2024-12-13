from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col, isnan, when, count, to_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Tepezza Sales Data Quality Checks") \
    .getOrCreate()

# Define schema based on expected data quality rules
schema = StructType([
    StructField("sales_id", StringType(), True),
    StructField("product_name", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", FloatType(), True),
    StructField("sale_date", StringType(), True)
])

# Sample data
data = [
    ("1", "Tepezza", 10, 1500.0, "2023-01-01"),
    ("2", "Tepezza", 5, 750.0, "2023-01-02"),
    ("3", "Tepezza", None, 1500.0, "2023-01-03"),
    ("4", "Tepezza", 8, None, "2023-01-04"),
    ("5", "Tepezza", 12, 1800.0, None),
    ("6", "Tepezza", "ten", 1500.0, "2023-01-06"),
    ("7", "Tepezza", 7, "one thousand", "2023-01-07"),
    ("8", "Tepezza", 9, 1350.0, "01-08-2023"),
    ("9", "Tepezza", 15, 2250.0, "2023-01-09"),
    ("10", "Tepezza", 20, 3000.0, "2023-01-10"),
    ("11", "Tepezza", 0, 0.0, "2023-01-11"),
    ("12", "Tepezza", -5, 750.0, "2023-01-12"),
    ("13", "Tepezza", 10, -1500.0, "2023-01-13"),
    ("14", "Tepezza", 10, 1500.0, "2023-01-14"),
    ("15", "Tepezza", 5, 750.0, "2023-01-15"),
    ("16", "Tepezza", 8, 1200.0, "2023-01-16"),
    ("17", "Tepezza", 12, 1800.0, "2023-01-17"),
    ("18", "Tepezza", 7, 1050.0, "2023-01-18"),
    ("19", "Tepezza", 9, 1350.0, "2023-01-19"),
    ("20", "Tepezza", 15, 2250.0, "2023-01-20"),
    ("21", "Tepezza", 20, 3000.0, "2023-01-21"),
    ("22", "Tepezza", 0, 0.0, "2023-01-22"),
    ("23", "Tepezza", -5, 750.0, "2023-01-23"),
    ("24", "Tepezza", 10, -1500.0, "2023-01-24"),
    ("25", "Tepezza", 10, 1500.0, "2023-01-25"),
    ("26", "Tepezza", 5, 750.0, "2023-01-26"),
    ("27", "Tepezza", 8, 1200.0, "2023-01-27"),
    ("28", "Tepezza", 12, 1800.0, "2023-01-28"),
    ("29", "Tepezza", 7, 1050.0, "2023-01-29"),
    ("30", "Tepezza", 9, 1350.0, "2023-01-30")
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Validate completeness: Check for missing fields
completeness_checks = df.select(
    [count(when(col(c).isNull() | isnan(c), c)).alias(c) for c in df.columns]
)
completeness_checks.show()

# Validate accuracy: Check for correct data types and formats
accuracy_checks = df.withColumn("quantity_check", col("quantity").cast("int").isNotNull()) \
    .withColumn("price_check", col("price").cast("float").isNotNull()) \
    .withColumn("sale_date_check", to_date(col("sale_date"), "yyyy-MM-dd").isNotNull())

accuracy_checks.select("sales_id", "quantity_check", "price_check", "sale_date_check").show()

# Validate consistency: Check for business rule adherence
consistency_checks = df.withColumn("positive_quantity", col("quantity") > 0) \
    .withColumn("positive_price", col("price") > 0)

consistency_checks.select("sales_id", "positive_quantity", "positive_price").show()

# Flag records failing data quality checks
failed_records = df.filter(
    col("quantity").isNull() | col("price").isNull() | col("sale_date").isNull() |
    col("quantity").cast("int").isNull() | col("price").cast("float").isNull() |
    to_date(col("sale_date"), "yyyy-MM-dd").isNull() |
    (col("quantity") <= 0) | (col("price") <= 0)
)
failed_records.show()

# Log and alert for data quality issues
failed_records_count = failed_records.count()
if failed_records_count > 0:
    print(f"Data quality issues detected: {failed_records_count} records failed checks.")
    # Here you would implement logging and alerting mechanisms

# Update data quality rules
# This part would involve reloading or modifying the rules and re-running the checks
# For demonstration, assume rules are updated and checks are re-executed
# Re-run the checks after updating rules
