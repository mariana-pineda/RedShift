
CREATE TABLE Customers (
  CustomerID STRING(5) NOT NULL, 
  CompanyName STRING(40) NOT NULL, 
  ContactName STRING(30), 
  ContactTitle STRING(30), 
  Address STRING(60), 
  City STRING(15), 
  Region STRING(15), 
  PostalCode STRING(10), 
  Country STRING(15), 
  Phone STRING(24), 
  Fax STRING(24),
  PRIMARY KEY (CustomerID)
)
