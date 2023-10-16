DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS movieRatings;

CREATE TABLE movies(
    id  SERIAL PRIMARY KEY NOT NULL,
    movieName TEXT NOT NULL,
    releaseDate TIMESTAMP
);

CREATE TABLE movieRatings(
    id SERIAL PRIMARY Key NOT NULL,
    revieweeName TEXT NOT NULL,
    rating INT NOT NULL
);

INSERT INTO movies(movieName, releaseDate) VALUES
('The Untold Truth', '2023-01-01');

INSERT INTO movieRatings(id, revieweeName, rating) VALUES
(1, 'Ash', 5);


SELECT movieName, rating FROM movies INNER JOIN movieRatings ON movies.id = movieRatings.id