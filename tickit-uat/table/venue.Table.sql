
CREATE TABLE tickit.venue (
	venueid SMALLINT,
	venuename STRING,
	venuecity STRING,
	venuestate STRING,
	venueseats INT,
	PRIMARY KEY (venueid)
) USING DELTA;
