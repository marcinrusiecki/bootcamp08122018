import json
import requests
import decimal
import urllib.parse
#urllib.parse.urlparse("sciezkahttp")
resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
resp = resp.json(parse_float=decimal.Decimal)[0]['rates']

print("Dysponuję walutami: ")
for k in resp:
    print(k)

waluta = input("Podaj kod waluty: ")
ilosc = decimal.Decimal(input("Za ile chcesz kupic: "))

for k in resp:
    if k['code'] == waluta:
        print(f"Za {ilosc} możesz kupić {ilosc/k['mid']}")

