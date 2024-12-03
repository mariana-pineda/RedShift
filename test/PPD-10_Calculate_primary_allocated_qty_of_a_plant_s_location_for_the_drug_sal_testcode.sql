-- Test script to validate the calculation of allocated_qty

-- Test calculation logic
SELECT
    f_order.order_nbr,
    f_order.order_line_nbr,
    COALESCE(f_order.primary_qty, 0) + COALESCE(f_order.open_qty, 0) 
    + COALESCE(f_order.shipped_qty, 0) + COALESCE(f_order.cancel_qty, 0) AS calculated_allocated_qty
FROM
    f_order
WHERE
    EXISTS (
        SELECT 1
        FROM f_order
        WHERE f_order.order_nbr IS NOT NULL
          AND f_order.order_line_nbr IS NOT NULL
    );

-- Expected results for each set of data
CREATE TABLE expected_results (
    order_nbr INT,
    order_line_nbr INT,
    expected_allocated_qty INT
);

INSERT INTO expected_results (order_nbr, order_line_nbr, expected_allocated_qty) VALUES
(1, 1, 16),  -- 10 + 5 + 0 + 1
(1, 2, 12),  -- 0 + 10 + 2 + 0
(2, 1, 15),  -- 5 + 0 + 5 + 5
(2, 2, 0),   -- 0 + 0 + 0 + 0
(3, 1, 9),   -- 3 + 3 + 3 + 0
(3, 2, 0),   -- All NULLs treated as zero
(4, 1, 0),   -- All zeros
(4, 2, 10),  -- 1 + 2 + 3 + 4
(5, 1, 15),  -- 0 + 10 + 0 + 5
(5, 2, 1),   -- 0 + 0 + 0 + 1
(6, 1, 10),  -- 10 + 0 + 0 + 0
(6, 2, 2),   -- 0 + 2 + 0 + 0
(7, 1, 3),   -- 0 + 0 + 3 + 0
(7, 2, 4),   -- 0 + 0 + 0 + 4
(8, 1, 5),   -- -5 + 0 + 5 + 5
(8, 2, 5),   -- 5 + -5 + 0 + 5
(9, 1, 0),   -- 0 + 0 + 0 + 0
(9, 2, 0),   -- 0 + 0 + 0 + 0
(10, 1, 0),  -- 0 + 0 + 0 + 0 
(10, 2, 5),  -- 0 + 5 + -3 + 3
(11, 1, 5),  -- 0 + 0 + -5 + 10
(11, 2, -20),-- -5 + -5 + -5 + -5
(12, 1, -1), -- 0 + 0 + 0 + -1
(12, 2, -2), -- 0 + 0 + 0 + -2
(13, 1, 40), -- 10 + 10 + 10 + 10
(13, 2, 20), -- 5 + 5 + 5 + 5
(14, 1, 5),  -- 0 + 5 + 0 + 0
(14, 2, 5);  -- 5 + 0 + 0 + 0

-- Validate actual vs expected
SELECT
    r.order_nbr,
    r.order_line_nbr,
    r.calculated_allocated_qty,
    e.expected_allocated_qty,
    CASE 
        WHEN r.calculated_allocated_qty = e.expected_allocated_qty THEN 'Pass'
        ELSE 'Fail'
    END AS validation_status
FROM (
    SELECT
        f_order.order_nbr,
        f_order.order_line_nbr,
        COALESCE(f_order.primary_qty, 0) + COALESCE(f_order.open_qty, 0) 
        + COALESCE(f_order.shipped_qty, 0) + COALESCE(f_order.cancel_qty, 0) AS calculated_allocated_qty
    FROM f_order
) r
JOIN expected_results e
ON r.order_nbr = e.order_nbr
AND r.order_line_nbr = e.order_line_nbr;
