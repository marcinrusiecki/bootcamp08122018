class Samochod:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def wyswietl_nazwe(self):
        print(f'Twoj samochod to: {self.nazwa}')

moj_samochod = Samochod(input("Wprowadz nazwe samochodu: "))
print(moj_samochod.nazwa)
moj_samochod.wyswietl_nazwe()


imiona = ['Basia', 'Jarek']

class Dane:
    def __init__(self, imie):
        self.imie = imie
    def dodaj_imie(self):
        imiona.append(self.imie)
    def wyswietl_imie(self):
        if len(imiona)>1:
            print(imiona)
        else:
            print("Brak imion w bazie")
print("""Jeśli chcesz wyswietlić imiona naciśnij 1
         Jeśli chcesz dodać imie naciśnij 2
         Aby zakończyć naciśnij 0
      """)
wybor = int(input("Co chcesz zrobić: "))

if wybor == 1:
    pobierz_dane = Dane(imiona)
    pobierz_dane.wyswietl_imie()
elif wybor == 2:
    wprowadz_dane = input("Wprowadz imie: ")
    wprowadz_dane = Dane(wprowadz_dane)
    wprowadz_dane.dodaj_imie()
    print(imiona)





