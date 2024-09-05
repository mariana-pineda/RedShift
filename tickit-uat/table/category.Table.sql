
CREATE TABLE tickit.category (
    catid SMALLINT NOT NULL, 
    catgroup STRING, 
    catname STRING, 
    catdesc STRING,
    PRIMARY KEY (catid)
) USING DELTA
PARTITIONED BY (catid)
