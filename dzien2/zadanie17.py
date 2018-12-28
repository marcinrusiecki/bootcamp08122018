lista = []
ilosc_wprowadzen = 0
while ilosc_wprowadzen < 10:
    liczba = int(input("Podaj liczbe: "))
    lista.append(liczba)
    srednia = sum(lista)/len(lista)
    print(srednia)
    ilosc_wprowadzen+=1
print(lista)











