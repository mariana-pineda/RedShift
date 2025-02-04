from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit, round

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Data Quality Checks") \
    .getOrCreate()

# Load the drug_inventory_management table
drug_inventory_df = spark.table("agilisium_playground.purgo_playground.drug_inventory_management")

# Define data quality rules based on DQ_rules_IM sheet
# Example rules (these should be replaced with actual rules from the DQ_rules_IM sheet)
rules = [
    {"check_name": "Check for Null Values in Drug Name", "condition": col("drug_name").isNotNull()},
    {"check_name": "Check for Positive Inventory Count", "condition": col("inventory_count") > 0},
    {"check_name": "Check for Valid Expiry Date", "condition": col("expiry_date") > lit("2023-01-01")},
    # Add more rules as per the DQ_rules_IM sheet
]

# Initialize a list to store the results
results = []

# Apply each rule and calculate the pass percentage
for rule in rules:
    total_count = drug_inventory_df.count()
    pass_count = drug_inventory_df.filter(rule["condition"]).count()
    pass_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0

    # Append the result to the list
    results.append({
        "check_name": rule["check_name"],
        "result": "Pass" if pass_percentage == 100 else "Fail",
        "pass_%": round(pass_percentage, 2)
    })

# Create a DataFrame from the results
dq_results_df = spark.createDataFrame(results)

# Show the data quality results
dq_results_df.show(truncate=False)

# Stop the Spark session
spark.stop()


This code snippet initializes a Spark session, loads the `drug_inventory_management` table, and applies a set of data quality rules. Each rule checks a specific condition, and the code calculates the pass percentage for each rule. The results are stored in a DataFrame and displayed. The rules in the code are placeholders and should be replaced with actual rules from the `DQ_rules_IM` sheet.