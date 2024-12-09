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
(2, 1, 20, 10, 5, 5),
-- Test case: Some quantities are null
(3, 1, NULL, 10, 5, 5),
(4, 1, 15, NULL, 5, 5),
(5, 1, 15, 10, NULL, 5),
(6, 1, 15, 10, 5, NULL),
-- Test case: All quantities are null
(7, 1, NULL, NULL, NULL, NULL),
-- Test case: Zero quantities
(8, 1, 0, 0, 0, 0),
-- Test case: Negative quantities
(9, 1, -10, -5, -3, -2),
-- Test case: Large quantities
(10, 1, 100000, 50000, 30000, 20000),
-- Test case: Duplicate entries for the same order_nbr and order_line_nbr
(11, 1, 10, 5, 3, 2),
(11, 1, 20, 10, 5, 5),
-- Test case: Different order_line_nbr for the same order_nbr
(12, 1, 10, 5, 3, 2),
(12, 2, 20, 10, 5, 5),
-- Test case: Different order_nbr for the same order_line_nbr
(13, 1, 10, 5, 3, 2),
(14, 1, 20, 10, 5, 5),
-- Test case: Orders with zero and non-zero quantities
(15, 1, 0, 10, 5, 5),
(16, 1, 15, 0, 5, 5),
(17, 1, 15, 10, 0, 5),
(18, 1, 15, 10, 5, 0),
-- Test case: Orders with mixed positive and negative quantities
(19, 1, 10, -5, 3, -2),
(20, 1, -10, 5, -3, 2);

-- Test data generation for f_order table
CREATE TABLE f_order (
    order_nbr INT,
    order_line_nbr INT
);

INSERT INTO f_order (order_nbr, order_line_nbr) VALUES
-- Test case: Matching entries in f_inv_movmnt
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(12, 2),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(17, 1),
(18, 1),
(19, 1),
(20, 1),
-- Test case: Non-matching entries in f_inv_movmnt
(21, 1),
(22, 1);
