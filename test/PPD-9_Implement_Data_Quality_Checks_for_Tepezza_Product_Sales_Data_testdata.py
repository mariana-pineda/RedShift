from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType
import random

spark = SparkSession.builder.appName("TepezzaSalesData").getOrCreate()

schema = StructType([
    StructField("Demand", IntegerType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("Unit_Price", FloatType(), True),
    StructField("Product_Status", StringType(), True),
    StructField("Shipment_Type", StringType(), True)
])

# Random data generation for testing

# Demand and Quantity should be in realistic ranges, e.g., Demand between 1-1000 and Quantity between 1-500
# Validate realistic ranges
def generate_demand_quantity():
    demand = random.randint(1, 1000)
    quantity = random.randint(1, 500)
    return demand, quantity

# Unit_Price should be a plausible float value, e.g., between 10.0 - 500.0
# Validate Price Calculation Accuracy
def generate_unit_price():
    return round(random.uniform(10.0, 500.0), 2)

# Product_Status can be 'Sold' or 'Returned'
# Verify Reverse Logistics Steps for Returned Products
def generate_product_status():
    return random.choice(['Sold', 'Returned'])

# Shipment_Type could be 'Small', 'Medium', or 'Large'
# Validate Correct Unit Shipment Type
def generate_shipment_type():
    return random.choice(['Small', 'Medium', 'Large'])

# Generating test data
data = []
for _ in range(30):
    demand, quantity = generate_demand_quantity()
    unit_price = generate_unit_price()
    product_status = generate_product_status()
    shipment_type = generate_shipment_type()
    data.append((demand, quantity, unit_price, product_status, shipment_type))

# Create DataFrame
df = spark.createDataFrame(data, schema)
df.show(truncate=False)
