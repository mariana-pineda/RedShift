from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DoubleType, DateType
from pyspark.sql.functions import lit, current_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Test Data Generation") \
    .getOrCreate()

# Schema for employees table
employees_schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("lastdate", DateType(), True)
])

# Generate test data for employees
employees_data = [
    # Happy path
    (1, "Alice", 29, None),
    (2, "Bob", 35, None),
    (3, "Charlie", 45, None),
    # Edge cases
    (4, "", 0, None),  # Empty name, age boundary
    (5, "Eve", 120, None),  # Edge case age
    # Error cases
    (6, "Dave", 30, "2023-02-30"),  # Invalid date
    (7, "Megan", 40, "2099-12-31"),  # Future date
    # NULL handling
    (8, "NULL_NAME", None, None),
    # Special characters and multi-byte characters
    (9, "Renée", 33, None),
    (10, "こんにちは", 28, None)  # Japanese for Hello
]

# Creating DataFrame for employees
employees_df = spark.createDataFrame(employees_data, schema=employees_schema)

# Set default lastdate to current date
employees_df = employees_df.withColumn("lastdate", lit(current_date()))

# Schema for customers table
customers_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("customer_name", StringType(), True),
    StructField("categoryGroup", StringType(), True)
])

# Generate test data for customers
customers_data = [
    # Happy path
    (1, "John Doe", "VIP"),
    (2, "Jane Smith", "Regular"),
    (3, "Jim Bean", "New"),
    # Edge cases
    (4, "Anna", ""),  # Empty category
    (5, "Elon", "VIPč"),  # Special character in category
    # Error cases
    (6, "Sarah", "Super VIP"),  # Invalid category
    (7, "Tom", "Gold"),  # Invalid category
    # NULL handling
    (8, "NULL_CUSTOMER", None),
    # Special characters and multi-byte characters
    (9, "Mulțumesc", "Regular"),  # Romanian for Thank You
    (10, "谢谢", "New")  # Chinese for Thank You
]

# Creating DataFrame for customers
customers_df = spark.createDataFrame(customers_data, schema=customers_schema)

# Set default categoryGroup to "Uncategorized"
customers_df = customers_df.withColumn("categoryGroup", 
                                       lit("Uncategorized")
                                       .when(customers_df.categoryGroup == '', lit("Uncategorized"))
                                       .otherwise(customers_df.categoryGroup))

# Show generated data
employees_df.show()
customers_df.show()