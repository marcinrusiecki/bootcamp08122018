import sys
import json
import requests
lokalizacja = sys.argv[1]

lokalizacja = input("Podaj miasto: ")

resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={lokalizacja.replace(' ', '%20')}")


woid = resp.json()[0]['woeid']

resp1 = requests.get(f"https://www.metaweather.com/api/location/{woid}/")

pogoda = resp1.json()['consolidated_weather'][0]


print(f"Pogoda w lokalizacji {lokalizacja}")
print("Temperatura: ", pogoda['the_temp'])


