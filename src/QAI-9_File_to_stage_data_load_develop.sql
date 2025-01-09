-- Load the CSV files into temporary views
CREATE OR REPLACE TEMPORARY VIEW product_revenue AS
SELECT * FROM csv.`/Volumes/agilisium_playground/purgo_playground/d_product_revenue_csv/d_product_revenue.csv`;

CREATE OR REPLACE TEMPORARY VIEW customer AS
SELECT * FROM csv.`/Volumes/agilisium_playground/purgo_playground/d_product_revenue_csv/customer.csv`;

-- Perform the left join and create the surrogate key
SELECT 
  *,
  sha2(concat_ws('', product_id, customer_id, revenue, product_name, customer_name, customer_email), 256) AS surrogate_key
FROM 
  product_revenue
LEFT JOIN 
  customer
ON 
  product_revenue.customer_id = customer.customer_id;
