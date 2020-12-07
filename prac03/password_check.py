def main():
    password = get_password()
    print('*'*len(password))

def get_password():
    password=str(input('Enter your password: '))
    return password

main()