# say hi, space and no space, def
fourth = "Nisa"
for calling in {"Jadi", "Saiid", "Mohammad", fourth}:
    print("Hello", calling)
    print("Bye" + calling)
    print("Nice to meet you " + calling)


def calling_2(c1, c2):
    print(c1, c2)


for calling in range(0, 4):
    calling_2("Hello", calling)


def calling_3():
    print("Hello")


for calling in "FUM":
    calling_3()
    print(calling, "thing about")


def calling_4(name):
    print("Hello", name)


for calling in ["Shakira", "Amo Jani", "Alexis", "lana"]:
    calling_4(calling)


# numbers summing
def summing_numbers(n1, n2):
    print(n1 + n2)


summing_numbers(10, 23)


def summing_numbers_2(number_1, number_2):
    while number_1 < 100:
        number_3 = number_1 + number_2
        number_1 = number_2
        number_2 = number_3
    return number_1, number_2, number_3


print(summing_numbers_2(0, 0.00009))


def summing_numbers_3(n1):
    for summing in range(0, 10):
        n1 *= 2
        print(n1)
    return n1


summing_numbers_3(1)
