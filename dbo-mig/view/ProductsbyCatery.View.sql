
CREATE VIEW `Products by Catery` AS
SELECT 
  c.CateryName, 
  p.ProductName, 
  p.QuantityPerUnit, 
  p.UnitsInStock, 
  p.Discontinued
FROM 
  Cateries c 
INNER JOIN 
  Products p 
ON 
  c.CateryID = p.CateryID
WHERE 
  p.Discontinued <> 1

