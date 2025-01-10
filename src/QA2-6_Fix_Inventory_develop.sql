-- Add lastdate to employees table
ALTER TABLE dbo.Employees
ADD LastDate DATE DEFAULT GETDATE();

-- Update existing records with default lastdate
UPDATE dbo.Employees
SET LastDate = GETDATE()
WHERE LastDate IS NULL;

-- Add categoryGroup to customers table
ALTER TABLE dbo.Customers
ADD CategoryGroup NVARCHAR(20) DEFAULT 'Uncategorized';

-- Update existing records with default categoryGroup
UPDATE dbo.Customers
SET CategoryGroup = 'Uncategorized'
WHERE CategoryGroup IS NULL;

-- Add check constraint for categoryGroup
ALTER TABLE dbo.Customers
ADD CONSTRAINT CHK_CategoryGroup CHECK (CategoryGroup IN ('VIP', 'Regular', 'New', 'Uncategorized'));
