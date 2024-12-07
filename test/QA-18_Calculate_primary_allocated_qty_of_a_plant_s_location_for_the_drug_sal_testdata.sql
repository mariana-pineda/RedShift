-- Test data generation for f_inv_movmnt table
CREATE TEMP TABLE f_inv_movmnt (
    order_nbr INT,
    order_line_nbr INT,
    primary_qty INT,
    open_qty INT,
    shipped_qty INT,
    cancel_qty INT
);

INSERT INTO f_inv_movmnt (order_nbr, order_line_nbr, primary_qty, open_qty, shipped_qty, cancel_qty) VALUES
(1, 1, 10, 5, 3, 2),  -- Normal case with all values present
(2, 1, NULL, 5, 3, 2),  -- Null primary_qty
(3, 1, 10, NULL, 3, 2),  -- Null open_qty
(4, 1, 10, 5, NULL, 2),  -- Null shipped_qty
(5, 1, 10, 5, 3, NULL),  -- Null cancel_qty
(6, 1, NULL, NULL, NULL, NULL),  -- All values null
(7, 1, 0, 0, 0, 0),  -- All values zero
(8, 1, 10, 5, 3, 2),  -- Duplicate entry for testing duplicates
(8, 1, 10, 5, 3, 2),  -- Duplicate entry for testing duplicates
(9, 1, 15, 5, 5, 5),  -- Different values for variety
(10, 1, 20, 10, 5, 0),  -- Zero cancel_qty
(11, 1, 0, 10, 5, 5),  -- Zero primary_qty
(12, 1, 10, 0, 5, 5),  -- Zero open_qty
(13, 1, 10, 5, 0, 5),  -- Zero shipped_qty
(14, 1, 10, 5, 5, 0),  -- Zero cancel_qty
(15, 1, 100, 50, 30, 20),  -- Large values
(16, 1, 1, 1, 1, 1),  -- Small values
(17, 1, 10, 5, 3, 2),  -- Normal case with all values present
(18, 1, 10, 5, 3, 2),  -- Normal case with all values present
(19, 1, 10, 5, 3, 2),  -- Normal case with all values present
(20, 1, 10, 5, 3, 2);  -- Normal case with all values present

-- Test data generation for f_order table
CREATE TEMP TABLE f_order (
    order_nbr INT,
    order_line_nbr INT
);

INSERT INTO f_order (order_nbr, order_line_nbr) VALUES
(1, 1),  -- Matching entry in f_inv_movmnt
(2, 1),  -- Matching entry in f_inv_movmnt
(3, 1),  -- Matching entry in f_inv_movmnt
(4, 1),  -- Matching entry in f_inv_movmnt
(5, 1),  -- Matching entry in f_inv_movmnt
(6, 1),  -- Matching entry in f_inv_movmnt
(7, 1),  -- Matching entry in f_inv_movmnt
(8, 1),  -- Matching entry in f_inv_movmnt
(9, 1),  -- Matching entry in f_inv_movmnt
(10, 1),  -- Matching entry in f_inv_movmnt
(11, 1),  -- Matching entry in f_inv_movmnt
(12, 1),  -- Matching entry in f_inv_movmnt
(13, 1),  -- Matching entry in f_inv_movmnt
(14, 1),  -- Matching entry in f_inv_movmnt
(15, 1),  -- Matching entry in f_inv_movmnt
(16, 1),  -- Matching entry in f_inv_movmnt
(17, 1),  -- Matching entry in f_inv_movmnt
(18, 1),  -- Matching entry in f_inv_movmnt
(19, 1),  -- Matching entry in f_inv_movmnt
(20, 1);  -- Matching entry in f_inv_movmnt
