from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit, round

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Data Quality Checks") \
    .getOrCreate()

# Load the drug_inventory_management table
drug_inventory_df = spark.table("agilisium_playground.purgo_playground.drug_inventory_management")

# Define data quality rules based on DQ_rules_IM sheet
dq_rules = [
    {"check_name": "Check for Null Values", "column": "drug_id", "condition": "IS NOT NULL"},
    {"check_name": "Check for Valid Quantity", "column": "quantity", "condition": "> 0"},
    {"check_name": "Check for Valid Expiry Date", "column": "expiry_date", "condition": ">= current_date()"},
    # Add more rules as per DQ_rules_IM sheet
]

# Function to apply data quality checks
def apply_dq_checks(df, rules):
    results = []
    total_rows = df.count()
    
    for rule in rules:
        check_name = rule["check_name"]
        column = rule["column"]
        condition = rule["condition"]
        
        # Apply the condition and calculate pass percentage
        passed_rows = df.filter(f"{column} {condition}").count()
        pass_percentage = (passed_rows / total_rows) * 100
        
        # Determine result
        result = "Pass" if pass_percentage == 100 else "Fail"
        
        # Append result to the list
        results.append((check_name, result, round(pass_percentage, 2)))
    
    # Create a DataFrame from the results
    dq_results_df = spark.createDataFrame(results, ["check_name", "result", "pass_%"])
    return dq_results_df

# Apply data quality checks
dq_results_df = apply_dq_checks(drug_inventory_df, dq_rules)

# Show the results
dq_results_df.show()

# Stop the Spark session
spark.stop()


This code initializes a Spark session, loads the `drug_inventory_management` table, and applies data quality checks based on predefined rules. The results are compiled into a DataFrame showing the check name, result, and pass percentage.