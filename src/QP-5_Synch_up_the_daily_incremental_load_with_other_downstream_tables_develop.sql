-- SQL to synchronize d_product_sk table with d_product table

-- Step 1: Delete records from d_product_sk that exist in d_product
DELETE FROM d_product_sk
WHERE prod_id IN (
    SELECT prod_id
    FROM d_product
);

-- Step 2: Insert records into d_product_sk if they exist in d_product but not in d_product_sk
INSERT INTO d_product_sk (prod_id, plant_key_sn)
SELECT prod_id, 
       ROW_NUMBER() OVER (ORDER BY prod_id) + (SELECT COALESCE(MAX(plant_key_sn), 0) FROM d_product_sk) AS plant_key_sn
FROM d_product
WHERE prod_id NOT IN (
    SELECT prod_id
    FROM d_product_sk
);

-- Note: 
-- ROW_NUMBER() function is used to auto-increment plant_key_sn starting from the maximum value already present in d_product_sk.
-- Error handling, logging, and performance optimizations are assumed to be handled by the surrounding application or execution framework.
