
CREATE VIEW `Products Above Average Price` AS
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products)
-- Uncomment the line below if you want to order by UnitPrice descending
-- ORDER BY UnitPrice DESC
