lista = [100, -100, 2, -2, 100, 2, -2, 0]

licznik_dodatnich = 0
licznik_ujemnych = 0

for liczba in lista:
    if liczba > 0:
        licznik_dodatnich += 1
    elif liczba < 0:
        licznik_ujemnych += 1

print(f"Liczba dodatnich: {licznik_dodatnich}, liczb ujemnych {licznik_ujemnych}")

licznik_dodatnich = len([x for x in lista if x > 0])
licznik_ujemnych = len([x for x in lista if x < 0])

print(f"Liczba dodatnich: {licznik_dodatnich}, liczb ujemnych {licznik_ujemnych}")
