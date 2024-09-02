CREATE TABLE tpcds.reason (
    r_reason_sk INT NOT NULL, 
    r_reason_id CHAR(16) NOT NULL, 
    r_reason_desc CHAR(100), 
    PRIMARY KEY (r_reason_sk)
) USING delta
DISTRIBUTE BY HASH (r_reason_sk)