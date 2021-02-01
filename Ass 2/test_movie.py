"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: Write tests to show this initialisation works
    print(initial_movie)

    # TODO: Add more tests, as appropriate, for each method
    initial_movie.watched_unwatched()
    assert initial_movie.is_watched == False

    initial_movie.unwatched_watched()
    assert initial_movie.is_watched == True


run_tests()
