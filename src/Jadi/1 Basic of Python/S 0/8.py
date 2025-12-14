# Impotant of doing, reverse numbers problem
# One
print("Hello World!")

# Two
Number_1 = input()
Number_2 = input()
RealNumber_1 = int(Number_1)
RealNumber_2 = int(Number_2)
print(RealNumber_1 * RealNumber_2)
# Three IDN
# Four IDN
# Five
Number_3 = input()
Number_4 = input()


if Number_3 > Number_4:
    print(Number_3)
elif Number_4 > Number_3:
    print(Number_4)
else:
    print(Number_3 or Number_4)

# Six
Number_5 = input()
RealNumber_5 = int(Number_5)


if 6 > RealNumber_5 > 0:
    Result = "Khordsal"
elif 10 > RealNumber_5 >= 6:
    Result = "koodak"
elif 14 > RealNumber_5 >= 10:
    Result = "nojavan"
elif 24 > RealNumber_5 >= 14:
    Result = "javan"
elif 40 > RealNumber_5 >= 24:
    Result = "bozorgsal"
elif RealNumber_5 >= 40:
    Result = "miansal"


print(Result)
