def czy_jest_pierwsza(a):
    if (a % 2 == 1) or (a == 2):
        print("Liczba jest pierwsza")
        return True
    else:
        print("Liczba nie jest pierwsza")
        return False

liczba = czy_jest_pierwsza(int(input("Podaj liczbę: ")))
