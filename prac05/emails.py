def get_name():
    email_dict = {}
    while True:
        email=input('Email: ')
        if email=='':
            print('')
            break
        list=email.split('@')
        name=list[0].replace('.', ' ').title()
        choice=input('Is your name {}? (Y/n)'.format(name)).lower()
        if choice=='n' or choice=='no':
            name=input('Name: ')
        email_dict[email]=name.title()
    for key, value in email_dict.items():
        print('{} ({})'.format(value, key))

def main():
    get_name()
main()