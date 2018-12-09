x = range(101)
licznik = 0
for n in x:
    if n % 3 == 0 or n % 5 == 0:
        licznik +=1
        print("Liczby podzielne przez 3 lub 5 to: ", n )
        print(" W przedziale 0-100 jest ", licznik)