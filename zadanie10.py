liczba1 = int(input("Podaj liczbę pierwszą: "))
liczba2 = int(input("Podaj liczbę drugą: "))
rodzaj_operacji = input("Wyierz rodzaj operacji spośród +, -, *, / : ")

if rodzaj_operacji == "+":
    print("Wynik: ", liczba1 + liczba2)
elif rodzaj_operacji == "-":
    print("Wynik: ", liczba1 - liczba2)
elif rodzaj_operacji == "*":
    print("Wynik: ", liczba1 * liczba2)
else:
    print("Wynik: ", liczba1 / liczba2)