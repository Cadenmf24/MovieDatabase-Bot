
from utility import exec_get_all, exec_sql_file, exec_commit, exec_get_one


def addMovie(movie,release):

    result = exec_commit('INSERT INTO movies(movieName, releaseDate) VALUES (%s , %s)', [movie, release])

    return result

def deleteMovie(movieName):

    result = exec_commit('DELETE FROM movies WHERE movieName = %s', [movieName])

    return result

def getMovieID(movieName):

    result = exec_get_one('SELECT movies.id FROM movies WHERE movieName = %s', [movieName])

    return result[0]

def rateMovie(movieName, rating, name):

    id = getMovieID(movieName)

    result = exec_commit('INSERT INTO movieRatings (movieId, revieweeName, rating) VALUES %s, %s, %s', [id, name, rating])

    return result

def getMovieRatingByMovie(movieName):

    id = getMovieID(movieName)

    result = exec_get_all('SELECT movieName, rating FROM movies INNER JOIN movieRatings ON movieRatings.movieId = %s', [id])

    return result

def getRaterRates(name):

    result = exec_get_all('SELECT revieweeName, movieName, rating From movieRatings INNER JOIN movies ON movieId = movies.id WHERE revieweeName = %s', [name])


def main():
    exec_sql_file('movieDatabase.sql')


if __name__ == "__main__":
    main()