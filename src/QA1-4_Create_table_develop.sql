-- SQL script to update the database schema

-- Add lastdate column to Employees table
ALTER TABLE Employees
ADD COLUMN lastdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Add categoryGroup column to Customers table
ALTER TABLE Customers
ADD COLUMN categoryGroup VARCHAR(255);

-- Assuming a check constraint for predefined categories
ALTER TABLE Customers
ADD CONSTRAINT chk_categoryGroup CHECK (categoryGroup IN ('Retail', 'Wholesale', 'Online', 'Corporate'));
