-- SQL logic to calculate allocated_qty in inventory stock management

SELECT
    f_order.order_nbr,
    f_order.order_line_nbr,
    COALESCE(f_order.primary_qty, 0) + COALESCE(f_order.open_qty, 0) 
    + COALESCE(f_order.shipped_qty, 0) + COALESCE(f_order.cancel_qty, 0) AS allocated_qty
FROM
    f_inv_movmnt
JOIN
    f_order 
    ON f_inv_movmnt.order_nbr = f_order.order_nbr
    AND f_inv_movmnt.order_line_nbr = f_order.order_line_nbr
WHERE
    f_order.order_nbr IS NOT NULL
    AND f_order.order_line_nbr IS NOT NULL;
