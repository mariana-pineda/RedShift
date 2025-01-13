-- SQL code to add lastdate to employees table
ALTER TABLE employees
ADD COLUMN lastdate DATE;

-- SQL code to add categoryGroup to customers table
ALTER TABLE customers
ADD COLUMN categoryGroup VARCHAR(255);
