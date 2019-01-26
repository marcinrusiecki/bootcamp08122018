class Pracownik():

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godzin = 0

    def register_time(self, godzin):
        self.godzin = godzin
        if godzin > 8:
            self.godzin += godzin - 8

    def pay_salary(self):
        wyplata = self.stawka * self.godzin
        self.godzin = 0.0
        return wyplata


employee = Pracownik("Adam", "Kowalski",40)
employee.register_time(5)
print(employee.pay_salary())
employee.pay_salary()
