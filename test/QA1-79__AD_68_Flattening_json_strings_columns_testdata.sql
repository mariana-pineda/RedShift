-- SQL Query to select fields from product_details JSON string in the d_product_revenue table

SELECT 
  -- Extract batch_number from JSON
  from_json(product_details, 'STRUCT<batch_number: STRING, expiration_date: STRING, manufacturing_site: STRING, regulatory_approval: STRING, price: DOUBLE>').batch_number AS batch_number,
  
  -- Extract expiration_date from JSON and cast it to STRING as per JSON definition
  from_json(product_details, 'STRUCT<batch_number: STRING, expiration_date: STRING, manufacturing_site: STRING, regulatory_approval: STRING, price: DOUBLE>').expiration_date AS expiration_date,
  
  -- Extract manufacturing_site from JSON
  from_json(product_details, 'STRUCT<batch_number: STRING, expiration_date: STRING, manufacturing_site: STRING, regulatory_approval: STRING, price: DOUBLE>').manufacturing_site AS manufacturing_site,
  
  -- Extract regulatory_approval from JSON
  from_json(product_details, 'STRUCT<batch_number: STRING, expiration_date: STRING, manufacturing_site: STRING, regulatory_approval: STRING, price: DOUBLE>').regulatory_approval AS regulatory_approval,
  
  -- Extract price from JSON and cast it to DOUBLE
  from_json(product_details, 'STRUCT<batch_number: STRING, expiration_date: STRING, manufacturing_site: STRING, regulatory_approval: STRING, price: DOUBLE>').price AS price
FROM 
  purgo_playground.d_product_revenue
