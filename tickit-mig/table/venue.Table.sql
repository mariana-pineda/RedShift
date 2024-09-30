
CREATE TABLE tickit.venue (
    venueid SMALLINT NOT NULL, 
    venuename STRING, 
    venuecity STRING, 
    venuestate STRING, 
    venueseats INT
);

ALTER TABLE tickit.venue
ADD CONSTRAINT pk_venue PRIMARY KEY (venueid);
