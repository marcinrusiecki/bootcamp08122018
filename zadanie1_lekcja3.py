def liczby_pierwsze(liczba):
    if (liczba % 2 == 1) or (liczba == 2):
        print("Tak")
    else:
        print("Nie")


wynik = liczby_pierwsze(int(input("Podaj liczbę: ")))




