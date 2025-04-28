-- SQL Test Code for Databricks Environment

/* 
  Setup and Configurations 
  Assume the tables purgo_playground.f_inv_movmnt_apl_qty, purgo_playground.f_inv_movmnt_apl_qty_test, 
  and purgo_playground.f_inv_movmnt_apl_qty_result already exist with the appropriate schema.
*/

-- Unit Test for Condition 1
SELECT txn_id, ref_txn_qty, cumulative_txn_qty, cumulative_ref_ord_sched_qty, ref_ord_sched_qty,
       prior_cumulative_txn_qty, prior_cumulative_ref_ord_sched_qty,
       CASE 
         WHEN ref_txn_qty > 0 
              AND cumulative_txn_qty >= cumulative_ref_ord_sched_qty 
              AND prior_cumulative_txn_qty > prior_cumulative_ref_ord_sched_qty THEN 
           (ref_ord_sched_qty - (prior_cumulative_txn_qty - prior_cumulative_ref_ord_sched_qty))
         ELSE ref_ord_sched_qty 
       END AS expected_apl_qty
FROM purgo_playground.f_inv_movmnt_apl_qty_test
WHERE txn_id = '1';

-- Integration Test for all Conditions
WITH calculated_data AS (
  SELECT txn_id, ref_txn_qty, cumulative_txn_qty, cumulative_ref_ord_sched_qty, ref_ord_sched_qty,
         prior_cumulative_txn_qty, prior_cumulative_ref_ord_sched_qty,
         CASE
           WHEN ref_txn_qty > 0 
                AND cumulative_txn_qty >= cumulative_ref_ord_sched_qty
                AND prior_cumulative_txn_qty > prior_cumulative_ref_ord_sched_qty THEN 
             (ref_ord_sched_qty - (prior_cumulative_txn_qty - prior_cumulative_ref_ord_sched_qty))
           WHEN ref_txn_qty > 0 
                AND cumulative_ref_ord_sched_qty >= cumulative_txn_qty 
                AND prior_cumulative_ref_ord_sched_qty > prior_cumulative_txn_qty THEN 
             (ref_txn_qty - (prior_cumulative_ref_ord_sched_qty - prior_cumulative_txn_qty))
           WHEN ref_txn_qty < 0 
                AND cumulative_txn_qty != 0 
                AND cumulative_ref_ord_sched_qty > 0 THEN 
             ref_txn_qty
           ELSE NULL
         END AS apl_qty
    FROM purgo_playground.f_inv_movmnt_apl_qty
)
SELECT * FROM calculated_data;

-- Performance Test: Analyze and optimize SQL execution plan
EXPLAIN
SELECT txn_id, COUNT(*) AS record_count
FROM purgo_playground.f_inv_movmnt_apl_qty
GROUP BY txn_id;

-- Data Quality Validation Test
-- Check for NULL values where apl_qty should not be NULL
SELECT COUNT(*) AS null_count
FROM purgo_playground.f_inv_movmnt_apl_qty
WHERE apl_qty IS NULL
  AND (ref_txn_qty > 0 OR ref_txn_qty < 0);

-- Validation for Delta Lake Operations - MERGE Operation Test
MERGE INTO purgo_playground.f_inv_movmnt_apl_qty_result AS target
USING (SELECT * FROM purgo_playground.f_inv_movmnt_apl_qty_test) AS source
ON target.txn_id = source.txn_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN 
INSERT (txn_id, ref_txn_qty, cumulative_txn_qty, cumulative_ref_ord_sched_qty, 
        ref_ord_sched_qty, prior_cumulative_txn_qty, prior_cumulative_ref_ord_sched_qty, apl_qty)
VALUES (source.txn_id, source.ref_txn_qty, source.cumulative_txn_qty, source.cumulative_ref_ord_sched_qty, 
        source.ref_ord_sched_qty, source.prior_cumulative_txn_qty, source.prior_cumulative_ref_ord_sched_qty, source.apl_qty);

-- Clean-up Operations after Test
DELETE FROM purgo_playground.f_inv_movmnt_apl_qty_result WHERE txn_id IN ('1', '2', '3', '4');

-- Test Window Functions and Analytics Features
SELECT txn_id, ref_txn_qty, cumulative_txn_qty,
       ROW_NUMBER() OVER (PARTITION BY ref_ord_sched_qty ORDER BY cumulative_txn_qty DESC) AS rank
FROM purgo_playground.f_inv_movmnt_apl_qty_test;

/*
  Schema Validation Test 
  Ensure correct schema for purgo_playground.f_inv_movmnt_apl_qty
*/
DESCRIBE TABLE purgo_playground.f_inv_movmnt_apl_qty;

