
CREATE TABLE tickit.category (
  catid SMALLINT NOT NULL, 
  catgroup STRING, 
  catname STRING, 
  catdesc STRING 
) 
USING DELTA
TBLPROPERTIES ('delta.autoOptimize.optimizeWrite' = 'true')

