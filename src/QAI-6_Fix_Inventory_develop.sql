-- SQL to add the 'lastdate' column to the 'qa.employees' table
ALTER TABLE qa.employees
ADD COLUMN lastdate TIMESTAMP NULL;

-- SQL to add the 'categoryGroup' column to the 'qa.customers' table
ALTER TABLE qa.customers
ADD COLUMN categoryGroup VARCHAR(255) NULL;
