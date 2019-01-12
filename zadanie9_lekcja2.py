towary = {'jabłko':10, 'gruszki':5, 'papryka':7}


k = None
j = towary['jabłko']
g = towary['gruszki']
p = towary['papryka']

print("""
Towary w sklepie:
1 - jabłka
2 - gruszki
3 - papryka
""")

towar = int(input("Wybierz towar z listy: "))
waga = float(input("Podaj wagę w kg: "))

if towar == 1:
    k = j * waga
    print(k)

elif towar == 2:
    k = g * waga
    print(k)
elif towar == 3:
    k = p * waga
    print(k)
else:
    print("Brak towaru w sklepie")





