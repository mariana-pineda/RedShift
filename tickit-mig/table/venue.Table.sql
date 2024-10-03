
CREATE TABLE tickit.venue (
    venueid SMALLINT NOT NULL, 
    venuename STRING, 
    venuecity STRING, 
    venuestate CHAR(2), 
    venueseats INT
) USING DELTA
TBLPROPERTIES ('delta.autoOptimize.optimizeWrite' = 'true', 'delta.autoOptimize.autoCompact' = 'true');
