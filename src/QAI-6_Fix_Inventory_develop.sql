-- SQL to add new columns to the tables

-- Add lastdate column to employees table
ALTER TABLE qa.employees
ADD COLUMN lastdate TIMESTAMP NULL;

-- Add categoryGroup column to customers table
ALTER TABLE qa.customers
ADD COLUMN categoryGroup VARCHAR NULL;
