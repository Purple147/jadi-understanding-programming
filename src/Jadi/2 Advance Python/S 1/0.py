# We have advance pure python too, we going to learn speceficts python things, Lambda Functions, Functions do = easier and shorter doing
# Lambda Functions have expiring(After using they going to useless) = AnonyMouse, Lambda Function = 1/2/... Argoman: 1 Expression
# Sorting, sort(),map, filter
def Lambda_1(Number_1):
    print(Number_1**2)


Lambda_1(4)


Lambda_2 = lambda Number_2: Number_2**2


print(Lambda_2(4))


List = [(20, 111), (24, 355), (14, 25), (367, 89)]
NewList = list()


for vibration in List:
    for vibration_2 in vibration:
        NewList.append(vibration_2)
        NewList.sort()


print(NewList)


List_2 = [(1, 33), (0, 44), (3, 11), (55, 0)]
By_Left_Sorted = List_2.sort()
print(List_2)


def ByRightSorted1(LIST):
    LIST.reverse()
    LIST.sort()
    LIST.reverse()


By_Right_Sorted_1 = ByRightSorted1(List_2)
print(List_2)


By_Right_Sorted_2 = List_2.sort(key=lambda y: y[1])
print(List_2)


LiSST = [(2), (11), (55), (5134), (0.24)]


print(list(map(lambda x: x * 2, LiSST)))

lisT = [1, 3, 5, 6, 8, 11, 123, 44, 1, 0, 22, 13]

for vibration_11 in lisT:
    if vibration_11 >= 10:
        print("Big")
    else:
        print("Small")

print(list(map(lambda x: "Big" if x >= 10 else "Small", lisT)))


lliisstt = [3, 55, 148, 12, 0.444, 123]

for vibration147 in lliisstt:
    if vibration147 % 2 == 0:
        print(vibration147)


print(list(filter(lambda x: x % 2 == 0, lliisstt)))
