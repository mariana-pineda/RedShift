-- Test code to validate the allocated_qty calculation

-- Update the f_order table to calculate allocated_qty
UPDATE f_order
SET allocated_qty = COALESCE(primary_qty, 0) + COALESCE(open_qty, 0) + COALESCE(shipped_qty, 0) + COALESCE(cancel_qty, 0);

-- Validation queries to compare expected and actual outcomes

-- Test case: All quantities are non-null
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 20 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) IN ((1, 1), (1, 2), (2, 1));

-- Test case: Some quantities are null
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 20 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) IN ((2, 2), (3, 1), (3, 2), (4, 1));

-- Test case: All quantities are zero
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 0 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (4, 2);

-- Test case: Large quantities
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 10000 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (5, 1);

SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 14000 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (5, 2);

-- Test case: Negative quantities
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = -20 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) IN ((6, 1), (6, 2));

-- Test case: Mixed positive and negative quantities
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 6 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (7, 1);

SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = -6 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (7, 2);

-- Test case: Edge case with maximum integer values
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 2147483647 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) IN ((8, 1), (8, 2));

-- Test case: Edge case with minimum integer values
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = -2147483648 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) IN ((9, 1), (9, 2));

-- Test case: Random quantities
SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 30 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (10, 1);

SELECT order_nbr, order_line_nbr, allocated_qty, 
       CASE WHEN allocated_qty = 18 THEN 'Pass' ELSE 'Fail' END AS result
FROM f_order
WHERE (order_nbr, order_line_nbr) = (10, 2);
