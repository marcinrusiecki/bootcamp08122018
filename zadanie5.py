miastoA = input("Podaj nazwę miejscowości A: ")
miastoB = input("Podaj nazwę miejscowości B: ")
dystans = int(input(f"Podaj dystans między {miastoA} {miastoB}: "))
cena_paliwa = float(input("Podaj cenę paliwa: "))
spalanie = float(input("Podaj spalanie na 100 km: "))
koszt= dystans*spalanie*cena_paliwa/100


print(f"Koszt przejazdu {miastoA} {miastoB} to ", koszt)

