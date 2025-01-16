import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

class DataQualityChecksTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Spark session
        cls.spark = SparkSession.builder.appName("DataQualityChecksTest").getOrCreate()
        # Load the drug_inventory_management table into a DataFrame
        cls.drug_inventory_df = cls.spark.read.format("csv").option("header", "true").load("path_to_drug_inventory_management.csv")
        # Define the schema for the data quality result DataFrame
        cls.dq_result_schema = StructType([
            StructField("check_name", StringType(), False),
            StructField("result", StringType(), False),
            StructField("pass_%", DoubleType(), False)
        ])
        # Total number of records
        cls.total_records = cls.drug_inventory_df.count()

    def test_mandatory_fields_check(self):
        # Test case: All mandatory fields are present
        mandatory_fields_check = self.drug_inventory_df.filter(
            col("product_ID").isNull() |
            col("product_name").isNull() |
            col("quantity").isNull() |
            col("location").isNull() |
            col("expiry_date").isNull() |
            col("batch_number").isNull() |
            col("supplier_ID").isNull()
        ).count()

        mandatory_fields_pass_percentage = ((self.total_records - mandatory_fields_check) / self.total_records) * 100
        result = "Pass" if mandatory_fields_check == 0 else "Fail"
        self.assertEqual(result, "Pass", "Mandatory Fields Check failed")
        self.assertGreaterEqual(mandatory_fields_pass_percentage, 100.0, "Mandatory Fields Check pass percentage is not 100%")

    def test_expiry_date_check(self):
        # Test case: Expiry date is greater than purchase date
        expiry_date_check = self.drug_inventory_df.filter(
            col("expiry_date") <= col("purchase_date")
        ).count()

        expiry_date_pass_percentage = ((self.total_records - expiry_date_check) / self.total_records) * 100
        result = "Pass" if expiry_date_check == 0 else "Fail"
        self.assertEqual(result, "Pass", "Expiry Date Check failed")
        self.assertGreaterEqual(expiry_date_pass_percentage, 100.0, "Expiry Date Check pass percentage is not 100%")

    def test_unique_check(self):
        # Test case: Ensure Product ID and Batch number are unique
        unique_check = self.drug_inventory_df.groupBy("product_ID", "batch_number").count().filter("count > 1").count()

        unique_pass_percentage = ((self.total_records - unique_check) / self.total_records) * 100
        result = "Pass" if unique_check == 0 else "Fail"
        self.assertEqual(result, "Pass", "Unique Check failed")
        self.assertGreaterEqual(unique_pass_percentage, 100.0, "Unique Check pass percentage is not 100%")

    def test_data_consistency_check(self):
        # Test case: Ensure quantity is positive and date format is correct
        data_consistency_check = self.drug_inventory_df.filter(
            (col("quantity") <= 0) |
            (~col("expiry_date").rlike("^\d{4}-\d{2}-\d{2}$"))
        ).count()

        data_consistency_pass_percentage = ((self.total_records - data_consistency_check) / self.total_records) * 100
        result = "Pass" if data_consistency_check == 0 else "Fail"
        self.assertEqual(result, "Pass", "Data Consistency Check failed")
        self.assertGreaterEqual(data_consistency_pass_percentage, 100.0, "Data Consistency Check pass percentage is not 100%")

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

if __name__ == '__main__':
    unittest.main()
