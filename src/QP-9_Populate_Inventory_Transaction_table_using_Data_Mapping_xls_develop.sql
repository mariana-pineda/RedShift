-- SQL logic to populate the Inventory Transaction table (f_inv_movmnt)

-- Assuming the field mappings are provided and the source tables are accessible
-- The following SQL script is a generic template and should be adjusted based on actual field mappings

INSERT INTO f_inv_movmnt (
    transaction_id,
    item_id,
    quantity,
    transaction_type,
    transaction_date,
    supplier_id,
    warehouse_id,
    unit_price,
    total_value,
    status
)
SELECT
    src.transaction_id,
    src.item_id,
    src.quantity,
    src.transaction_type,
    src.transaction_date,
    src.supplier_id,
    src.warehouse_id,
    src.unit_price,
    src.quantity * src.unit_price AS total_value,
    src.status
FROM (
    SELECT
        -- Assuming source tables and fields are known
        -- Replace 'source_table' and field names with actual source table and field names
        st.transaction_id,
        st.item_id,
        st.quantity,
        st.transaction_type,
        st.transaction_date,
        st.supplier_id,
        st.warehouse_id,
        st.unit_price,
        st.status
    FROM source_table st
    -- Add necessary joins and conditions based on field mappings
) src
-- Handle data type discrepancies if necessary
-- Ensure data type compatibility between source and target
-- Add error handling and logging if required
-- Validate data transformation and loading process
-- Define a schedule for executing the logic if needed
;
