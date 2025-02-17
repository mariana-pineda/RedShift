-- Create test data for purgo_playground.f_inv_movmnt table

-- Happy path test data
INSERT INTO purgo_playground.f_inv_movmnt (txn_id, inv_loc, financial_qty, net_qty, expired_qt, item_nbr, unit_cost, um_rate, plant_loc_cd, inv_stock_reference, stock_type, qty_on_hand, qty_shipped, cancel_dt, flag_active, crt_dt, updt_dt)
VALUES
('TXN001', 'LOC001', 100.0, 90.0, 0, 'ITEM001', 10.0, 1.0, 'PLANT001', 'REF001', 'STOCK001', 100.0, 10.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN002', 'LOC002', 200.0, 180.0, 0, 'ITEM002', 20.0, 1.0, 'PLANT002', 'REF002', 'STOCK002', 200.0, 20.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000');

-- Edge cases
INSERT INTO purgo_playground.f_inv_movmnt (txn_id, inv_loc, financial_qty, net_qty, expired_qt, item_nbr, unit_cost, um_rate, plant_loc_cd, inv_stock_reference, stock_type, qty_on_hand, qty_shipped, cancel_dt, flag_active, crt_dt, updt_dt)
VALUES
('TXN003', 'LOC003', 0.0, 0.0, 0, 'ITEM003', 0.0, 0.0, 'PLANT003', 'REF003', 'STOCK003', 0.0, 0.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN004', 'LOC004', 9999999999.99, 9999999999.99, 0, 'ITEM004', 9999999999.99, 1.0, 'PLANT004', 'REF004', 'STOCK004', 9999999999.99, 0.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000');

-- Error cases
INSERT INTO purgo_playground.f_inv_movmnt (txn_id, inv_loc, financial_qty, net_qty, expired_qt, item_nbr, unit_cost, um_rate, plant_loc_cd, inv_stock_reference, stock_type, qty_on_hand, qty_shipped, cancel_dt, flag_active, crt_dt, updt_dt)
VALUES
('TXN005', 'LOC005', -100.0, -90.0, 0, 'ITEM005', -10.0, 1.0, 'PLANT005', 'REF005', 'STOCK005', -100.0, -10.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN006', 'LOC006', 100.0, 90.0, 0, 'ITEM006', 10.0, 1.0, 'PLANT006', 'REF006', 'STOCK006', 100.0, 10.0, 0, 'INVALID', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000');

-- NULL handling scenarios
INSERT INTO purgo_playground.f_inv_movmnt (txn_id, inv_loc, financial_qty, net_qty, expired_qt, item_nbr, unit_cost, um_rate, plant_loc_cd, inv_stock_reference, stock_type, qty_on_hand, qty_shipped, cancel_dt, flag_active, crt_dt, updt_dt)
VALUES
('TXN007', NULL, 100.0, 90.0, 0, 'ITEM007', 10.0, 1.0, 'PLANT007', 'REF007', 'STOCK007', 100.0, 10.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN008', 'LOC008', NULL, 90.0, 0, 'ITEM008', 10.0, 1.0, 'PLANT008', 'REF008', 'STOCK008', 100.0, 10.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000');

-- Special characters and multi-byte characters
INSERT INTO purgo_playground.f_inv_movmnt (txn_id, inv_loc, financial_qty, net_qty, expired_qt, item_nbr, unit_cost, um_rate, plant_loc_cd, inv_stock_reference, stock_type, qty_on_hand, qty_shipped, cancel_dt, flag_active, crt_dt, updt_dt)
VALUES
('TXN009', 'LOC009', 100.0, 90.0, 0, 'ITEM009', 10.0, 1.0, 'PLANT009', 'REF009', 'STOCK009', 100.0, 10.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN010', 'LOC010', 200.0, 180.0, 0, 'ITEM010', 20.0, 1.0, 'PLANT010', 'REF010', 'STOCK010', 200.0, 20.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN011', 'LOC011', 300.0, 270.0, 0, 'ITEM011', 30.0, 1.0, 'PLANT011', 'REF011', 'STOCK011', 300.0, 30.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN012', 'LOC012', 400.0, 360.0, 0, 'ITEM012', 40.0, 1.0, 'PLANT012', 'REF012', 'STOCK012', 400.0, 40.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN013', 'LOC013', 500.0, 450.0, 0, 'ITEM013', 50.0, 1.0, 'PLANT013', 'REF013', 'STOCK013', 500.0, 50.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN014', 'LOC014', 600.0, 540.0, 0, 'ITEM014', 60.0, 1.0, 'PLANT014', 'REF014', 'STOCK014', 600.0, 60.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN015', 'LOC015', 700.0, 630.0, 0, 'ITEM015', 70.0, 1.0, 'PLANT015', 'REF015', 'STOCK015', 700.0, 70.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN016', 'LOC016', 800.0, 720.0, 0, 'ITEM016', 80.0, 1.0, 'PLANT016', 'REF016', 'STOCK016', 800.0, 80.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN017', 'LOC017', 900.0, 810.0, 0, 'ITEM017', 90.0, 1.0, 'PLANT017', 'REF017', 'STOCK017', 900.0, 90.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN018', 'LOC018', 1000.0, 900.0, 0, 'ITEM018', 100.0, 1.0, 'PLANT018', 'REF018', 'STOCK018', 1000.0, 100.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN019', 'LOC019', 1100.0, 990.0, 0, 'ITEM019', 110.0, 1.0, 'PLANT019', 'REF019', 'STOCK019', 1100.0, 110.0, 0, 'Y', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000'),
('TXN020', 'LOC020', 1200.0, 1080.0, 0, 'ITEM020', 120.0, 1.0, 'PLANT020', 'REF020', 'STOCK020', 1200.0, 120.0, 0, 'N', '2024-03-21T00:00:00.000+0000', '2024-03-21T00:00:00.000+0000');
