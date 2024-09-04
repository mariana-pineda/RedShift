
CREATE VIEW Invoices AS
SELECT Orders.ShipName, Orders.ShipAddress, Orders.ShipCity, Orders.ShipRegion, Orders.ShipPostalCode, 
       Orders.ShipCountry, Orders.CustomerID, Customers.CompanyName AS CustomerName, Customers.Address, Customers.City, 
       Customers.Region, Customers.PostalCode, Customers.Country, 
       CONCAT(Employees.FirstName, ' ', Employees.LastName) AS Salesperson, 
       Orders.OrderID, Orders.OrderDate, Orders.RequiredDate, Orders.ShippedDate, Shippers.CompanyName AS ShipperName, 
       OrderDetails.ProductID, Products.ProductName, OrderDetails.UnitPrice, OrderDetails.Quantity, 
       OrderDetails.Discount, 
       (CAST((OrderDetails.UnitPrice * OrderDetails.Quantity * (1 - OrderDetails.Discount)) AS DECIMAL(18, 2))) AS ExtendedPrice, Orders.Freight
FROM Shippers 
INNER JOIN Orders ON Shippers.ShipperID = Orders.ShipVia
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID;

