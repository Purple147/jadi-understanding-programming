# API, Deep curl, OAuth 2 = Security API in a Private API in a Public API, database
import requests

API_Key_Storage_ID = "59ecc487e4b03ffa030b24cf"
API_Key_Auth_ID = "59ecc487e4b0edcca31c1d09"
API_Key_Auth_Key = "59ecc487e4b05ef67685eff4"
url_1 = "https://api.cacktory.com/auth/login"
url_2 = "https://api.backtory.com/%s/classes/divar/" % API_Key_Storage_ID
Username = "divar"
Password = "qwe"
Auth = {
    "username": Username,
    "password": Password,
    "id": API_Key_Auth_ID,
    "key": API_Key_Auth_Key,
}
Login = requests.get(url_1, auth=Auth)
Text = {"text": "Fuck You Girl", "average_score": 1, "average_age": 18}
Object_Storage = requests.get(url_2, Text)

print(Auth, Object_Storage)
