/* 
Test Script for validating delivery_dt in purgo_playground.f_order

This script performs schema validation, data type checks, 
format validation, and NULL handling for the delivery_dt column 
in the f_order table. The results of the tests are inserted into 
the dq_reports table.
*/

/* 
Schema Validation Test
Ensure the f_order table has the expected number of columns
*/
WITH schema_validation AS (
    SELECT COUNT(*) AS column_count
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_catalog = 'purgo_databricks' 
      AND table_schema = 'purgo_playground' 
      AND table_name = 'f_order'
),
expected_schema AS (
    SELECT 20 AS expected_column_count -- Adjust based on actual number of columns
)

/* 
Data Type Validation Test for delivery_dt
Ensure delivery_dt is of type Decimal(38,0)
*/
,data_type_validation AS (
    SELECT 
        data_type, 
        numeric_precision, 
        numeric_scale
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_catalog = 'purgo_databricks' 
      AND table_schema = 'purgo_playground' 
      AND table_name = 'f_order'
      AND column_name = 'delivery_dt'
)

/* 
Format Validation Test: Check if delivery_dt is in yyyymmdd format
*/
,format_validation AS (
    SELECT 
        COUNT(*) AS invalid_format_count
    FROM purgo_databricks.purgo_playground.f_order
    WHERE 
        delivery_dt IS NULL
        OR delivery_dt < 10000101 
        OR delivery_dt > 99991231
        OR ((delivery_dt / 10000) % 100) < 1 
        OR ((delivery_dt / 10000) % 100) > 12
        OR (delivery_dt % 100) < 1 
        OR (delivery_dt % 100) > 31
)

/* 
NULL Handling Test: Check for NULLs in delivery_dt
*/
,null_validation AS (
    SELECT 
        COUNT(*) AS null_count
    FROM purgo_databricks.purgo_playground.f_order
    WHERE delivery_dt IS NULL
)

/* 
Final Test Result Aggregation
Insert the test outcomes into dq_reports table
*/
INSERT INTO purgo_databricks.purgo_playground.dq_reports
SELECT
    NULL AS Order_ID,
    CASE 
        WHEN sv.column_count = ec.expected_column_count THEN 'PASS' 
        ELSE 'FAIL' 
    END AS Mandatory_Fields_Check,
    CASE 
        WHEN dtv.data_type = 'decimal' 
             AND dtv.numeric_precision = 38 
             AND dtv.numeric_scale = 0 THEN 'PASS' 
        ELSE 'FAIL' 
    END AS Date_Consistency_Check,
    CASE 
        WHEN fv.invalid_format_count = 0 THEN 'PASS' 
        ELSE 'FAIL' 
    END AS Range_Check,
    CASE 
        WHEN nv.null_count = 0 THEN 'PASS' 
        ELSE 'FAIL' 
    END AS Status_Consistency_Check,
    NULL AS Unique_Identifier_Check,
    NULL AS Returned_Product_Validation,
    NULL AS Correct_Unit_Shipment_Type,
    NULL AS Price_Calculation_Accuracy
FROM 
    schema_validation sv
    CROSS JOIN expected_schema ec
    CROSS JOIN data_type_validation dtv
    CROSS JOIN format_validation fv
    CROSS JOIN null_validation nv;
