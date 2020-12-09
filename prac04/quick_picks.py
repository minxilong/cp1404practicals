# Choose sets of random numbers
import random
num_line=6
quick_pick=int(input('How many quick picks? '))

for i in range(quick_pick):
    CONSTANTS = []
    for n in range(6):
        num=random.randint(1, 45)
        while num in CONSTANTS:
            num = random.randint(1, 45)
        CONSTANTS.append(num)
    CONSTANTS.sort()
    print(" ".join("{:2}".format(num) for num in CONSTANTS))