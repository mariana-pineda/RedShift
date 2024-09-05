
CREATE TABLE tickit.sales (
    salesid INT NOT NULL, 
    listid INT NOT NULL, 
    sellerid INT NOT NULL, 
    buyerid INT NOT NULL, 
    eventid INT NOT NULL, 
    dateid SMALLINT NOT NULL, 
    qtysold SMALLINT NOT NULL, 
    pricepaid DECIMAL(8, 2), 
    commission DECIMAL(8, 2), 
    saletime TIMESTAMP
);
