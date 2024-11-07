-- SQL code to add columns to the respective tables

-- Add "lastdate" column to "employees" table
ALTER TABLE qa.employees
ADD COLUMN lastdate TIMESTAMP;

-- Add "categoryGroup" column to "customers" table
ALTER TABLE qa.customers
ADD COLUMN categoryGroup VARCHAR(255);
