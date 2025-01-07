-- Test data generation for f_order table
CREATE TABLE f_order (
    order_nbr INT,
    order_line_nbr INT,
    primary_qty INT,
    open_qty INT,
    shipped_qty INT,
    cancel_qty INT,
    allocated_qty INT
);

-- Generate 20-30 records for testing
INSERT INTO f_order (order_nbr, order_line_nbr, primary_qty, open_qty, shipped_qty, cancel_qty)
VALUES
    -- Test case: All quantities are non-null
    (1, 1, 10, 5, 3, 2),  -- allocated_qty should be 20
    (1, 2, 15, 0, 5, 0),  -- allocated_qty should be 20
    (2, 1, 0, 10, 5, 5),  -- allocated_qty should be 20
    -- Test case: Some quantities are null
    (2, 2, NULL, 10, 5, 5),  -- allocated_qty should be 20 (NULL treated as 0)
    (3, 1, 10, NULL, 5, 5),  -- allocated_qty should be 20 (NULL treated as 0)
    (3, 2, 10, 5, NULL, 5),  -- allocated_qty should be 20 (NULL treated as 0)
    (4, 1, 10, 5, 5, NULL),  -- allocated_qty should be 20 (NULL treated as 0)
    -- Test case: All quantities are zero
    (4, 2, 0, 0, 0, 0),  -- allocated_qty should be 0
    -- Test case: Large quantities
    (5, 1, 1000, 2000, 3000, 4000),  -- allocated_qty should be 10000
    (5, 2, 5000, 4000, 3000, 2000),  -- allocated_qty should be 14000
    -- Test case: Negative quantities
    (6, 1, -10, -5, -3, -2),  -- allocated_qty should be -20
    (6, 2, -15, 0, -5, 0),  -- allocated_qty should be -20
    -- Test case: Mixed positive and negative quantities
    (7, 1, 10, -5, 3, -2),  -- allocated_qty should be 6
    (7, 2, -10, 5, -3, 2),  -- allocated_qty should be -6
    -- Test case: Edge case with maximum integer values
    (8, 1, 2147483647, 0, 0, 0),  -- allocated_qty should be 2147483647
    (8, 2, 0, 2147483647, 0, 0),  -- allocated_qty should be 2147483647
    -- Test case: Edge case with minimum integer values
    (9, 1, -2147483648, 0, 0, 0),  -- allocated_qty should be -2147483648
    (9, 2, 0, -2147483648, 0, 0),  -- allocated_qty should be -2147483648
    -- Test case: Random quantities
    (10, 1, 7, 8, 9, 6),  -- allocated_qty should be 30
    (10, 2, 3, 4, 5, 6);  -- allocated_qty should be 18
