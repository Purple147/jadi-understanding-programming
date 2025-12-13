# project eular 2
def even_numbers(number):
    return number % 2 == 0


number_1 = 0
number_2 = 1
summing = 0
while number_1 < 4 * 10**6:
    if even_numbers(number_1):
        summing += number_1
    number_3 = number_1 + number_2
    number_1 = number_2
    number_2 = number_3
    print(number_1, summing)


# Way two
number_1 = 0
number_2 = 1
summing = 0
while number_1 < 4 * 10**6:
    if number_1 % 2 == 0:
        summing += number_1
    number_3 = number_1 + number_2
    number_1 = number_2
    number_2 = number_3
    print(number_1, summing)
