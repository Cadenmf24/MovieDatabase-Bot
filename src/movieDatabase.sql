

CREATE TABLE movies(
    id  SERIAL PRIMARY KEY NOT NULL,
    movieName TEXT NOT NULL,
    releaseDate TIMESTAMP, 
);

INSERT INTO movies(movieName, releaseDate) VALUES
('The Untold Truth', '2023-01-01');

