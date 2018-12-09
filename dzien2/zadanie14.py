
znalezione_max = None
znalezione_min = None
liczba = None

while True:

    komenda = input("Podaj liczbę lub k aby zakończyć ")
    if komenda == "k":
        break
    if len(komenda) > 0 and komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = - liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("Nie podałeś liczby")

    if liczba or liczba ==0:
        if znalezione_max is None or liczba > znalezione_max:
            znalezione_max = liczba
        if znalezione_min is None or liczba < znalezione_min:
            znalezione_min = liczba

print("Znalezione maksimum to: ",znalezione_max, "Znalezione maksimum to: ",znalezione_min )


