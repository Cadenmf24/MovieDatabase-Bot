DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS movieRatings;

CREATE TABLE movies(
    id  SERIAL PRIMARY KEY NOT NULL,
    movieName TEXT NOT NULL,
    releaseDate TIMESTAMP
);

CREATE TABLE movieRatings(
    movieId INT NOT NULL,
    revieweeName TEXT NOT NULL,
    rating INT NOT NULL
);

INSERT INTO movies(movieName, releaseDate) VALUES
('The Untold Truth', '2023-01-01');

INSERT INTO movieRatings(movieId, revieweeName, rating) VALUES
(1, 'Ash', 5);


