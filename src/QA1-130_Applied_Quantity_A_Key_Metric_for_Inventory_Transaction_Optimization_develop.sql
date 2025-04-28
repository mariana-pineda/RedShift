-- SQL Implementation for Calculating Applied Quantity (apl_qty) in Databricks Environment

/*
  Assume tables exist in Unity Catalog: purgo_databricks, Schema: purgo_playground
  Tables: f_inv_movmnt_apl_qty, f_inv_movmnt_apl_qty_test, f_inv_movmnt_apl_qty_result
*/

-- Calculate apl_qty based on conditions provided

WITH calculated_apl_qty AS (
  SELECT txn_id, ref_txn_qty, cumulative_txn_qty, cumulative_ref_ord_sched_qty, ref_ord_sched_qty,
         prior_cumulative_txn_qty, prior_cumulative_ref_ord_sched_qty,
         CASE
           /* Condition 1 */
           WHEN ref_txn_qty > 0 
                AND cumulative_txn_qty >= cumulative_ref_ord_sched_qty 
                AND prior_cumulative_txn_qty > prior_cumulative_ref_ord_sched_qty THEN 
             (ref_ord_sched_qty - (prior_cumulative_txn_qty - prior_cumulative_ref_ord_sched_qty))

           /* Condition 2 */
           WHEN ref_txn_qty > 0 
                AND cumulative_ref_ord_sched_qty >= cumulative_txn_qty 
                AND prior_cumulative_ref_ord_sched_qty > prior_cumulative_txn_qty THEN 
             (ref_txn_qty - (prior_cumulative_ref_ord_sched_qty - prior_cumulative_txn_qty))

           /* Condition 3 */
           WHEN ref_txn_qty < 0 
                AND cumulative_txn_qty != 0 
                AND cumulative_ref_ord_sched_qty > 0 THEN 
             ref_txn_qty

           /* Default Condition: Null apl_qty */
           ELSE NULL
         END AS apl_qty
  FROM purgo_playground.f_inv_movmnt_apl_qty
)

/*
  Selecting final calculated data
*/

SELECT * FROM calculated_apl_qty;

/*
  Validate Correctness and Coverage of Applied Quantity Logic
  Using Logical Constructs and Performance Optimization Techniques
*/

-- Ensure schema consistency
DESCRIBE TABLE purgo_playground.f_inv_movmnt_apl_qty;

/*
  Data Quality Check: Ensure no null apl_qty for specific ref_txn_qty conditions
*/

SELECT COUNT(*) AS null_count
FROM purgo_playground.f_inv_movmnt_apl_qty
WHERE apl_qty IS NULL
  AND (ref_txn_qty > 0 OR ref_txn_qty < 0);
