-- SQL logic to populate f_inv_movmnt table based on field mappings from the provided Excel file

-- Assuming following tables and columns based on typical inventory transaction scenario
-- source_table_1 (SrcID, SrcSKU, SrcTransactionType, SrcQuantity, SrcTransactionDate, SrcSupplierID)
-- source_table_2 (SrcID, SrcDiscrepancyFlag)

INSERT INTO f_inv_movmnt (SKU, TransactionType, Quantity, TransactionDate, SupplierID, DiscrepancyFlag)
SELECT
    st1.SrcSKU AS SKU,
    st1.SrcTransactionType AS TransactionType,
    st1.SrcQuantity AS Quantity,
    st1.SrcTransactionDate AS TransactionDate,
    st1.SrcSupplierID AS SupplierID,
    COALESCE(st2.SrcDiscrepancyFlag, FALSE) AS DiscrepancyFlag
FROM
    source_table_1 st1
LEFT JOIN
    source_table_2 st2 ON st1.SrcID = st2.SrcID
WHERE
    st1.SrcQuantity >= 0  -- Assuming only non-negative quantities are valid for this insert
    AND NOT EXISTS (
        SELECT 1 FROM f_inv_movmnt fm WHERE fm.SKU = st1.SrcSKU AND fm.TransactionDate = st1.SrcTransactionDate
    );

-- This logic assumes:
-- - The source fields and target fields structure as described in the introduction.
-- - Basic data discrepancies handling through LEFT JOIN and COALESCE.
-- - Ensuring non-existing records in the target by checking with EXISTS condition.
-- - Filtering inappropriate data if applicable (e.g., negative quantities).
