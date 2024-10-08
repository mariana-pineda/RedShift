
CREATE TABLE tickit.venue (
    venueid SMALLINT NOT NULL, 
    venuename STRING, 
    venuecity STRING, 
    venuestate STRING, 
    venueseats INT
) 
USING DELTA 
TBLPROPERTIES ('delta.autoOptimize.optimizeWrite' = 'true', 'delta.autoOptimize.autoCompact' = 'true')
