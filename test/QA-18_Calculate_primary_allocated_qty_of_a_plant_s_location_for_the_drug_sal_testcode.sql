-- Test code to validate the calculation of allocated_qty

WITH calculated_allocated_qty AS (
    SELECT 
        f_order.order_nbr,
        f_order.order_line_nbr,
        COALESCE(primary_qty, 0) + COALESCE(open_qty, 0) + COALESCE(shipped_qty, 0) + COALESCE(cancel_qty, 0) AS allocated_qty
    FROM 
        f_order
    JOIN 
        f_inv_movmnt ON f_order.order_nbr = f_inv_movmnt.order_nbr 
        AND f_order.order_line_nbr = f_inv_movmnt.order_line_nbr
    GROUP BY 
        f_order.order_nbr, f_order.order_line_nbr
)

-- Validate the results
SELECT 
    c.order_nbr,
    c.order_line_nbr,
    c.allocated_qty AS calculated_allocated_qty,
    CASE 
        WHEN c.allocated_qty = e.expected_allocated_qty THEN 'PASS'
        ELSE 'FAIL'
    END AS validation_result
FROM 
    calculated_allocated_qty c
JOIN (
    SELECT 
        order_nbr,
        order_line_nbr,
        COALESCE(primary_qty, 0) + COALESCE(open_qty, 0) + COALESCE(shipped_qty, 0) + COALESCE(cancel_qty, 0) AS expected_allocated_qty
    FROM 
        f_inv_movmnt
    WHERE 
        (order_nbr, order_line_nbr) IN (SELECT order_nbr, order_line_nbr FROM f_order)
    GROUP BY 
        order_nbr, order_line_nbr
) e ON c.order_nbr = e.order_nbr AND c.order_line_nbr = e.order_line_nbr;
