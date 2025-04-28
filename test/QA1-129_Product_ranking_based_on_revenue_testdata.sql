-- Code for generating test data using Databricks SQL

-- Use CTE for generating test data using the specified table
WITH TestData AS (
  SELECT
    -- Happy Path Test Data
    1 AS product_id,
    'Product A' AS product_name,
    'Type1' AS product_type,
    10000 AS revenue,
    'USA' AS country,
    'CUST001' AS customer_id,
    CAST('2024-01-21' AS DATE) AS purchased_date,
    CAST('2024-01-21' AS DATE) AS invoice_date,
    1001 AS invoice_number,
    0 AS is_returned,
    100 AS customer_satisfaction_score,
    'Details of Product A' AS product_details,
    CAST('2023-01-21' AS DATE) AS customer_first_purchased_date,
    'First Product A' AS customer_first_product,
    2000.50 AS customer_first_revenue,

    -- Edge Cases: Boundary Conditions
    2 AS product_id,
    'Product B' AS product_name,
    'Type2' AS product_type,
    9999999999 AS revenue, -- Edge case for large revenue
    'CAN' AS country,
    'CUST002' AS customer_id,
    CAST('2024-11-20' AS DATE) AS purchased_date,
    CAST('2024-11-20' AS DATE) AS invoice_date,
    1002 AS invoice_number,
    1 AS is_returned,
    50 AS customer_satisfaction_score,
    'Details of Product B' AS product_details,
    CAST('2023-11-20' AS DATE) AS customer_first_purchased_date,
    'First Product B' AS customer_first_product,
    1000.00 AS customer_first_revenue,

    -- Special Characters
    3 AS product_id,
    'Product C!' AS product_name, -- Test special character
    'Type3' AS product_type,
    8888 AS revenue,
    'MEX' AS country,
    'CUST003' AS customer_id,
    CAST('2024-03-11' AS DATE) AS purchased_date,
    CAST('2024-03-11' AS DATE) AS invoice_date,
    1003 AS invoice_number,
    0 AS is_returned,
    90 AS customer_satisfaction_score,
    'Details of Product C!' AS product_details,
    CAST('2023-03-11' AS DATE) AS customer_first_purchased_date,
    'First Product C' AS customer_first_product,
    3000.75 AS customer_first_revenue,

    -- Error Cases: Invalid Scenarios
    4 AS product_id,
    'Product D' AS product_name,
    'Type4' AS product_type,
    -1000 AS revenue, -- Invalid revenue case
    'BRA' AS country,
    NULL AS customer_id, -- Null handling in a non-null field
    CAST('2024-05-01' AS DATE) AS purchased_date,
    CAST('2024-05-01' AS DATE) AS invoice_date,
    1004 AS invoice_number,
    1 AS is_returned,
    10 AS customer_satisfaction_score,
    'Details of Product D' AS product_details,
    CAST('2023-05-01' AS DATE) AS customer_first_purchased_date,
    'First Product D' AS customer_first_product,
    5000.25 AS customer_first_revenue,

    -- NULL handling scenario
    5 AS product_id,
    NULL AS product_name,
    'Type5' AS product_type,
    5000 AS revenue,
    'UK' AS country,
    'CUST005' AS customer_id,
    CAST('2024-09-16' AS DATE) AS purchased_date,
    CAST('2024-09-16' AS DATE) AS invoice_date,
    1005 AS invoice_number,
    0 AS is_returned,
    70 AS customer_satisfaction_score,
    NULL AS product_details,
    CAST('2023-09-16' AS DATE) AS customer_first_purchased_date,
    'First Product E' AS customer_first_product,
    6000.55 AS customer_first_revenue
)

-- Validate and convert data types before insertion
SELECT
  product_id,
  product_name,
  product_type,
  CAST(revenue AS BIGINT) AS revenue,
  country,
  customer_id,
  CAST(purchased_date AS DATE) AS purchased_date,
  CAST(invoice_date AS DATE) AS invoice_date,
  CAST(invoice_number AS BIGINT) AS invoice_number,
  CAST(is_returned AS BIGINT) AS is_returned,
  CAST(customer_satisfaction_score AS BIGINT) AS customer_satisfaction_score,
  product_details,
  CAST(customer_first_purchased_date AS DATE) AS customer_first_purchased_date,
  customer_first_product,
  CAST(customer_first_revenue AS DOUBLE) AS customer_first_revenue
FROM
  TestData;
