"""
Name: Minxi Long
URL: https://github.com/JCUS-CP1404/assignment-2---movies-2-minxilong
"""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

import csv
from movie import Movie
from moviecollection import MovieCollection


def get_data(filename):
    # Get movies data from csv file into a list
    list = []
    file = open(filename).readlines()
    for line in file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[1] = int(parts[1])  # Make the number an integer
        list.append(parts)
    return list


def list_movies(list):
    watched = 0
    unwatched = 0
    mark = 0
    for line in list:
        # Get the number of watched movies and unwatched movies
        if line[3] == 'w':
            watched += 1
        else:
            unwatched += 1
        # List the movies
        print('{:2}. {:3^} {:<35} - {:>5} ({})'.format(mark, '*' if line[3] == 'u' else ' ', line[0], line[1], line[2]))
        mark += 1
    print('{} movies watched, {} movies still to watch\n'.format(watched, unwatched))


def watch_movies(list):
    # See if all movies have watched
    unwatched = 0
    for line in list:
        if line[3] == 'u':
            unwatched += 1
    if unwatched == 0:
        print('No more movies to watch!\n')
        return

    print('Enter the number of a movie to mark as watched')
    # Ensure valid input
    valid_input = False
    while not valid_input:
        try:
            mark = int(input('>>> '))
            while mark < 0:
                print('Number must be >= 0')
                mark = int(input('>>> '))
            while mark > len(list):
                print('Invalid movie number')
                mark = int(input('>>> '))
            valid_input = True
        except:
            print('Invalid input; enter a valid number')

    # Add an unwatched movie to watched
    if list[mark][3] == 'u':
        print('{} from {} watched\n'.format(list[mark][0], list[mark][1]))
        list[mark][3] = 'w'
        return
    else:
        print('You have already watched {}\n'.format(list[mark][0]))


def add_movies():
    # Ensure valid input
    valid_title = False
    while not valid_title:
        title = input('Title: ')
        if title == '':
            print('Input can not be blank')
        else:
            valid_title = True

    # Ensure valid input
    valid_year = False
    while not valid_year:
        try:
            year = int(input('Year: '))
            while year < 0:
                print('Number must be >= 0')
                year = input('Year: ')
            valid_year = True
        except:
            print('Invalid input; enter a valid number')

    # Ensure valid input
    valid_cate = False
    while not valid_cate:
        category = input("Category: ")
        if category == '':
            print('Input can not be blank')
        else:
            valid_cate = True

    # Add an unwatched movie to the list
    print("{} ({} from {}) added to movie list\n".format(title, category, year))
    return [title, year, category, 'u']


def main():
    # Import csv file
    filename = 'movies.csv'
    list = get_data(filename)
    print("Movies To Watch 1.0 - by <Minxi Long>\n{} movies loaded".format(len(list)))
    while True:
        # Get menu
        choice = str(input("Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit\n>>> ")).upper()

        # When choice not in the menu
        valid_choice = "LAWQ"
        if choice not in valid_choice:
            print("Invalid menu choice.\n")

        if choice == 'L':
            list_movies(list)

        if choice == 'W':
            watch_movies(list)

        if choice == 'A':
            line = add_movies()
            list.append(line)

        if choice == 'Q':
            # Write movies into csv file
            out_file = open(filename, 'w')
            for line in list:
                out_file.write(line[0] + ',' + str(line[1]) + ',' + line[2] + ',' + line[3] + '\n')
            out_file.close()
            print('{} movies saved to {}\nHave a nice day :)'.format(len(list), filename))
            break


if __name__ == '__main__':
    main()
