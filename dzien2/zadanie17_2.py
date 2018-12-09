dane = input("Podaj liczby po spacjach: ")

dane = dane.split()
dane2 = []
for d in dane:
    dane2.append(int(d))

dane = [int(d) for d in dane]

print(dane)
print(dane2)