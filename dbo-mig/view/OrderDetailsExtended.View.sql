
CREATE VIEW `Order Details Extended` AS
SELECT `Order Details`.OrderID,
       `Order Details`.ProductID,
       Products.ProductName,
       `Order Details`.UnitPrice,
       `Order Details`.Quantity,
       `Order Details`.Discount,
       (CAST((`Order Details`.UnitPrice * Quantity * (1 - Discount) / 100) AS DECIMAL(19, 4)) * 100) AS ExtendedPrice
FROM Products
INNER JOIN `Order Details` ON Products.ProductID = `Order Details`.ProductID
