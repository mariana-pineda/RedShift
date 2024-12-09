-- Test code to validate the calculation of allocated_qty

WITH calculated_allocated_qty AS (
    SELECT 
        f.order_nbr,
        f.order_line_nbr,
        COALESCE(SUM(COALESCE(m.primary_qty, 0) + COALESCE(m.open_qty, 0) + COALESCE(m.shipped_qty, 0) + COALESCE(m.cancel_qty, 0)), 0) AS allocated_qty
    FROM 
        f_order f
    LEFT JOIN 
        f_inv_movmnt m ON f.order_nbr = m.order_nbr AND f.order_line_nbr = m.order_line_nbr
    GROUP BY 
        f.order_nbr, f.order_line_nbr
)

-- Validate each test case
SELECT 
    c.order_nbr,
    c.order_line_nbr,
    c.allocated_qty,
    CASE 
        WHEN c.order_nbr = 1 AND c.allocated_qty = 20 THEN 'Pass'
        WHEN c.order_nbr = 2 AND c.allocated_qty = 40 THEN 'Pass'
        WHEN c.order_nbr = 3 AND c.allocated_qty = 20 THEN 'Pass'
        WHEN c.order_nbr = 4 AND c.allocated_qty = 25 THEN 'Pass'
        WHEN c.order_nbr = 5 AND c.allocated_qty = 30 THEN 'Pass'
        WHEN c.order_nbr = 6 AND c.allocated_qty = 30 THEN 'Pass'
        WHEN c.order_nbr = 7 AND c.allocated_qty = 0 THEN 'Pass'
        WHEN c.order_nbr = 8 AND c.allocated_qty = 0 THEN 'Pass'
        WHEN c.order_nbr = 9 AND c.allocated_qty = -20 THEN 'Pass'
        WHEN c.order_nbr = 10 AND c.allocated_qty = 200000 THEN 'Pass'
        WHEN c.order_nbr = 11 AND c.allocated_qty = 45 THEN 'Pass'
        WHEN c.order_nbr = 12 AND c.allocated_qty = 45 THEN 'Pass'
        WHEN c.order_nbr = 13 AND c.allocated_qty = 20 THEN 'Pass'
        WHEN c.order_nbr = 14 AND c.allocated_qty = 40 THEN 'Pass'
        WHEN c.order_nbr = 15 AND c.allocated_qty = 20 THEN 'Pass'
        WHEN c.order_nbr = 16 AND c.allocated_qty = 25 THEN 'Pass'
        WHEN c.order_nbr = 17 AND c.allocated_qty = 30 THEN 'Pass'
        WHEN c.order_nbr = 18 AND c.allocated_qty = 30 THEN 'Pass'
        WHEN c.order_nbr = 19 AND c.allocated_qty = 6 THEN 'Pass'
        WHEN c.order_nbr = 20 AND c.allocated_qty = -6 THEN 'Pass'
        ELSE 'Fail'
    END AS test_result
FROM 
    calculated_allocated_qty c
ORDER BY 
    c.order_nbr, c.order_line_nbr;
