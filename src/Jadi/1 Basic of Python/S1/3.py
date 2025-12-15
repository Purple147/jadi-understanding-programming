# Seeing not Improve you so Doing Improve you, Seeing others codes(Hack), Big Programm is successful smals programms, Debugging(Sosk)
# Outing 1: Game Programming, FlowChart(Start, Computer saving datas, Player Gausing, False answer, Doning somethings, Correct answer and finish)
import random

random.seed()
Random_Number = random.randrange(100)
Name = input("Please Enter Your Name: ")
Gause_Number = input("Your Gause Number is: ")
Real_Gause_Number = int(Gause_Number)


while Real_Gause_Number != Random_Number:
    print("Welcome", Name)
    if Real_Gause_Number != Random_Number:
        if Real_Gause_Number > Random_Number:
            print("Help: its lower than this")
        elif Real_Gause_Number < Random_Number:
            print("Help: its bigger than this")
    Gause_Number = input("Gause more time: ")
    Real_Gause_Number = int(Gause_Number)


print("Well Done", Name, "Your Job is Greet")
print("Number is", Random_Number)


# Reverse This Game(Me and Cumputer)
Name_2 = random.randint(0, 7**4)
Random_Number_2 = input()
Random_Number_2 = int(Random_Number_2)
Gause_Number_2 = random.randrange(100)
Needed_1 = random.randrange(100)
Needed_2 = random.randrange(100)
Uper = 0
Lower = 100

while Gause_Number_2 != -1:
    print("Welcome", Name_2)
    print(Gause_Number_2)
    Status = input()
    if Status == "Uper":
        Uper = Gause_Number_2
    elif Status == "Lower":
        Lower = Gause_Number_2
    elif Status == "Correct":
        input()
        break
    Gause_Number_2 = random.randrange(Uper, Lower)
