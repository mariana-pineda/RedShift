-- Modify Employees Table to add lastdate column
ALTER TABLE dbo.[Employees]
ADD [lastdate] DATE DEFAULT GETDATE() NOT NULL;

-- Update existing records to set lastdate to the current date
UPDATE dbo.[Employees]
SET [lastdate] = GETDATE();

-- Modify Customers Table to add categoryGroup column
ALTER TABLE dbo.[Customers]
ADD [categoryGroup] NVARCHAR(20) DEFAULT 'Uncategorized' NOT NULL;

-- Update existing records to set categoryGroup to "Uncategorized"
UPDATE dbo.[Customers]
SET [categoryGroup] = 'Uncategorized';

-- Add check constraint to ensure categoryGroup contains valid values
ALTER TABLE dbo.[Customers]
ADD CONSTRAINT CHK_Customers_CategoryGroup CHECK ([categoryGroup] IN ('VIP', 'Regular', 'New', 'Uncategorized'));
