
CREATE TABLE Region (
  RegionID INT NOT NULL,
  RegionDescription STRING NOT NULL 
)
USING DELTA
TBLPROPERTIES ('delta.columnMapping.mode' = 'name')
COMMENT 'Table for storing region data';

ALTER TABLE Region
ADD CONSTRAINT PK_Region PRIMARY KEY (RegionID);
