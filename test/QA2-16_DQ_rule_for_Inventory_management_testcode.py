import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.types import StringType, DoubleType, StructType, StructField

class DataQualityChecksTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize Spark session
        cls.spark = SparkSession.builder.appName("DataQualityChecksTest").getOrCreate()
        # Load the drug_inventory_management table
        cls.drug_inventory_df = cls.spark.table("agilisium_playground.purgo_playground.drug_inventory_management")

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def calculate_pass_percentage(self, df, condition):
        total_rows = df.count()
        passed_rows = df.filter(expr(condition)).count()
        pass_percentage = (passed_rows / total_rows) * 100 if total_rows > 0 else 0
        return pass_percentage

    def test_mandatory_fields_check(self):
        # Test to ensure all mandatory fields are not null
        condition = "product_ID IS NOT NULL AND product_name IS NOT NULL AND quantity IS NOT NULL AND location IS NOT NULL AND expiry_date IS NOT NULL AND batch_number IS NOT NULL AND supplier_ID IS NOT NULL"
        pass_percentage = self.calculate_pass_percentage(self.drug_inventory_df, condition)
        self.assertEqual(pass_percentage, 100, "Mandatory Fields Check failed")

    def test_expiry_date_check(self):
        # Test to ensure expiry_date is greater than purchase_date
        condition = "expiry_date > purchase_date"
        pass_percentage = self.calculate_pass_percentage(self.drug_inventory_df, condition)
        self.assertEqual(pass_percentage, 100, "Expiry Date Check failed")

    def test_unique_check(self):
        # Test to ensure Product ID and Batch number are unique
        condition = "product_ID IS NOT NULL AND batch_number IS NOT NULL"
        unique_df = self.drug_inventory_df.dropDuplicates(["product_ID", "batch_number"])
        pass_percentage = self.calculate_pass_percentage(unique_df, condition)
        self.assertEqual(pass_percentage, 100, "Unique Check failed")

    def test_data_consistency_check(self):
        # Test to ensure quantity is positive and date formats are correct
        condition = "quantity > 0 AND expiry_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' AND purchase_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'"
        pass_percentage = self.calculate_pass_percentage(self.drug_inventory_df, condition)
        self.assertEqual(pass_percentage, 100, "Data Consistency Check failed")

    def test_error_handling_for_null_fields(self):
        # Test error handling for null fields
        condition = "product_ID IS NULL OR product_name IS NULL OR quantity IS NULL OR location IS NULL OR expiry_date IS NULL OR batch_number IS NULL OR supplier_ID IS NULL"
        error_rows = self.drug_inventory_df.filter(expr(condition)).count()
        self.assertEqual(error_rows, 0, "Error handling for null fields failed")

    def test_error_handling_for_invalid_dates(self):
        # Test error handling for invalid date formats
        condition = "NOT (expiry_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' AND purchase_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$')"
        error_rows = self.drug_inventory_df.filter(expr(condition)).count()
        self.assertEqual(error_rows, 0, "Error handling for invalid dates failed")

if __name__ == '__main__':
    unittest.main()
