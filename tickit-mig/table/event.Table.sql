
CREATE TABLE tickit.event (
    eventid INT NOT NULL PRIMARY KEY, 
    venueid SMALLINT NOT NULL, 
    catid SMALLINT NOT NULL, 
    dateid SMALLINT NOT NULL, 
    eventname STRING, 
    starttime TIMESTAMP
) USING DELTA
CLUSTERED BY (eventid) SORT BY (dateid)

