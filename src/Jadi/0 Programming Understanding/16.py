# Dictionary & Type
Name_1 = "Mohammad"
Job_1 = "Living"
Dictionary = {"Saeed": "Programmer", "Ali": "Bikar", Name_1: Job_1, "Income": 10**7}
Dictionary
Dictionary["Ali"]
Dictionary[Name_1]
Dictionary.get("Akbar", "None")
Dictionary.keys()
Dictionary.values()
"Akbar" in Dictionary
"Ali" in Dictionary
Dictionary["Mother"] = "Empty"
Dictionary["Key"] = "Value"
Dictionary["Me"] = "98930"
del Dictionary["Saeed"]
print(Dictionary)
type(Dictionary)
for Writing in Dictionary:
    print(Writing)
for Writing_2 in Dictionary.items():
    print(Writing_2)
for Key, Value in Dictionary.items():
    print("Our Key is", Key, "And our Value is", Value)
