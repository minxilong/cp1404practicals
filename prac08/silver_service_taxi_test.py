from silver_service_taxi import SilverServiceTaxi

def main():
    taxi=SilverServiceTaxi('taxi', 100, 2)
    taxi.drive(18)
    print(taxi)
    print('fare = ${}'.format(taxi.get_fare()))

main()