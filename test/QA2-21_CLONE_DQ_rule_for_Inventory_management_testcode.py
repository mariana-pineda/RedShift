import unittest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DoubleType
from pyspark.sql import functions as F

class DataQualityChecksTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Spark session
        cls.spark = SparkSession.builder \
            .appName("Data Quality Checks Test") \
            .getOrCreate()

        # Define schema for test data
        schema = StructType([
            StructField("product_ID", StringType(), True),
            StructField("product_name", StringType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("location", StringType(), True),
            StructField("expiry_date", DateType(), True),
            StructField("purchase_date", DateType(), True),
            StructField("batch_number", StringType(), True),
            StructField("supplier_ID", StringType(), True)
        ])

        # Create test data
        cls.test_data = [
            ("P001", "Product A", 10, "Location 1", "2023-12-31", "2023-01-01", "B001", "S001"),
            ("P002", "Product B", 0, "Location 2", "2023-01-01", "2023-01-01", "B002", "S002"),
            ("P003", None, 5, "Location 3", "2023-01-01", "2023-01-01", "B003", "S003"),
            ("P004", "Product D", 15, "Location 4", "2022-12-31", "2023-01-01", "B004", "S004"),
            ("P005", "Product E", 20, "Location 5", "2023-12-31", "2023-01-01", "B005", "S005"),
            ("P001", "Product A", 10, "Location 1", "2023-12-31", "2023-01-01", "B001", "S001")  # Duplicate
        ]

        # Create DataFrame from test data
        cls.df = cls.spark.createDataFrame(cls.test_data, schema)

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_mandatory_fields_check(self):
        # Test for non-null mandatory fields
        result_df = self.df.filter(
            F.col("product_ID").isNull() |
            F.col("product_name").isNull() |
            F.col("quantity").isNull() |
            F.col("location").isNull() |
            F.col("expiry_date").isNull() |
            F.col("batch_number").isNull() |
            F.col("supplier_ID").isNull()
        )
        self.assertEqual(result_df.count(), 1, "Mandatory fields check failed")

    def test_expiry_date_check(self):
        # Test for expiry_date > purchase_date
        result_df = self.df.filter(F.col("expiry_date") <= F.col("purchase_date"))
        self.assertEqual(result_df.count(), 1, "Expiry date check failed")

    def test_unique_check(self):
        # Test for uniqueness of Product ID and Batch number
        result_df = self.df.groupBy("product_ID", "batch_number").count().filter("count > 1")
        self.assertEqual(result_df.count(), 1, "Unique check failed")

    def test_data_consistency_check(self):
        # Test for positive quantity and correct date format
        result_df = self.df.filter(
            (F.col("quantity") <= 0) |
            (~F.col("expiry_date").cast(StringType()).rlike('^[0-9]{4}-[0-9]{2}-[0-9]{2}$'))
        )
        self.assertEqual(result_df.count(), 1, "Data consistency check failed")

if __name__ == '__main__':
    unittest.main()
