
CREATE TABLE tickit.event (
	eventid INT NOT NULL, 
	venueid SMALLINT NOT NULL, 
	catid SMALLINT NOT NULL, 
	dateid SMALLINT NOT NULL, 
	eventname STRING, 
	starttime TIMESTAMP
) USING DELTA

