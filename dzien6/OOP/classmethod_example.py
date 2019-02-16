from datetime import date

# random Person
class Osoba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Osoba('Adam', 19)
person.display()

person1 = Osoba.fromBirthYear('John',  1985)
person1.display()


Osoba('Johon',  date.today().year - 1985)

print(date.today().year)