class ElectricCar():
    def __init__(self,max_range):
        self.range = max_range
        self.max_range = max_range

    def drive(self,distance):
        if distance > self.range:
            wynik = self.range
            self.range = 0
            return wynik
        else:
            self.range -= distance
            return distance

    def charge(self):
        self.range = self.max_range
        print(self.range)

car = ElectricCar(200)
print(car.drive(70))
print(car.drive(50))
print(car.drive(20))
car.charge()
print(car.drive(70))
print(car.drive(70))
print(car.drive(300))
print(car.drive(300))

