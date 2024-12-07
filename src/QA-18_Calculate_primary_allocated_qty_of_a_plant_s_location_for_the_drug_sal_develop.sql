WITH calculated_allocated_qty AS (
    SELECT 
        f_order.order_nbr,
        f_order.order_line_nbr,
        COALESCE(SUM(primary_qty), 0) + COALESCE(SUM(open_qty), 0) + COALESCE(SUM(shipped_qty), 0) + COALESCE(SUM(cancel_qty), 0) AS allocated_qty
    FROM 
        f_order
    JOIN 
        f_inv_movmnt ON f_order.order_nbr = f_inv_movmnt.order_nbr 
        AND f_order.order_line_nbr = f_inv_movmnt.order_line_nbr
    GROUP BY 
        f_order.order_nbr, f_order.order_line_nbr
)

SELECT 
    order_nbr,
    order_line_nbr,
    allocated_qty
FROM 
    calculated_allocated_qty;
