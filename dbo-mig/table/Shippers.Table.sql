
CREATE TABLE Shippers (
    ShipperID INT NOT NULL,
    CompanyName STRING NOT NULL, 
    Phone STRING 
)
USING DELTA;

ALTER TABLE Shippers
ALTER COLUMN ShipperID SET NOT NULL;

ALTER TABLE Shippers 
ADD CONSTRAINT PK_Shippers PRIMARY KEY (ShipperID);

CREATE SEQUENCE Shippers_ShipperID_seq START 1;

CREATE OR REPLACE TRIGGER Shippers_ShipperID_trigger 
BEFORE INSERT ON Shippers 
FOR EACH ROW 
SET new.ShipperID = nextval('Shippers_ShipperID_seq');
