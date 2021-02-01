"""
Name: Minxi Long
URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-minxilong
"""


# TODO: Create your Movie class in this file


class Movie:
    """Represent a Movie Object"""

    def __init__(self, title='', year=0, category='', is_watched=False):
        """Initialise the movies' name, year, category and whether watched"""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return details of movie object"""
        if self.is_watched:
            return '{} - {} ({}) is watched'.format(self.title, self.year, self.category)
        else:
            return '{} - {} ({}) have not watched'.format(self.title, self.year, self.category)

    def unwatched_watched(self):
        """Add unwatched movies to watched"""
        self.is_watched = True

    def watched_unwatched(self):
        """Add watched movies to unwatched"""
        self.is_watched = False

    pass
