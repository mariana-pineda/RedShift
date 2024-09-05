
CREATE TABLE tickit.event (
  eventid INTEGER NOT NULL, 
  venueid SMALLINT NOT NULL, 
  catid SMALLINT NOT NULL, 
  dateid SMALLINT NOT NULL, 
  eventname STRING, 
  starttime TIMESTAMP
) USING DELTA

-- Optional: If you need to create indexes, partitions, or other optimizations, you would include them here. 
-- Example of primary key constraint in Databricks:
ALTER TABLE tickit.event ADD CONSTRAINT event_pk PRIMARY KEY (eventid);
