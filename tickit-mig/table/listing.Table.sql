
CREATE TABLE tickit.listing (
    listid INT NOT NULL, 
    sellerid INT NOT NULL, 
    eventid INT NOT NULL, 
    dateid SMALLINT NOT NULL, 
    numtickets SMALLINT NOT NULL, 
    priceperticket DECIMAL(8, 2), 
    totalprice DECIMAL(8, 2), 
    listtime TIMESTAMP
) 
USING DELTA
OPTIONS (
    PRIMARY KEY (listid)
)

