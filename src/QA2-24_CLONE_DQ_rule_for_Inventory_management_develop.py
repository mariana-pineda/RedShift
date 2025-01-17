from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Initialize Spark session
spark = SparkSession.builder.appName("DataQualityChecks").getOrCreate()

# Load the drug_inventory_management table into a DataFrame
drug_inventory_df = spark.table("agilisium_playground.purgo_playground.drug_inventory_management")

# Define the schema for the data quality result DataFrame
dq_result_schema = StructType([
    StructField("check_name", StringType(), True),
    StructField("result", StringType(), True),
    StructField("pass_%", DoubleType(), True)
])

# Initialize an empty DataFrame for storing data quality results
dq_results_df = spark.createDataFrame([], schema=dq_result_schema)

# Total number of records
total_records = drug_inventory_df.count()

# Mandatory Fields Check
mandatory_fields = ["product_ID", "product_name", "quantity", "location", "expiry_date", "batch_number", "supplier_ID"]
mandatory_check = drug_inventory_df.select(
    [when(col(field).isNull(), 1).otherwise(0).alias(field) for field in mandatory_fields]
).agg(
    *[count(when(col(field) == 1, field)).alias(field) for field in mandatory_fields]
)

mandatory_failures = mandatory_check.collect()[0]
mandatory_pass_percentage = (1 - sum(mandatory_failures) / (total_records * len(mandatory_fields))) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame([("Mandatory Fields Check", "Pass" if mandatory_pass_percentage == 100 else "Fail", mandatory_pass_percentage)], schema=dq_result_schema)
)

# Expiry Date Check
expiry_date_check = drug_inventory_df.filter(col("expiry_date") <= col("purchase_date")).count()
expiry_date_pass_percentage = ((total_records - expiry_date_check) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame([("Expiry Date Check", "Pass" if expiry_date_pass_percentage == 100 else "Fail", expiry_date_pass_percentage)], schema=dq_result_schema)
)

# Unique Check
unique_check = drug_inventory_df.groupBy("product_ID", "batch_number").count().filter("count > 1").count()
unique_pass_percentage = ((total_records - unique_check) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame([("Unique Check", "Pass" if unique_pass_percentage == 100 else "Fail", unique_pass_percentage)], schema=dq_result_schema)
)

# Data Consistency Check
quantity_check = drug_inventory_df.filter(col("quantity") <= 0).count()
date_format_check = drug_inventory_df.filter(~col("expiry_date").rlike(r"^\d{4}-\d{2}-\d{2}$")).count() + \
                    drug_inventory_df.filter(~col("purchase_date").rlike(r"^\d{4}-\d{2}-\d{2}$")).count()

consistency_failures = quantity_check + date_format_check
consistency_pass_percentage = ((total_records - consistency_failures) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame([("Data Consistency Check", "Pass" if consistency_pass_percentage == 100 else "Fail", consistency_pass_percentage)], schema=dq_result_schema)
)

# Show the data quality results
dq_results_df.show()
