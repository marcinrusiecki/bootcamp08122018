class BasketEntry:
    def __init__(self, product, quantity):

        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f'{self.product.nazwa} x {self.quantity}'

    def generate_report(self):
        return f'- {self.product.nazwa} ({self.product.id}), cena: {self.product.cena} x {self.quantity}\n'



class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product, qty):
        self.entries.append(BasketEntry(product, qty))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        out = "Produkty w koszyku:\n"
        for entry in self.entries:
            out += entry.generate_report()
        out += f"W sumie: {self.count_total_price()}"
        return out

class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena






basket = Basket()
product = Product(1,"Woda",3)
basket.add_product(product,5)
product1 = Product(1,"Ryż",2)
basket.add_product(product1,53)
product2 = Product(1,"Maka",6)
basket.add_product(product2,3.6)
print(basket.count_total_price())
print(basket.generate_report())