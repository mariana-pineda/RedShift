# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, LongType

# Initialize Spark session
spark = SparkSession.builder.appName("DataQualityChecks").getOrCreate()

# Define schema for drug_inventory_management table
schema = StructType([
    StructField("product_ID", StringType(), True),
    StructField("product_name", StringType(), True),
    StructField("quantity", LongType(), True),
    StructField("location", StringType(), True),
    StructField("expiry_date", TimestampType(), True),
    StructField("batch_number", StringType(), True),
    StructField("supplier_ID", StringType(), True),
    StructField("purchase_date", TimestampType(), True),
    StructField("last_restocked_date", TimestampType(), True),
    StructField("status", StringType(), True),
    StructField("data_loaded_at", TimestampType(), True)
])

# Load the drug_inventory_management table
drug_inventory_df = spark.read.format("delta").schema(schema).load("dbfs:/path/to/drug_inventory_management")

# Define data quality rules
dq_rules = [
    {"check_name": "Non-null ProductID", "condition": "product_ID IS NOT NULL"},
    {"check_name": "Valid Expiry Date", "condition": "expiry_date > current_timestamp()"},
    {"check_name": "Non-negative Qty", "condition": "quantity >= 0"}
]

# Initialize an empty list to store data quality results
dq_results = []

# Apply data quality rules
for rule in dq_rules:
    check_name = rule["check_name"]
    condition = rule["condition"]
    
    # Calculate pass percentage
    total_count = drug_inventory_df.count()
    pass_count = drug_inventory_df.filter(expr(condition)).count()
    pass_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0
    
    # Determine result
    result = "Pass" if pass_percentage == 100 else "Fail"
    
    # Append result to the list
    dq_results.append((check_name, result, pass_percentage))

# Create a DataFrame for data quality results
dq_results_df = spark.createDataFrame(dq_results, ["check_name", "result", "pass_%"])

# Write the data quality results to the im_data_check table
dq_results_df.withColumn("dq_check_date", current_timestamp()) \
    .write.format("delta").mode("overwrite").saveAsTable("purgo_playground.im_data_check")

# Stop the Spark session
spark.stop()
