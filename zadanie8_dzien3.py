
def wiecej_niz(napis,prog):
    wynik = set()
    unikalne = set(napis)
    for c in unikalne:
        if napis.count(c) > prog:
            wynik.add(c)
    return wynik



dane = wiecej_niz(input("Wprowadz napis: "), 6)
print(dane)


