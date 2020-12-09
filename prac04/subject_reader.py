FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print(get_details())

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list.append(parts)
    input_file.close()
    print(list)

def get_details():
    input_file = open(FILENAME)
    list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list.append(parts)
        subject = parts[0]
        name = parts[1]
        num = parts[2]
        print('{} is taught by {:<12} and has {:3} students'.format(subject,name,num))
    input_file.close()


main()