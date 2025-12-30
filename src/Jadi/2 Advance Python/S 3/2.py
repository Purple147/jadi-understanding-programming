# Regex = data extracting without requests or any other tools like google do, Regex -> Data -> Database -> what I want to do = Google 
# readin data in wb by requests, API, Deep learning happen in needs
# UTF-8 = Readin in every languages without errors, doing regex is hard to do in real projects so we need to just know that
import requests
url = "https://google.com"
r = requests.get(url)
print(r)
print(r.text)

url2 = "https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD"
r2 = requests.get(url2)
print(r.json())
last_price = r.json()["last"]
highest_price = r.json()["high"]
lowest_price = r.json()["low"]
print("for bitcoin to now last price is %f and highest price is %f and lowest is %s" % (last_price, highest_price, lowest_price))

print("سلام بر دوستام گلم از UTF-8 چه خبر")
