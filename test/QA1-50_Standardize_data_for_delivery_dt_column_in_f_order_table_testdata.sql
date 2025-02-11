-- Generate test data for purgo_playground.f_order table

-- Happy path test data
INSERT INTO purgo_playground.f_order VALUES
('ORD001', 1, 20240321, 100.0, 20240320, 20240322, 20240323, 'OLN001', 'LT001', '123 Main St', 100.0, 0.0, 100.0, 'Order Description', 'N', 'N', 20240324, 0.0, '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('ORD002', 2, 20240322, 200.0, 20240321, 20240323, 20240324, 'OLN002', 'LT002', '456 Elm St', 200.0, 0.0, 200.0, 'Order Description', 'N', 'N', 20240325, 0.0, '2024-03-22T00:00:00.000+0000', '2024-03-22T00:00:00.000+0000');

-- Edge cases
-- Boundary condition for delivery_dt
INSERT INTO purgo_playground.f_order VALUES
('ORD003', 3, 20240101, 300.0, 20231231, 20240102, 20240103, 'OLN003', 'LT003', '789 Oak St', 300.0, 0.0, 300.0, 'Order Description', 'N', 'N', 20240104, 0.0, '2024-01-01T00:00:00.000+0000', '2024-01-01T00:00:00.000+0000');

-- Error cases
-- Invalid delivery_dt format
INSERT INTO purgo_playground.f_order VALUES
('ORD004', 4, 20241301, 400.0, 20241231, 20241302, 20241303, 'OLN004', 'LT004', '101 Pine St', 400.0, 0.0, 400.0, 'Order Description', 'N', 'N', 20241304, 0.0, '2024-13-01T00:00:00.000+0000', '2024-13-01T00:00:00.000+0000');

-- NULL handling scenarios
INSERT INTO purgo_playground.f_order VALUES
('ORD005', 5, NULL, 500.0, NULL, NULL, NULL, 'OLN005', 'LT005', '202 Birch St', 500.0, 0.0, 500.0, 'Order Description', 'N', 'N', NULL, 0.0, '2024-03-25T00:00:00.000+0000', '2024-03-25T00:00:00.000+0000');

-- Special characters and multi-byte characters
INSERT INTO purgo_playground.f_order VALUES
('ORD006', 6, 20240326, 600.0, 20240325, 20240327, 20240328, 'OLN006', 'LT006', '303 Maple St', 600.0, 0.0, 600.0, 'Order Description with special char !@#$%^&*()', 'N', 'N', 20240329, 0.0, '2024-03-26T00:00:00.000+0000', '2024-03-26T00:00:00.000+0000'),
('ORD007', 7, 20240327, 700.0, 20240326, 20240328, 20240329, 'OLN007', 'LT007', '404 Cedar St', 700.0, 0.0, 700.0, 'Order Description with multi-byte 文字', 'N', 'N', 20240330, 0.0, '2024-03-27T00:00:00.000+0000', '2024-03-27T00:00:00.000+0000');

-- Additional diverse test records
INSERT INTO purgo_playground.f_order VALUES
('ORD008', 8, 20240328, 800.0, 20240327, 20240329, 20240330, 'OLN008', 'LT008', '505 Walnut St', 800.0, 0.0, 800.0, 'Order Description', 'N', 'N', 20240331, 0.0, '2024-03-28T00:00:00.000+0000', '2024-03-28T00:00:00.000+0000'),
('ORD009', 9, 20240329, 900.0, 20240328, 20240330, 20240331, 'OLN009', 'LT009', '606 Cherry St', 900.0, 0.0, 900.0, 'Order Description', 'N', 'N', 20240401, 0.0, '2024-03-29T00:00:00.000+0000', '2024-03-29T00:00:00.000+0000'),
('ORD010', 10, 20240330, 1000.0, 20240329, 20240331, 20240401, 'OLN010', 'LT010', '707 Spruce St', 1000.0, 0.0, 1000.0, 'Order Description', 'N', 'N', 20240402, 0.0, '2024-03-30T00:00:00.000+0000', '2024-03-30T00:00:00.000+0000');
