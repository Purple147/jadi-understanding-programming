# Making a program, ''', """, #TODO, Systems URL, BreakPoin(F9)
import requests

API_Key = "4D59644B442B52423271633873314C6B6F2F34413D3D"
url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_Key
api = requests.get(url)
Sender = "9812949515"
Receptor = "981231231", "98123123123", "981231231"
payload = {
    "message": "hey there, i'm sorry for your time's losting, your time giving is 3 days",
    "receptor": Receptor,
    "sender": Sender,
}

requests.post(url, data=payload)

# Way Two
FileName = "C:/Users/Persatech/Desktop/Phones.txt"

Text = """Hi there, how are you, your book is sending and if you not give a book in a 3 days later
content with me by godcraft1380@gmail.com, hopely good well
"""


def Read_Phones(FileName):
    with open(FileName) as filename:
        content = filename.readlines()
    content = [x.strip() for x in content]
    return content


def Send_SMS(Number, Text):
    API_Key = "7A4F794F53557935526D346C414F673456626E4866413D3D"
    url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_Key
    payload = {"receptor": Number, "massage": Text}
    api = requests.post(url, data=payload)
    return api.ok


Phones = Read_Phones(FileName)


for Phone in Phones:
    if not Send_SMS(Phone, Text):
        print(Phones)
