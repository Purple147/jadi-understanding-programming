# Tuple, immutable like lists and strings, (), slice, split(), join(), Dictionary, items(), list(), %s,
Four = 4
arosak = (0, 1, 2, "Three", Four)
print(arosak, type(arosak))
print(arosak[3])
Tuples = tuple()
print(arosak[2:4])
zero, one, two, three, four = arosak
print(zero, one, two, three, four)
zero, one, three = 00, 11, 33
print(zero, one, two, three, four)
print(arosak)
zero, one = one, zero
print(zero, one, two, three, four)
MyPhone = "9892345235235623425"
print(MyPhone)
MyNewPhone = MyPhone.split("4")
print(MyNewPhone)
print("4".join(MyNewPhone))
MyGmail = "Mohammad@gmail.com"
Name, Domain = MyGmail.split("@")
print(MyGmail, Name, Domain)
Dictionary = {"Mohammad": "Hacker", "Hacker": 147}
print(Dictionary, Dictionary.items())
print(list(Dictionary), list(Dictionary.items()))


for key, value in list(Dictionary.items()):
    print("Names is", key)
    print("Jobs is", value)


Dictionary_2 = {("Mohammad"): ("Purple")}
print(Dictionary_2)
Dictionary_3 = dict()
Dictionary_3["Mohammad", "Purple147"] = "Hacker"
print(Dictionary_3)
