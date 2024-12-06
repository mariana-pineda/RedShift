-- Test data generation for f_inv_movmnt table
CREATE TABLE f_inv_movmnt (
    order_nbr INT,
    order_line_nbr INT,
    primary_qty INT,
    open_qty INT,
    shipped_qty INT,
    cancel_qty INT
);

INSERT INTO f_inv_movmnt (order_nbr, order_line_nbr, primary_qty, open_qty, shipped_qty, cancel_qty) VALUES
-- Test case: All quantities are non-null
(1, 1, 10, 5, 3, 2),
(1, 2, 20, 10, 5, 5),
-- Test case: Some quantities are null
(2, 1, NULL, 5, 3, 2),
(2, 2, 20, NULL, 5, 5),
(2, 3, 20, 10, NULL, 5),
(2, 4, 20, 10, 5, NULL),
-- Test case: All quantities are null
(3, 1, NULL, NULL, NULL, NULL),
-- Test case: Zero quantities
(4, 1, 0, 0, 0, 0),
-- Test case: Large quantities
(5, 1, 1000, 500, 300, 200),
-- Test case: Negative quantities
(6, 1, -10, -5, -3, -2),
-- Test case: Mixed positive and negative quantities
(7, 1, 10, -5, 3, -2),
-- Test case: Duplicate order_nbr and order_line_nbr
(8, 1, 10, 5, 3, 2),
(8, 1, 20, 10, 5, 5),
-- Test case: Edge case with maximum integer values
(9, 1, 2147483647, 2147483647, 2147483647, 2147483647),
-- Test case: Edge case with minimum integer values
(10, 1, -2147483648, -2147483648, -2147483648, -2147483648),
-- Test case: Single order with multiple lines
(11, 1, 10, 5, 3, 2),
(11, 2, 20, 10, 5, 5),
(11, 3, 30, 15, 8, 7),
-- Test case: Orders with only primary_qty
(12, 1, 10, NULL, NULL, NULL),
(12, 2, 20, NULL, NULL, NULL),
-- Test case: Orders with only open_qty
(13, 1, NULL, 10, NULL, NULL),
(13, 2, NULL, 20, NULL, NULL),
-- Test case: Orders with only shipped_qty
(14, 1, NULL, NULL, 10, NULL),
(14, 2, NULL, NULL, 20, NULL),
-- Test case: Orders with only cancel_qty
(15, 1, NULL, NULL, NULL, 10),
(15, 2, NULL, NULL, NULL, 20);
