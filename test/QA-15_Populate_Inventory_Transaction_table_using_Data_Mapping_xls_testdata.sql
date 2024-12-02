-- Create a table to store test data for inventory transactions
CREATE TABLE test_inventory_transaction (
    transaction_id INT PRIMARY KEY,
    item_id INT,
    quantity INT,
    transaction_type VARCHAR(50),
    source VARCHAR(100),
    timestamp TIMESTAMP
);

-- Insert test data to validate the correctness of data migration
-- Condition: Validate different transaction types (inbound, outbound)
INSERT INTO test_inventory_transaction VALUES (1, 101, 50, 'inbound', 'Supplier A', '2023-10-01 10:00:00');
INSERT INTO test_inventory_transaction VALUES (2, 102, -30, 'outbound', 'Customer B', '2023-10-01 11:00:00');

-- Condition: Validate transactions with different suppliers and customers
INSERT INTO test_inventory_transaction VALUES (3, 103, 100, 'inbound', 'Supplier C', '2023-10-02 09:00:00');
INSERT INTO test_inventory_transaction VALUES (4, 104, -50, 'outbound', 'Customer D', '2023-10-02 13:00:00');

-- Condition: Validate transactions at different timestamps
INSERT INTO test_inventory_transaction VALUES (5, 105, 20, 'inbound', 'Supplier E', '2023-10-03 08:45:00');
INSERT INTO test_inventory_transaction VALUES (6, 106, -10, 'outbound', 'Customer F', '2023-10-03 15:30:00');

-- Condition: Validate zero quantity to test edge cases
INSERT INTO test_inventory_transaction VALUES (7, 107, 0, 'adjustment', 'Warehouse G', '2023-10-04 10:00:00');

-- Condition: Validate large quantities for performance & scalability
INSERT INTO test_inventory_transaction VALUES (8, 108, 1000, 'inbound', 'Supplier H', '2023-10-05 09:15:00');
INSERT INTO test_inventory_transaction VALUES (9, 109, -500, 'outbound', 'Customer I', '2023-10-05 11:45:00');

-- Condition: Validate data migration from multiple sources
INSERT INTO test_inventory_transaction VALUES (10, 110, 70, 'inbound', 'Supplier J', '2023-10-06 12:00:00');
INSERT INTO test_inventory_transaction VALUES (11, 111, -40, 'outbound', 'Customer K', '2023-10-06 14:00:00');

-- Condition: Validate uniqueness of transaction IDs
INSERT INTO test_inventory_transaction VALUES (12, 112, 60, 'inbound', 'Supplier L', '2023-10-07 16:00:00');
INSERT INTO test_inventory_transaction VALUES (13, 113, -25, 'outbound', 'Customer M', '2023-10-07 17:30:00');

-- Condition: Validate security by simulating unauthorized transaction data
-- (In a real-world scenario, implement security checks, this entry here is just for completeness)
INSERT INTO test_inventory_transaction VALUES (14, 114, -15, 'outbound-unauthorized', 'Unknown', '2023-10-08 10:00:00');

-- Condition: Validate transactions with missing optional information
INSERT INTO test_inventory_transaction VALUES (15, 115, 200, 'inbound', NULL, '2023-10-09 09:30:00');
INSERT INTO test_inventory_transaction VALUES (16, 116, -75, 'outbound', NULL, '2023-10-09 10:45:00');

-- Condition: Validate multiple transactions for the same item to check aggregate functions
INSERT INTO test_inventory_transaction VALUES (17, 117, 150, 'inbound', 'Supplier N', '2023-10-10 14:00:00');
INSERT INTO test_inventory_transaction VALUES (18, 117, -100, 'outbound', 'Customer O', '2023-10-10 16:20:00');

-- Condition: Extra valid data samples to ensure the data generation meets record count requirement
INSERT INTO test_inventory_transaction VALUES (19, 118, 300, 'inbound', 'Supplier P', '2023-10-11 08:10:00');
INSERT INTO test_inventory_transaction VALUES (20, 119, -10, 'outbound', 'Customer Q', '2023-10-11 10:30:00');
INSERT INTO test_inventory_transaction VALUES (21, 120, 45, 'inbound', 'Supplier R', '2023-10-12 09:00:00');
INSERT INTO test_inventory_transaction VALUES (22, 120, -20, 'outbound', 'Customer S', '2023-10-12 11:00:00');
INSERT INTO test_inventory_transaction VALUES (23, 121, 200, 'inbound', 'Supplier T', '2023-10-13 13:00:00');
INSERT INTO test_inventory_transaction VALUES (24, 122, 5, 'inbound', 'Supplier U', '2023-10-14 15:10:00');
INSERT INTO test_inventory_transaction VALUES (25, 122, -3, 'outbound', 'Customer V', '2023-10-14 16:50:00');
INSERT INTO test_inventory_transaction VALUES (26, 123, 400, 'inbound', 'Supplier W', '2023-10-15 09:00:00');
INSERT INTO test_inventory_transaction VALUES (27, 124, -150, 'outbound', 'Customer X', '2023-10-15 10:00:00');
INSERT INTO test_inventory_transaction VALUES (28, 125, 30, 'inbound', 'Supplier Y', '2023-10-16 10:00:00');
INSERT INTO test_inventory_transaction VALUES (29, 126, -30, 'outbound', 'Customer Z', '2023-10-16 11:30:00');
INSERT INTO test_inventory_transaction VALUES (30, 127, 50, 'inbound', 'Supplier A1', '2023-10-17 12:30:00');
