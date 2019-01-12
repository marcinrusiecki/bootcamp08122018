zbior = set()
parzyste = set(range(0,100,2))

while True:

    liczba = input("Wprowadz liczbę lub zakoncz k: ")
    if liczba == "k":
        break
    else:
        liczba = int(liczba)
        zbior.add(liczba)

print(zbior)
print("liczb unikalnych jest ", len(zbior))
print("liczb parzystych jest ", len(zbior & parzyste))

