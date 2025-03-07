from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType
from pyspark.sql.functions import lit, current_date, col
from pyspark.sql.streaming import DataStreamWriter
from pyspark.sql import Row
from pyspark.sql.utils import AnalysisException

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Databricks Schema Modification Tests") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .getOrCreate()

# Schema for employees table
employees_schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("lastdate", DateType(), True)  # New column to be tested
])

# Schema for customers table
customers_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("categoryGroup", StringType(), True)
])

# Test case for adding lastdate to employees table
def test_add_lastdate_to_employees():
    # Initial Data
    initial_data = [
        (1, "Alice", 29, None),
        (2, "Bob", 35, None)
    ]
    
    # Create DataFrame
    df = spark.createDataFrame(initial_data, schema=employees_schema)
    
    # Set default lastdate to current date
    df = df.withColumn("lastdate", lit(current_date()))

    # Assertion: Check if lastdate column is added correctly with current date
    assert df.filter(df.lastdate.isNull()).count() == 0, "Default lastdate is not set to current date"
    
    # Invalid Date Insertion Test
    invalid_date_data = Row(employee_id=3, name="Charlie", age=30, lastdate="2023-02-30")
    try:
        df = df.union(spark.createDataFrame([invalid_date_data], employees_schema))
    except AnalysisException as exc:
        assert str(exc).contains("Could not cast"), f"Unexpected error message: {str(exc)}"

    # Future Date Test
    future_date_data = Row(employee_id=4, name="Dave", age=40, lastdate="2099-12-31")
    try:
        df = df.union(spark.createDataFrame([future_date_data], employees_schema))
    except AnalysisException as exc:
        assert str(exc).contains("Could not cast"), f"Unexpected error message: {str(exc)}"

# Test case for adding categoryGroup to customers table
def test_add_categoryGroup_to_customers():
    # Initial Data
    initial_data = [
        (1, "John Doe", "VIP"),
        (2, "Jane Smith", "")
    ]

    # Create DataFrame
    df = spark.createDataFrame(initial_data, schema=customers_schema)
    
    # Set default categoryGroup to "Uncategorized"
    df = df.withColumn("categoryGroup",
                       lit("Uncategorized")
                       .when(col("categoryGroup") == '', lit("Uncategorized"))
                       .otherwise(col("categoryGroup")))

    # Assertion: Check if "Uncategorized" is set for empty categoryGroup
    assert df.filter(df.categoryGroup == "Uncategorized").count() == len(initial_data), "Default categoryGroup is not set to 'Uncategorized'"
    
    # Invalid Category Test
    invalid_category_data = Row(customer_id=3, customer_name="Elon", categoryGroup="Gold")
    try:
        df = df.union(spark.createDataFrame([invalid_category_data], customers_schema))
    except AnalysisException as exc:
        assert str(exc).contains("Invalid category"), f"Unexpected error message: {str(exc)}"

# Run Tests
test_add_lastdate_to_employees()
test_add_categoryGroup_to_customers()

# Cleanup: This might typically involve dropping temporary tables or views
# Drop temporary views or tables if created
# spark.sql("DROP VIEW IF EXISTS temp_employees_view")
# spark.sql("DROP VIEW IF EXISTS temp_customers_view")