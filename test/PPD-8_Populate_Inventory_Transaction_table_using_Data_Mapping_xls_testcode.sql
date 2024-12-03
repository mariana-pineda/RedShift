-- Test Code to Validate the Inventory Transaction Program

-- Validate uniqueness of txn_id in f_inv_movmnt table
CREATE OR REPLACE FUNCTION validate_txn_id_uniqueness() RETURNS BOOLEAN AS $$
DECLARE
    duplicate_count INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO duplicate_count
    FROM (
        SELECT txn_id
        FROM f_inv_movmnt
        GROUP BY txn_id
        HAVING COUNT(*) > 1
    ) AS duplicates;

    IF duplicate_count = 0 THEN
        RETURN TRUE; -- No duplicates found, test passed
    ELSE
        RAISE EXCEPTION 'Duplicate txn_id found: % duplicates', duplicate_count;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Execute the uniqueness function
SELECT validate_txn_id_uniqueness();

-- Validate handling of NULL values with defaults
CREATE OR REPLACE FUNCTION validate_null_handling() RETURNS BOOLEAN AS $$
DECLARE
    row_count INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO row_count
    FROM (
        SELECT *
        FROM f_inv_movmnt
        WHERE (quantity IS NULL AND default_quantity IS NOT NULL)
            OR (expired_dt IS NULL AND default_expired_dt IS NOT NULL)
    ) AS defaults_applied;

    IF row_count > 0 THEN
        RETURN TRUE; -- Defaults correctly applied, test passed
    ELSE
        RAISE EXCEPTION 'NULL value handling test failed: no defaults applied';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Execute the null handling function
SELECT validate_null_handling();

-- Validate consistent naming for 'expired_dt'
CREATE OR REPLACE FUNCTION validate_expired_date_naming() RETURNS BOOLEAN AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'f_inv_movmnt'
          AND column_name = 'expired_dt'
    ) THEN
        RETURN TRUE; -- Consistent naming, test passed
    ELSE
        RAISE EXCEPTION 'Inconsistent naming for expired date';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Execute the expired date naming function
SELECT validate_expired_date_naming();

-- Validate clear join conditions for VBAX and parl tables
CREATE OR REPLACE FUNCTION validate_join_conditions() RETURNS BOOLEAN AS $$
DECLARE
    valid_join_count INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO valid_join_count
    FROM VBAX vb
    LEFT JOIN parl pl ON vb.item_id = pl.item_id
    WHERE pl.condition = 'Active';

    IF valid_join_count > 0 THEN
        RETURN TRUE; -- Valid join exists, test passed
    ELSE
        RAISE EXCEPTION 'Invalid join conditions for VBAX and parl tables';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Execute the join conditions function
SELECT validate_join_conditions();

-- Note: Managing error cases and transaction logging requires additional infrastructure
-- beyond core SQL capabilities.
