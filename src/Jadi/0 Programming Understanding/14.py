# libraries, solving jadi's problem, continue
import random

random.seed()
peoples = [100] * 50
count_numbers = 0


for changing in range(1000000):
    random_number_1 = random.randrange(50)
    random_number_2 = random.randrange(50)
    count_numbers += 1
    if peoples[random_number_1] < 1:
        continue
    peoples[random_number_1] -= 1
    peoples[random_number_2] += 1


print("for", count_numbers, "times", peoples)


# way 2
import random

random.seed()
count_numbers = 0
peoples = []
for room in range(50):
    peoples.append(100)


for changing in range(1000000):
    random_number_1 = random.randrange(50)
    random_number_2 = random.randrange(50)
    count_numbers += 1
    if peoples[random_number_1] < 1:
        continue
    peoples[random_number_1] -= 1
    peoples[random_number_2] += 1


print("for", count_numbers, "times", peoples)
