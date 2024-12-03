-- Generate test data for 'f_order' table with different combinations
CREATE TABLE f_order (
    order_nbr INT,
    order_line_nbr INT,
    primary_qty INT,
    open_qty INT,
    shipped_qty INT,
    cancel_qty INT
);

-- Test data to cover various scenarios including null handling and quantity calculation
INSERT INTO f_order (order_nbr, order_line_nbr, primary_qty, open_qty, shipped_qty, cancel_qty) VALUES
(1, 1, 10, 5, 0, 1),               -- All quantities are specified
(1, 2, NULL, 10, 2, 0),            -- primary_qty is NULL
(2, 1, 5, NULL, 5, 5),             -- open_qty is NULL
(2, 2, 0, 0, NULL, 0),             -- shipped_qty is NULL
(3, 1, 3, 3, 3, NULL),             -- cancel_qty is NULL
(3, 2, NULL, NULL, NULL, NULL),    -- All quantities are NULL
(4, 1, 0, 0, 0, 0),                -- All quantities are zero
(4, 2, 1, 2, 3, 4),                -- Mixed positive quantities
(5, 1, 0, 10, NULL, 5),            -- Mixed NULL and non-zero quantities
(5, 2, NULL, NULL, NULL, 1),       -- Mostly NULL with one non-zero
(6, 1, 10, NULL, NULL, NULL),      -- One non-null quantity
(6, 2, NULL, 2, NULL, NULL),       -- Another single non-null quantity
(7, 1, NULL, NULL, 3, NULL),       -- Another case of single non-null
(7, 2, NULL, NULL, NULL, 4),       -- Yet another single non-null
(8, 1, -5, NULL, 5, 5),            -- Handling negative values
(8, 2, 5, -5, NULL, 5),            -- Another negative value scenario
(9, 1, 0, NULL, NULL, NULL),       -- Edge case with only one zero
(9, 2, NULL, 0, NULL, NULL),       -- Zero in the middle
(10, 1, NULL, NULL, 0, NULL),      -- Zero at the end
(10, 2, NULL, 5, -3, 3),           -- Combination of positive, negative, and null
(11, 1, 0, 0, -5, 10),             -- A combination involving zero and negatives
(11, 2, -5, -5, -5, -5),           -- All negative values
(12, 1, NULL, NULL, NULL, -1),     -- Mostly NULL with one negative
(12, 2, 0, 0, 0, -2),              -- Mostly zero with one negative
(13, 1, 10, 10, 10, 10),           -- All values positive and equal
(13, 2, 5, 5, 5, 5),               -- Another equal but lesser positive
(14, 1, NULL, 5, NULL, NULL),      -- NULL interspersed with positive
(14, 2, 5, NULL, NULL, NULL);      -- A single non-null positive
