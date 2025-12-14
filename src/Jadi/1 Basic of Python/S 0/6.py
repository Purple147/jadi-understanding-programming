# Features in Technology = if, else, elif(else if), input()
Mohammad = "Programmer"
mohammad = 24
Roxana = 18
if Mohammad == "Programmer":
    if mohammad >= Roxana:
        status = True
        print(status, type(status))
        print("You are a", Mohammad, "and older than roxana by", mohammad, "Years old")

    else:
        status = False
        print(status, type(status))
        print("You are not a", Mohammad, "and roxana older than you", mohammad)


if mohammad < Roxana:
    Answer = "Roxana older than you"
elif mohammad == Roxana:
    Answe = "You and Roxana in same age"
else:
    Answer = "You are older than Roxana"


print(Answer)


Name = "Your name is: "
name = input(Name)
if name == "Purple147":
    Result = "Great Name"
elif name == "Sineme333":
    Result = "Not bad a Name"
else:
    Result = "You out of System Now"


print(Result)
