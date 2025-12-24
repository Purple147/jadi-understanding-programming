# OOP, IOT(Internet Of Things), OOP IOT(Object Oriented Programming Internet Of Things), inherite
# Constructure, sudo coe = like a full code but is not full code
# we can programming everything we don't know by OOP and making(constructure)
# OOP sometime is good and sometime is bad, we see what way is simplier 
# usint best tool for best doing
class device:
    count = 0
    def __init__(self, name, ip, mac):
        self.name = name 
        self.ip = ip
        self.mac_address = mac
        device.count += 1
        # result = ping the device
        if "result":
            self.status = "active"
        else:
            self.status = "Unknown"
        def get_status(self):
            # return result based on ping result fo self.ip
            pass
    def inf(self):
        return self.name, self.ip, self.mac_address    


SumsongJ2 = device("J2", "127.0.0.1", "asdf0932u9023j023")
chosen = input()
if chosen == "give it to me":
    print(SumsongJ2.inf())
else:
    pass
SumsongJ2.status = "Android 7"

class TV(device):
    def turn_on(self):
        # connect to self.ip and turn on
        pass
    def trun_off(self):
        # connect to self.ip and turn off
        pass

class Thermostat(device):
    def get_degree(self):
        # connect to self.ip and read degree and return the result
        return "result"
        pass

class SmartTV(TV):
    def turn_on(self):
        # turn on smart TV from mac self.ip
        pass
