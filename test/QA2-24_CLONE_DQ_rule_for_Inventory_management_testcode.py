import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

class DataQualityChecksTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Spark session
        cls.spark = SparkSession.builder.appName("DataQualityChecksTest").getOrCreate()
        # Load the drug_inventory_management table into a DataFrame
        cls.drug_inventory_df = cls.spark.table("agilisium_playground.purgo_playground.drug_inventory_management")
        # Total number of records
        cls.total_records = cls.drug_inventory_df.count()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_mandatory_fields_check(self):
        # Check for non-null values in mandatory fields
        mandatory_fields = ["product_ID", "product_name", "quantity", "location", "expiry_date", "batch_number", "supplier_ID"]
        mandatory_check = self.drug_inventory_df.select(
            [when(col(field).isNull(), 1).otherwise(0).alias(field) for field in mandatory_fields]
        ).agg(
            *[count(when(col(field) == 1, field)).alias(field) for field in mandatory_fields]
        )

        mandatory_failures = mandatory_check.collect()[0]
        mandatory_pass_percentage = (1 - sum(mandatory_failures) / (self.total_records * len(mandatory_fields))) * 100

        # Assert that the pass percentage is 100%
        self.assertEqual(mandatory_pass_percentage, 100, "Mandatory Fields Check failed")

    def test_expiry_date_check(self):
        # Check if expiry_date is greater than purchase_date
        expiry_date_check = self.drug_inventory_df.filter(col("expiry_date") <= col("purchase_date")).count()
        expiry_date_pass_percentage = ((self.total_records - expiry_date_check) / self.total_records) * 100

        # Assert that the pass percentage is 100%
        self.assertEqual(expiry_date_pass_percentage, 100, "Expiry Date Check failed")

    def test_unique_check(self):
        # Check for uniqueness of Product ID and Batch number
        unique_check = self.drug_inventory_df.groupBy("product_ID", "batch_number").count().filter("count > 1").count()
        unique_pass_percentage = ((self.total_records - unique_check) / self.total_records) * 100

        # Assert that the pass percentage is 100%
        self.assertEqual(unique_pass_percentage, 100, "Unique Check failed")

    def test_data_consistency_check(self):
        # Check for positive quantity and correct date format
        quantity_check = self.drug_inventory_df.filter(col("quantity") <= 0).count()
        date_format_check = self.drug_inventory_df.filter(~col("expiry_date").rlike(r"^\d{4}-\d{2}-\d{2}$")).count() + \
                            self.drug_inventory_df.filter(~col("purchase_date").rlike(r"^\d{4}-\d{2}-\d{2}$")).count()

        consistency_failures = quantity_check + date_format_check
        consistency_pass_percentage = ((self.total_records - consistency_failures) / self.total_records) * 100

        # Assert that the pass percentage is 100%
        self.assertEqual(consistency_pass_percentage, 100, "Data Consistency Check failed")

if __name__ == '__main__':
    unittest.main()
