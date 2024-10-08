
CREATE TABLE tickit.date (
  dateid SMALLINT NOT NULL, 
  caldate DATE NOT NULL, 
  day STRING(3) NOT NULL, 
  week SMALLINT NOT NULL, 
  month STRING(5) NOT NULL, 
  qtr STRING(5) NOT NULL, 
  year SMALLINT NOT NULL, 
  holiday BOOLEAN DEFAULT false
) USING DELTA
LOCATION '/mnt/tickit/date/'
