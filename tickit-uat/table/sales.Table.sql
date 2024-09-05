
CREATE TABLE tickit.sales (
	salesid INTEGER NOT NULL, 
	listid INTEGER NOT NULL, 
	sellerid INTEGER NOT NULL, 
	buyerid INTEGER NOT NULL, 
	eventid INTEGER NOT NULL, 
	dateid SMALLINT NOT NULL, 
	qtysold SMALLINT NOT NULL, 
	pricepaid DECIMAL(8, 2), 
	commission DECIMAL(8, 2), 
	saletime TIMESTAMP
) USING DELTA
PARTITIONED BY (listid)

