CREATE TABLE tickit.venue (
	venueid SMALLINT NOT NULL, 
	venuename VARCHAR(100), 
	venuecity VARCHAR(30), 
	venuestate CHAR(2), 
	venueseats INTEGER
) USING DELTA
PRIMARY KEY (venueid);