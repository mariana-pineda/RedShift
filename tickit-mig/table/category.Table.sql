
CREATE TABLE tickit.category (
	catid SMALLINT NOT NULL,
	catgroup STRING,
	catname STRING,
	catdesc STRING
) USING DELTA
OPTIONS (
	diststyle 'key', 
	distkey 'catid', 
	sortkey 'catid'
)
