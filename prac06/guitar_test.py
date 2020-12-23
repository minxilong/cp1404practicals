from guitar import Guitar

def test():
    guitar1=Guitar('Gibson L-5 CES',1922,16035.40)
    guitar2=Guitar('Another Guitar',2013,10000.00)
    print('{} get_age() - Expected {}. Got {}'.format(guitar1.name, 98, guitar1.get_age()))
    print('{} get_age() - Expected {}. Got {}'.format(guitar2.name, 7, guitar1.get_age()))
    print('{} is_vintage() - Expected {}. Got {}'.format(guitar1.name, True, guitar1.is_vintage()))
    print('{} is_vintage() - Expected {}. Got {}'.format(guitar2.name, False, guitar2.is_vintage()))

test()