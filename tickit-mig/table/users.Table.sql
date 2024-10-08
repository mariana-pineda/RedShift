
CREATE TABLE tickit.users (
    userid INT NOT NULL, 
    username STRING, 
    firstname STRING, 
    lastname STRING, 
    city STRING, 
    state STRING, 
    email STRING, 
    phone STRING, 
    likesports BOOLEAN, 
    liketheatre BOOLEAN, 
    likeconcerts BOOLEAN, 
    likejazz BOOLEAN, 
    likeclassical BOOLEAN, 
    likeopera BOOLEAN, 
    likerock BOOLEAN, 
    likevegas BOOLEAN, 
    likebroadway BOOLEAN, 
    likemusicals BOOLEAN
) USING DELTA
CLUSTERED BY (userid) INTO 8 BUCKETS
