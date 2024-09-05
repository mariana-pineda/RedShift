CREATE TABLE tickit.event (
    eventid INT NOT NULL, 
    venueid SMALLINT NOT NULL, 
    catid SMALLINT NOT NULL, 
    dateid SMALLINT NOT NULL, 
    eventname STRING, 
    starttime TIMESTAMP
) USING DELTA
LOCATION '/mnt/delta/tickit/event'

CREATE TABLE tickit.event
USING DELTA
TBLPROPERTIES ("delta.autoOptimize.optimizeWrite" = "true", "delta.autoOptimize.autoCompact" = "true")
AS SELECT *
FROM tickit.event