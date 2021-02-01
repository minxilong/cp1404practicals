"""
Name: Minxi Long
URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-minxilong
"""
# TODO: Create your MovieCollection class in this file

import csv
from movie import Movie


class MovieCollection(Movie):
    """Get a list of Movie objects"""

    def __init__(self):
        """Initialise the list"""
        super().__init__()
        self.movies = []

    def __str__(self):
        mstrs = []
        for movie in self.movies:
            mstrs.append(str(movie))
        return '\n'.join(mstrs)

    def add_movie(self, movie):
        """Add a single Movie object to the movies attribute"""
        self.movies.append(movie)

    def count_watched_movies(self):
        """Get number of watched movies"""
        count_watched = 0
        for movie in self.movies:
            if movie.is_watched == 'w':
                count_watched += 1
        return count_watched

    def count_unwatched_movies(self):
        """Get number of unwatched movies"""
        count_unwatched = 0
        for movie in self.movies:
            if movie.is_watched == 'u':
                count_unwatched += 1
        return count_unwatched

    def load_movies(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                title, year, category, is_watched = line
                title = title
                year = int(year)
                category = category
                is_watched == 'w'
                movie = Movie(title, year, category, is_watched)
                self.movies.append(movie)

    def save_movies(self, filename):
        with open(filename, 'w') as out_file:
            for movie in self.movies:
                if movie.is_watched:
                    is_watched = 'w'
                else:
                    is_watched = 'u'
                out_file.write('{}, {}, {}, {}\n'.format(movie.title, movie.year, movie.category, is_watched))

    def by_key(self, key, movie):
        """Sort by the key passed in"""
        key = key.lower()
        if key == 'title':
            return movie.title
        elif key == 'year':
            return movie.year
        elif key == 'category':
            return movie.category
        elif key == 'watched':
            return movie.is_watched

    def sort(self, key):
        self.movies.sort(key=lambda movie: (self.by_key(key, movie), movie.title))

    pass
