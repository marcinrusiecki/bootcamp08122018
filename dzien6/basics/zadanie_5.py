miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = int(input(f"Dystans {miasto_a} {miasto_b}: "))
cena_paliwa = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))
print()
koszt = (dystans / 100) * spalanie * cena_paliwa

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt} PLN")
