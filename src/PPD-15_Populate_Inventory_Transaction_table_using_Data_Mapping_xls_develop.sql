-- SQL logic to populate the f_inv_movmnt table based on field mappings

INSERT INTO f_inv_movmnt (transaction_id, item_id, quantity, transaction_type, transaction_date, source_system, discrepancy_flag, error_logged, report_generated)
SELECT 
    src.transaction_id,
    src.item_id,
    src.quantity,
    src.transaction_type,
    src.transaction_date,
    src.source_system,
    CASE 
        WHEN src.source_system = 'Redshift' AND src.discrepancy_flag = TRUE THEN TRUE
        WHEN src.source_system = 'Databricks' AND src.discrepancy_flag = TRUE THEN TRUE
        ELSE FALSE
    END AS discrepancy_flag,
    CASE 
        WHEN src.error_logged = TRUE THEN TRUE
        ELSE FALSE
    END AS error_logged,
    CASE 
        WHEN src.report_generated = TRUE THEN TRUE
        ELSE FALSE
    END AS report_generated
FROM (
    SELECT 
        r.transaction_id,
        r.item_id,
        r.quantity,
        r.transaction_type,
        r.transaction_date,
        'Redshift' AS source_system,
        r.discrepancy_flag,
        r.error_logged,
        r.report_generated
    FROM redshift_source_table r
    UNION ALL
    SELECT 
        d.transaction_id,
        d.item_id,
        d.quantity,
        d.transaction_type,
        d.transaction_date,
        'Databricks' AS source_system,
        d.discrepancy_flag,
        d.error_logged,
        d.report_generated
    FROM databricks_source_table d
) src;

