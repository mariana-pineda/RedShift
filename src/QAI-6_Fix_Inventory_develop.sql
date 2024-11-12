-- SQL code to alter the employees and customers tables

-- Add lastdate column to qa.employees table
ALTER TABLE qa.employees
ADD COLUMN lastdate TIMESTAMP NULL;

-- Add categoryGroup column to qa.customers table
ALTER TABLE qa.customers
ADD COLUMN categoryGroup VARCHAR(255) NULL;
