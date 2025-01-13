-- Add lastdate column to employees table
ALTER TABLE dbo.Employees
ADD lastdate DATE DEFAULT GETDATE();

-- Update existing records to set default value for lastdate
UPDATE dbo.Employees
SET lastdate = GETDATE()
WHERE lastdate IS NULL;

-- Add categoryGroup column to customers table
ALTER TABLE dbo.Customers
ADD categoryGroup NVARCHAR(20) DEFAULT 'Uncategorized';

-- Update existing records to set default value for categoryGroup
UPDATE dbo.Customers
SET categoryGroup = 'Uncategorized'
WHERE categoryGroup IS NULL;

-- Add check constraint for categoryGroup to ensure valid categories
ALTER TABLE dbo.Customers
ADD CONSTRAINT chk_categoryGroup CHECK (categoryGroup IN ('VIP', 'Regular', 'New', 'Uncategorized'));
