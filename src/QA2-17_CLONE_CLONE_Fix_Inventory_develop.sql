-- Add lastdate column to employees table
ALTER TABLE dbo.Employees
ADD lastdate DATE DEFAULT GETDATE();

-- Update existing records in employees table to set default value for lastdate
UPDATE dbo.Employees
SET lastdate = GETDATE()
WHERE lastdate IS NULL;

-- Add categoryGroup column to customers table
ALTER TABLE dbo.Customers
ADD categoryGroup NVARCHAR(20) DEFAULT 'Uncategorized';

-- Add CHECK constraint to ensure categoryGroup contains valid categories
ALTER TABLE dbo.Customers
ADD CONSTRAINT chk_categoryGroup CHECK (categoryGroup IN ('VIP', 'Regular', 'New', 'Uncategorized'));

-- Update existing records in customers table to set default value for categoryGroup
UPDATE dbo.Customers
SET categoryGroup = 'Uncategorized'
WHERE categoryGroup IS NULL;
