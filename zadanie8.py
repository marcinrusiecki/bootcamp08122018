szerokosc = int(input("Podaj szerokość opakowania w cm: "))
dlugosc = int(input("Podaj szerokość opakowania w cm: "))
wyskosc = int(input("Podaj szerokość opakowania w cm: "))

objetosc= szerokosc*dlugosc*wyskosc
if objetosc > 1000:
    print("Objetosc opakowania jest wieksza niz 1 litr i wynosi", objetosc)
elif objetosc == 1000:
    print("Objetosc opakowania jest równa 1 litr")
else:
    print("Objetosc opakowania jest mniejsza niz 1 litr i wynosi", objetosc)