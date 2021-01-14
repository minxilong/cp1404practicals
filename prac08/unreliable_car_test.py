from unreliable_car import UnreliableCar

def main():
    unreliablecar=UnreliableCar('car', 500, 50)
    time=int(input('Enter the time you want to test: '))
    for i in range(time):
        print('{} drives {}km'.format(unreliablecar.name, unreliablecar.drive(10)))
    print(unreliablecar)

main()