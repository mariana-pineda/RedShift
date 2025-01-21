import unittest
import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class TestDatabaseSchema(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup database connection
        cls.databricksToken = os.getenv("PURGO_DATABRICKS_TOKEN")
        cls.databricksHost = os.getenv("PURGO_DATABRICKS_HOST")
        cls.databricksPort = os.getenv("PURGO_DATABRICKS_PORT")
        cls.databricksHttpPath = os.getenv("PURGO_DATABRICKS_HTTP_PATH")
        cls.databricksCatalog = os.getenv("PURGO_DATABRICKS_CATALOG")
        cls.databricksSchema = os.getenv("PURGO_DATABRICKS_SCHEMA")

        cls.databricksConnection = (
            f"databricks://token:{cls.databricksToken}@{cls.databricksHost}:{cls.databricksPort}"
            f"?http_path={cls.databricksHttpPath}&catalog={cls.databricksCatalog}&schema={cls.databricksSchema}"
        )
        cls.databricksEngine = create_engine(url=cls.databricksConnection, echo=True)

    @classmethod
    def tearDownClass(cls):
        # Close database connection
        cls.databricksEngine.dispose()

    def test_schema_creation(self):
        # Test if schema is created
        query = "SHOW SCHEMAS"
        with self.databricksEngine.connect() as connection:
            result = connection.execute(query)
            schemas = [row['databaseName'] for row in result]
            self.assertIn('purgo_playground', schemas, "Schema purgo_playground does not exist")

    def test_table_creation(self):
        # Test if all tables are created
        expected_tables = [
            'programs', 'interactions', 'f_order', 'f_item', 'f_inv_movmnt', 'f_events',
            'enrollments', 'd_product', 'countries', 'f_sales', 'psek', 'pchk', 'parl',
            'pbev', 'l009t', 'vbax', 'para'
        ]
        query = "SHOW TABLES IN purgo_playground"
        with self.databricksEngine.connect() as connection:
            result = connection.execute(query)
            tables = [row['tableName'] for row in result]
            for table in expected_tables:
                self.assertIn(table, tables, f"Table {table} does not exist")

    def test_programs_table_structure(self):
        # Test if programs table has correct structure
        expected_columns = {
            'program_id': 'BIGINT',
            'program_name': 'STRING',
            'country_code': 'STRING',
            'program_start_date': 'TIMESTAMP'
        }
        query = "DESCRIBE purgo_playground.programs"
        with self.databricksEngine.connect() as connection:
            result = connection.execute(query)
            columns = {row['col_name']: row['data_type'] for row in result}
            self.assertDictEqual(expected_columns, columns, "Programs table structure is incorrect")

    def test_error_handling(self):
        # Test error handling for invalid SQL
        invalid_query = "SELECT * FROM non_existent_table"
        with self.assertRaises(SQLAlchemyError):
            with self.databricksEngine.connect() as connection:
                connection.execute(invalid_query)

    def test_data_import(self):
        # Test data import into programs table
        df = pd.read_parquet("programs.parquet")
        df.to_sql("programs", self.databricksEngine, if_exists='replace', index=False)

        query = "SELECT COUNT(*) AS count FROM purgo_playground.programs"
        with self.databricksEngine.connect() as connection:
            result = connection.execute(query)
            count = result.fetchone()['count']
            self.assertEqual(count, len(df), "Row count mismatch after data import")

    def test_data_export(self):
        # Test data export from programs table
        query = "SELECT * FROM purgo_playground.programs"
        with self.databricksEngine.connect() as connection:
            result = connection.execute(query)
            df = pd.DataFrame(result.fetchall())
            df.to_parquet("exported_programs.parquet", index=False)

        exported_df = pd.read_parquet("exported_programs.parquet")
        self.assertFalse(exported_df.empty, "Exported data is empty")

if __name__ == '__main__':
    unittest.main()
