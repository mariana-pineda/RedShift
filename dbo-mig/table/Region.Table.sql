
CREATE TABLE Region (
	RegionID INT NOT NULL, 
	RegionDescription STRING NOT NULL 
)
USING delta
OPTIONS ('primaryKey'='RegionID')
