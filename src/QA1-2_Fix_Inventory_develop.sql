-- SQL script to update the database schema according to the user story

-- Add "lastdate" column to "employees" table
ALTER TABLE qa.employees
ADD COLUMN lastdate DATE DEFAULT CURRENT_DATE;

-- Add "categoryGroup" column to "customers" table
ALTER TABLE qa.customers
ADD COLUMN categoryGroup VARCHAR(50);

