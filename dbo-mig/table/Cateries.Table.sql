
CREATE TABLE Cateries (
    CateryID INT NOT NULL GENERATED ALWAYS AS IDENTITY,
    CateryName STRING NOT NULL,
    Description STRING NULL,
    Picture BINARY NULL
);