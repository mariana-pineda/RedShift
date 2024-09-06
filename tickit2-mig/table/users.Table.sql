
CREATE TABLE tickit.users (
  userid INT NOT NULL, 
  username CHAR(8), 
  firstname STRING, 
  lastname STRING, 
  city STRING, 
  state CHAR(2), 
  email STRING, 
  phone CHAR(14), 
  likesports BOOLEAN, 
  liketheatre BOOLEAN, 
  likeconcerts BOOLEAN, 
  likejazz BOOLEAN, 
  likeclassical BOOLEAN, 
  likeopera BOOLEAN, 
  likerock BOOLEAN, 
  likevegas BOOLEAN, 
  likebroadway BOOLEAN, 
  likemusicals BOOLEAN,
  PRIMARY KEY (userid)
) 
USING DELTA
PARTITIONED BY (userid)
