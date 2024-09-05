
CREATE TABLE tickit.venue (
	venueid SMALLINT NOT NULL PRIMARY KEY, 
	venuename STRING, 
	venuecity STRING, 
	venuestate STRING, 
	venueseats INT
) USING DELTA;
