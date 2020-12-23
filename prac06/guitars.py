from guitar import Guitar

def main():
    guitars=[]
    print('My guitars!')
    name=str(input('Name: '))
    while name != '':
        year=int(input('Year: '))
        cost=float(input('Cost: $'))
        print('{} ({}) : ${} added.'.format(name, year, cost))
        guitar=Guitar(name, year, cost)
        guitars.append(guitar)
        name = str(input('Name: '))

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print('These are my guitars:')
    i=0
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string=' (vintage)'
        else:
            vintage_string =''
        print('Guitar {}: {:>20} ({:4}), worth ${:10,.2f}{}'.format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
        i+=1

main()