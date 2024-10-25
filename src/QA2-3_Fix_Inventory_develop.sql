ALTER TABLE qa.employees
ADD COLUMN lastdate DATE DEFAULT CURRENT_DATE;

ALTER TABLE qa.customers
ADD COLUMN categoryGroup VARCHAR DEFAULT 'Uncategorized';

CREATE OR REPLACE FUNCTION validate_categorygroup() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.categoryGroup NOT IN ('VIP', 'Regular', 'New', 'Uncategorized') THEN
        RAISE EXCEPTION 'Invalid categoryGroup %', NEW.categoryGroup;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS validate_categorygroup_trigger ON qa.customers;

CREATE TRIGGER validate_categorygroup_trigger
BEFORE INSERT OR UPDATE ON qa.customers
FOR EACH ROW EXECUTE FUNCTION validate_categorygroup();
