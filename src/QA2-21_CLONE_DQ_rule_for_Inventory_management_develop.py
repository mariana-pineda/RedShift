from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Initialize Spark session
spark = SparkSession.builder.appName("DataQualityChecks").getOrCreate()

# Load the drug_inventory_management table into a DataFrame
drug_inventory_df = spark.read.format("csv").option("header", "true").load("path_to_drug_inventory_management.csv")

# Define the schema for the data quality result DataFrame
dq_result_schema = StructType([
    StructField("check_name", StringType(), False),
    StructField("result", StringType(), False),
    StructField("pass_%", DoubleType(), False)
])

# Initialize an empty DataFrame for data quality results
dq_results_df = spark.createDataFrame([], dq_result_schema)

# Total number of records
total_records = drug_inventory_df.count()

# Data Quality Checks
# Mandatory Fields Check
mandatory_fields_check = drug_inventory_df.filter(
    col("product_ID").isNull() |
    col("product_name").isNull() |
    col("quantity").isNull() |
    col("location").isNull() |
    col("expiry_date").isNull() |
    col("batch_number").isNull() |
    col("supplier_ID").isNull()
).count()

mandatory_fields_pass_percentage = ((total_records - mandatory_fields_check) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame(
        [("Mandatory Fields Check", "Pass" if mandatory_fields_check == 0 else "Fail", mandatory_fields_pass_percentage)],
        dq_result_schema
    )
)

# Expiry Date Check
expiry_date_check = drug_inventory_df.filter(
    col("expiry_date") <= col("purchase_date")
).count()

expiry_date_pass_percentage = ((total_records - expiry_date_check) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame(
        [("Expiry Date Check", "Pass" if expiry_date_check == 0 else "Fail", expiry_date_pass_percentage)],
        dq_result_schema
    )
)

# Unique Check
unique_check = drug_inventory_df.groupBy("product_ID", "batch_number").count().filter("count > 1").count()

unique_pass_percentage = ((total_records - unique_check) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame(
        [("Unique Check", "Pass" if unique_check == 0 else "Fail", unique_pass_percentage)],
        dq_result_schema
    )
)

# Data Consistency Check
data_consistency_check = drug_inventory_df.filter(
    (col("quantity") <= 0) |
    (~col("expiry_date").rlike("^\d{4}-\d{2}-\d{2}$"))
).count()

data_consistency_pass_percentage = ((total_records - data_consistency_check) / total_records) * 100

dq_results_df = dq_results_df.union(
    spark.createDataFrame(
        [("Data Consistency Check", "Pass" if data_consistency_check == 0 else "Fail", data_consistency_pass_percentage)],
        dq_result_schema
    )
)

# Show the data quality results
dq_results_df.show()

