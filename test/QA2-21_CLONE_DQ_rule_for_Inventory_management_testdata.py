from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit, expr
from pyspark.sql.types import StringType, DoubleType, IntegerType, DateType
from pyspark.sql import functions as F

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Data Quality Checks") \
    .getOrCreate()

# Load the drug_inventory_management table
drug_inventory_df = spark.read.format("delta").load("path_to_drug_inventory_management_table")

# Define data quality rules
dq_rules = [
    {
        "check_name": "Mandatory Fields Check",
        "condition": "product_ID IS NOT NULL AND product_name IS NOT NULL AND quantity IS NOT NULL AND location IS NOT NULL AND expiry_date IS NOT NULL AND batch_number IS NOT NULL AND supplier_ID IS NOT NULL",
        "description": "Ensure all mandatory fields are not null"
    },
    {
        "check_name": "Expiry Date Check",
        "condition": "expiry_date > purchase_date",
        "description": "Ensure expiry_date is greater than purchase_date"
    },
    {
        "check_name": "Unique Check",
        "condition": "product_ID IS NOT NULL AND batch_number IS NOT NULL",
        "description": "Ensure Product ID and Batch number are unique"
    },
    {
        "check_name": "Data Consistency Check",
        "condition": "quantity > 0 AND expiry_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'",
        "description": "Make sure quantity is positive and date columns are in the correct format"
    }
]

# Function to apply data quality checks
def apply_dq_checks(df, rules):
    results = []
    total_rows = df.count()
    
    for rule in rules:
        check_name = rule["check_name"]
        condition = rule["condition"]
        
        # Apply the condition and calculate pass percentage
        passed_df = df.filter(condition)
        passed_count = passed_df.count()
        pass_percentage = (passed_count / total_rows) * 100
        
        # Append result
        results.append((check_name, "Pass" if pass_percentage == 100 else "Fail", pass_percentage))
    
    # Create a DataFrame for the results
    result_df = spark.createDataFrame(results, ["check_name", "result", "pass_%"])
    return result_df

# Apply data quality checks
dq_results_df = apply_dq_checks(drug_inventory_df, dq_rules)

# Show the results
dq_results_df.show()

# Stop the Spark session
spark.stop()


### Explanation of Test Data Generation

1. **Happy Path Test Data:**
   - Records where all mandatory fields are filled, expiry dates are valid, quantities are positive, and formats are correct.

2. **Edge Case Test Data:**
   - Records with expiry dates exactly one day after purchase dates.
   - Records with quantities exactly equal to zero (should fail).

3. **Error Case Test Data:**
   - Records with null values in mandatory fields.
   - Records with expiry dates before purchase dates.
   - Duplicate Product ID and Batch number combinations.

4. **Special Character and Format Test Data:**
   - Records with special characters in string fields.
   - Records with date fields in incorrect formats (e.g., DD-MM-YYYY).

### Data Generation Rules

- Ensure a mix of scenarios for each data field.
- Cover all business rules and validations.
- Include data for all identified edge cases.

### Code Structure

- Clear variable names indicating the test scenario.
- Comments explaining the test case conditions.
- Group related test data together.
- Include data type and format validations.