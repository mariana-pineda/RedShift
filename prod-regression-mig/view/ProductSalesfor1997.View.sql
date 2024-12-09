
CREATE OR REPLACE VIEW `Product Sales for 1997` AS
SELECT 
  Cateries.CateryName, 
  Products.ProductName, 
  SUM(CAST(Order_Details.UnitPrice * Quantity * (1 - Discount) AS DECIMAL(19,4))) AS ProductSales
FROM 
  Cateries 
  INNER JOIN Products ON Cateries.CateryID = Products.CateryID
  INNER JOIN Orders ON Orders.OrderID = Order_Details.OrderID
  INNER JOIN Order_Details ON Products.ProductID = Order_Details.ProductID
WHERE 
  Orders.ShippedDate BETWEEN '1997-01-01' AND '1997-12-31'
GROUP BY 
  Cateries.CateryName, 
  Products.ProductName

