-- Test Data Generation for purgo_playground Schema

-- Happy Path Test Data
-- Valid and expected scenarios for each table

-- programs table
INSERT INTO purgo_playground.programs (program_id, program_name, country_code, program_start_date) VALUES
(1, 'Program A', 'US', '2023-01-01 00:00:00'),
(2, 'Program B', 'CA', '2023-02-01 00:00:00');

-- interactions table
INSERT INTO purgo_playground.interactions (interaction_id, enrollment_id, interaction_date) VALUES
(1, 1, '2023-03-01 10:00:00'),
(2, 2, '2023-03-02 11:00:00');

-- f_order table
INSERT INTO purgo_playground.f_order (order_nbr, order_type, delivery_dt, order_qty, sched_dt, expected_shipped_dt, actual_shipped_dt, order_line_nbr, loc_tracker_id, shipping_add, primary_qty, open_qty, shipped_qty, order_desc, flag_return, flag_cancel, cancel_dt, cancel_qty, crt_dt, updt_dt) VALUES
('ORD001', 1, 20230101, 100.0, 20230102, 20230103, 20230104, 'LN001', 'LOC001', '123 Main St', 100.0, 0.0, 100.0, 'Order Description', 'N', 'N', NULL, 0.0, '2023-01-01 00:00:00', '2023-01-01 00:00:00');

-- Edge Case Test Data
-- Boundary conditions for each table

-- programs table with empty program_name
INSERT INTO purgo_playground.programs (program_id, program_name, country_code, program_start_date) VALUES
(3, '', 'MX', '2023-01-01 00:00:00');

-- interactions table with future interaction_date
INSERT INTO purgo_playground.interactions (interaction_id, enrollment_id, interaction_date) VALUES
(3, 3, '2024-01-01 10:00:00');

-- f_order table with zero order_qty
INSERT INTO purgo_playground.f_order (order_nbr, order_type, delivery_dt, order_qty, sched_dt, expected_shipped_dt, actual_shipped_dt, order_line_nbr, loc_tracker_id, shipping_add, primary_qty, open_qty, shipped_qty, order_desc, flag_return, flag_cancel, cancel_dt, cancel_qty, crt_dt, updt_dt) VALUES
('ORD002', 2, 20230105, 0.0, 20230106, 20230107, 20230108, 'LN002', 'LOC002', '456 Elm St', 0.0, 0.0, 0.0, 'Order Description', 'N', 'N', NULL, 0.0, '2023-01-05 00:00:00', '2023-01-05 00:00:00');

-- Error Case Test Data
-- Invalid inputs for each table

-- programs table with invalid country_code
INSERT INTO purgo_playground.programs (program_id, program_name, country_code, program_start_date) VALUES
(4, 'Program C', 'INVALID', '2023-01-01 00:00:00');

-- interactions table with non-existent enrollment_id
INSERT INTO purgo_playground.interactions (interaction_id, enrollment_id, interaction_date) VALUES
(4, 999, '2023-03-03 12:00:00');

-- f_order table with negative order_qty
INSERT INTO purgo_playground.f_order (order_nbr, order_type, delivery_dt, order_qty, sched_dt, expected_shipped_dt, actual_shipped_dt, order_line_nbr, loc_tracker_id, shipping_add, primary_qty, open_qty, shipped_qty, order_desc, flag_return, flag_cancel, cancel_dt, cancel_qty, crt_dt, updt_dt) VALUES
('ORD003', 3, 20230109, -10.0, 20230110, 20230111, 20230112, 'LN003', 'LOC003', '789 Pine St', -10.0, 0.0, -10.0, 'Order Description', 'N', 'N', NULL, 0.0, '2023-01-09 00:00:00', '2023-01-09 00:00:00');

-- Special Character and Format Test Data
-- Special characters and format variations for each table

-- programs table with special characters in program_name
INSERT INTO purgo_playground.programs (program_id, program_name, country_code, program_start_date) VALUES
(5, 'Program @#$%', 'UK', '2023-01-01 00:00:00');

-- interactions table with special characters in interaction_date
INSERT INTO purgo_playground.interactions (interaction_id, enrollment_id, interaction_date) VALUES
(5, 5, '2023-03-04 13:00:00');

-- f_order table with special characters in order_desc
INSERT INTO purgo_playground.f_order (order_nbr, order_type, delivery_dt, order_qty, sched_dt, expected_shipped_dt, actual_shipped_dt, order_line_nbr, loc_tracker_id, shipping_add, primary_qty, open_qty, shipped_qty, order_desc, flag_return, flag_cancel, cancel_dt, cancel_qty, crt_dt, updt_dt) VALUES
('ORD004', 4, 20230113, 50.0, 20230114, 20230115, 20230116, 'LN004', 'LOC004', '101 Maple St', 50.0, 0.0, 50.0, 'Order Desc @#$%', 'N', 'N', NULL, 0.0, '2023-01-13 00:00:00', '2023-01-13 00:00:00');
