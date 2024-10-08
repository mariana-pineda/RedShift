
CREATE TABLE tickit.date (
    dateid SMALLINT NOT NULL, 
    caldate DATE NOT NULL, 
    day STRING NOT NULL, 
    week SMALLINT NOT NULL, 
    month STRING NOT NULL, 
    qtr STRING NOT NULL, 
    year SMALLINT NOT NULL, 
    holiday BOOLEAN DEFAULT false
);
