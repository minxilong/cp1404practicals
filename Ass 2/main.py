"""
Name: Minxi Long
Date: 23/01/2021
Brief Project Description: Movie Program
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-minxilong
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection


class MoviesToWatchApp(App):
    """Main application to watch movies"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies("movies.csv")
        self.sorted_by = "year"

    def build(self):
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_movies(self.sorted_by)
        return self.root

    def movie_listed(self):
        self.root.ids.movies.clear_widgets()
        self.root.ids.top_label.text = 'To watch: {}. Watched: {}'.format(self.movie_collection.count_unwatched_movies,
                                                                          self.movie_collection.count_watched_movies)
        for movie in self.movies:
            button = Button(text=str(movie))
            button.bind(on_press=self.movie_click)
            button.movie = movie
            self.root.ids.movies.add_widget(button)
            if movie.is_watched:
                button.background_color = '#6e94b9'
            else:
                button.background_color = '#b26c6c'

    def movie_click(self, button):
        movie = button.movie
        if movie.is_watched:
            movie.watched_unwatched()
            self.root.ids.bottom_label.text = 'You have watched {}'.format(movie.title)
        else:
            movie.unwatched_watched()
            self.root.ids.bottom_label.text = 'You have unwatched {}'.format(movie.title)
        self.movie_listed()

    def sort_movies(self, sorted_by):
        self.sorted_by = sorted_by
        self.movie_collection.sort(sorted_by)
        self.movie_listed()

    def add_movie(self):
        movie = Movie(self.root.ids.title.text, int(self.root.ids.year.text), self.root.ids.category.text, False)
        self.movies.add_movie(movie)
        self.sort_movies(self.sorted_by)

    def clear(self):
        self.root.ids.title.text = ""
        self.root.ids.year.text = ""
        self.root.ids.category.text = ""
        self.root.ids.bottom_label.text = ""

    def over_app(self):
        self.movies.save_movies("movies.csv")

    pass


if __name__ == '__main__':
    MoviesToWatchApp().run()
