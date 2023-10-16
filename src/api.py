
from utility import exec_sql_file, exec_commit


def addMovie(movie,release):

    result = exec_commit('INSERT INTO movies(movieName, releaseDate) VALUES (%s , %s)', (movie, release))

    return result

def deleteMovie(movieName):

    result = exec_commit('DELETE FROM movies WHERE movieName = %s', (movieName))

    return result


def main():
    exec_sql_file('movieDatabase.sql')


if __name__ == "__main__":
    main()