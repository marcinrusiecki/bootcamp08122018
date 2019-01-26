class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"ID: {self.id}, Nazwa: {self.nazwa}, Cena: {self.cena}")

product = Product(1, "Woda", 2)
product.print_info()
