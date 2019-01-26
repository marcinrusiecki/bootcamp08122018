

class Psy:
    def __init__(self, nazwa, age):
        self.nazwa = nazwa
        self.age = age


def najstarszy(*args):
    dog_ages = []
    for dog in args:
        dog_ages.append([dog.age, dog.nazwa])
    dog_ages.sort()
    return dog_ages[-1][1]

piesek = Psy("mruczek", 10)
piesek2 = Psy("Rex", 2)
piesek3 = Psy("Reksio", 60)


print(najstarszy(piesek,piesek2,piesek3))








