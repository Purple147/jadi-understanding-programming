# libraries, matplotlib

import matplotlib.pyplot as plt

plt.bar(range(30), range(30))
plt.show()


# Two
import matplotlib.pyplot as plt


def Prime_number(number):
    Status = True
    for Prime_numbers in range(2, int(number**0.5) + 1):
        if number % Prime_numbers == 0:
            Status = False
    return Status


for barchart in range(2, 1 * 10**3):
    if Prime_number(barchart):
        plt.bar(barchart, barchart)
plt.show()

# Three
import random

import matplotlib.pyplot as plt

random.seed()
Peoples = [100] * 1 * 5 * 10
Counts_Times = 0
for Room in range(1 * 50):
    Random_1 = random.randrange(50)
    Random_2 = random.randrange(50)
    Counts_Times += 1
    if Peoples[Random_1] < 1:
        continue
    Peoples[Random_1] -= 20
    Peoples[Random_2] += 20
    plt.bar(range(50), sorted(Peoples, reverse=True))
plt.show()
