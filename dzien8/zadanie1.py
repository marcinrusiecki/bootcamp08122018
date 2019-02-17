import json
import getpass
try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []
op = ""
while op!="0":
    op = input("Co chcesz zrobić? [d - dodaj, w - wypisz, 0 - zakoncz, u - usun]: ")
    if op == 'd':
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        rok_ur = int(input("Rok urodzenia: "))
        pensja = float(input("Pensja: "))
        pracownicy.append({"imie": imie, "nazwisko": nazwisko,
                           "rok_urodzenia": rok_ur, "pensja": pensja})
        with open("pracownicy.json", "w") as plik:
            json.dump(pracownicy, plik)
    elif op == 'w':
        for nr, p in enumerate(pracownicy, 1):
            print(f"- [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['rok_urodzenia']}, pensja: {p['pensja']} PLN")

    elif op == 'u':
        for nr, p in enumerate(pracownicy, 1):
            print(f"- [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['rok_urodzenia']}, pensja: {p['pensja']} PLN")
        usun = int(input("Podaj numer pracownika którego chcesz usunąć: "))
        haslo = getpass.getpass("Podaj haslo: ")
        if haslo !="TAJNE":
            print("Zle haslo")
        else:
            del pracownicy[usun-1]
            with open("pracownicy.json", "w") as plik:
                json.dump(pracownicy, plik)