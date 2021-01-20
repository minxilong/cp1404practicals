"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.capitalize()
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    list(enumerate(new_name))
    str = '_'
    for i, char in enumerate(new_name):
        if new_name[i].islower() and new_name[i+1].isupper():
            str.join()
    return new_name


main()
# demo_walk()