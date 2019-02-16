class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Cześć jestem {self.imie} {self.nazwisko}")


class Pracownik(Osoba):

    def pracuj(self):
        print("Pracuję ...")

    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko)
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"pracuje jako {self.stanowisko}")

class Informatyk(Pracownik):

    def pracuj(self):
        print("Programuje")

osoba = Osoba("Adam", "Słodowy")
osoba.przedstaw_sie()


pracownik = Informatyk("Rafał", "Korzeniewski", "trener")

pracownik.przedstaw_sie()

pracownik.pracuj()
