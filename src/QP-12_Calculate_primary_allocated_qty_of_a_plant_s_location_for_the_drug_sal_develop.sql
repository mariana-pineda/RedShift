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
SELECT 
    order_nbr,
    order_line_nbr,
    allocated_qty
FROM 
    calculated_allocated_qty
ORDER BY 
    order_nbr, order_line_nbr;
