from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def list_taxi(taxis):
    mark=0
    for i in range(len(taxis)):
        print('{} - {}'.format(mark, taxis[i]))
        mark+=1


def choose_taxi(taxis):
    print("Taxis available: ")
    mark = 0
    for i in range(len(taxis)):
        print('{} - {}'.format(mark, taxis[i]))
        mark += 1

    taxi_choice=int(input("Choose taxi: "))
    if taxi_choice<0 or taxi_choice>len(taxis):
        print('Invalid choice\n')


def drive(taxis, current_taxi, total_cost):
    if current_taxi == None:
        print('Please choose a taxi first!')
    else:
        current_taxi.start_fare()
        distance=int(input("Drive how far? "))
        current_taxi.drive(distance)
        cost=current_taxi.get_fare()
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost))
        total_cost+=cost


def main():
    current_taxi = None
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print('Let\'s drive!')
    while True:
        choice=str(input('q)uit, c)hoose taxi, d)rive\n>>> ')).lower()

        valid_choice = "qcd"
        if choice not in valid_choice:
            print("Invalid choice.\n")

        if choice == 'c':
            current_taxi=choose_taxi(taxis)

        if choice == 'd':
            drive(taxis, current_taxi, total_cost)

        if choice == 'q':
            print("Total trip cost: ${:.2f}".format(total_cost))
            print("Taxis are now:")
            list_taxi(taxis)

        print("Bill to date: ${:.2f}\n".format(total_cost))

if __name__ == '__main__':
    main()