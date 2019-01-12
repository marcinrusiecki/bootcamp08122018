towary = {'jabłko':10, 'gruszki':5, 'papryka':7}
magazyn = {'jabłko':100, 'gruszki':58, 'papryka':75}

k = None
j = towary['jabłko']
g = towary['gruszki']
p = towary['papryka']

mj = magazyn['jabłko']
mg = magazyn['gruszki']
mp = magazyn['papryka']

role = input("Czy jesteś klientem(k) czy dostawcą(d): ")
if role.lower() == "k":

    while True:

        print("""
        Towary w sklepie:
        0 - zakoncz
        1 - jabłka
        2 - gruszki
        3 - papryka
        """)

        towar = int(input("Wybierz towar z listy: "))
        if towar == 0:
            print("Zapraszamy ponownie")
            break
        else:
            waga = float(input("Podaj wagę w kg: "))
            if towar == 1:
                if waga > mj:
                    print("Brak towaru w sklepie")
                    break
                k = j * waga
                print("Cena za", waga, "jabłek wynosi", k)
                mj -= waga
                print(mj)
            elif towar == 2:
                k = g * waga
                print("Cena za", waga, "gruszek wynosi", k)
            elif towar == 3:
                k = p * waga
                print("Cena za", waga, "papryki wynosi", k)
            else:
                print("Brak towaru w sklepie")

elif role.lower() == "d":
    do_dodania = input("Wprowadz [produkt, waga, cena]: ")
    produkt, waga, cena = do_dodania.split()
    waga = waga
    cena = float(cena)
    print(do_dodania)





produkty = {
    "ziemniaki": 1.99,
    'pomidory': 6.99,
    'woda': 1.79,
}
magazyn = {
    "ziemniaki": 10,
    'pomidory': 10,
    'woda': 10,
}

while True:
    rola = input("Czy jesteś [klient]em [k], czy [dostawca][d], [q] by zakończyć? ")
    if rola.lower() in ['klient', 'k']:
        while True:
            print("Nasz sklep oferuje: ")
            for produkt, cena in produkty.items():
                print(f' - {produkt} - {cena:.2f}')
            zakup = input("Co chcesz kupić? [k] by zakończyć: ")
            if zakup.lower() == 'k':
                print("Zapraszamy ponownie")
                break
            if zakup not in produkty:
                print("Nie ma takiego produkty")
                continue
            waga = float(input(f"Ile chcesz kupić - [{zakup}]: "))
            if waga > magazyn[zakup]:
                print()
                print("!! Nie ma tyle w magazynie !!")
                print(f"W magazynie pozostało: {magazyn[zakup]}")
                print()
            else:
                cena = produkty.get(zakup)
                koszt = waga * produkty[zakup]
                print(f"Za [{zakup}] zapłacisz: {koszt:.2f}")
                magazyn[zakup] -= waga

    elif rola.lower() in ['dostawca', 'd']:
        # ścieżka dostawcy
        # dodanie produktu -'d'
        # zmiana ceny - 'z'
        # prosimy o podanie produkty w formacie nazwa ilosc cena
        while True:
            do_dodania = input("Podaj produkt w formacie [nazwa ilosc cena]: ")
            if len(do_dodania.split()) == 3:
                nazwa, ilosc, cena = do_dodania.split()
                try:
                    ilosc = float(ilosc)
                    cena = float(cena)
                    produkty[nazwa] = cena
                    break
                except ValueError:
                    print("Niepoprawna cena lub ilosc")


            else:
                print("Podałeś produkt w niepoprawnym formacie")
        if nazwa in magazyn:
            magazyn[nazwa] = magazyn[nazwa] + ilosc
        else:
            magazyn[nazwa] = ilosc

        magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc

        print("Dziekuję. Produkt Dodany")
    elif rola.lower() == 'q':
        print("Program przestaje działać")
        break