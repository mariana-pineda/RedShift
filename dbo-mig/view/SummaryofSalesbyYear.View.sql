
CREATE VIEW `Summary of Sales by Year` AS
SELECT Orders.ShippedDate, Orders.OrderID, `Order Subtotals`.Subtotal
FROM Orders INNER JOIN `Order Subtotals` ON Orders.OrderID = `Order Subtotals`.OrderID
WHERE Orders.ShippedDate IS NOT NULL

