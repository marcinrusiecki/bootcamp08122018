dlugosc = int(input("Długość: "))
szerokosc = int(input("Szerkość: "))
wysokosc = int(input("Wysokość: "))

objetosc = dlugosc * szerokosc * wysokosc

print(f"Objętość wynosi: {objetosc}")
print(f"Czy większe od 1 litra: {objetosc > 1000}")

if objetosc > 2000:
    print("Objętość jest większa niż 2 litry")
elif objetosc > 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętość jest mniejsza niż 1 litr")

print("To jest koniec programu")