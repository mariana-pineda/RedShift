-- SQL logic to calculate allocated_qty in the f_order table

UPDATE f_order
SET allocated_qty = COALESCE(primary_qty, 0) + COALESCE(open_qty, 0) + COALESCE(shipped_qty, 0) + COALESCE(cancel_qty, 0)
WHERE EXISTS (
    SELECT 1
    FROM f_inv_movmnt
    WHERE f_inv_movmnt.order_nbr = f_order.order_nbr
    AND f_inv_movmnt.order_line_nbr = f_order.order_line_nbr
);
