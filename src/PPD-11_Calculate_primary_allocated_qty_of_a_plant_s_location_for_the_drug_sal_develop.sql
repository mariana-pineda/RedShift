UPDATE f_order
SET allocated_qty = COALESCE(
  GREATEST(primary_qty, 0), 0
) + COALESCE(
  GREATEST(open_qty, 0), 0
) + COALESCE(
  GREATEST(shipped_qty, 0), 0
) + COALESCE(
  GREATEST(cancel_qty, 0), 0
)
FROM f_inv_movmnt
WHERE f_order.order_nbr = f_inv_movmnt.order_nbr
  AND f_order.order_line_nbr = f_inv_movmnt.order_line_nbr;
