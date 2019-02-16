import datetime

# przykłady input

# x = int(input("Podaj wartość x: "))
# y = int(input("Podaj wartość y: "))
#
# print("Suma: ", x + y)

# Przykłady wartości logiczne
# operatory porównania
# ==, <, >, <=, >=,!=

x = 2
y = 5

print(x > 1 or y > 1)
# print(True or True)
print(True)
print(x > 1 and y < 3)
print(not True)

year = datetime.datetime.now().year

print(2010 < year)

# i = 0
# while True:
#     komenda = input("Podaj komendę: ")
#     if komenda == "koniec":
#         break
#     if komenda == 'dodaj':
#         a = int(input("Podaj a:"))
#         b = int(input("Podaj b:"))
#         print(a+b)
#     if komenda == "zmien i":
#         i = 1


# Napisy

tekst = "Ala ma kota"
        #012345678910
i=0
while i < len(tekst):
    print(tekst[i])
    i += 1

for litera in tekst:
    print(litera)

for i, litera in enumerate(tekst):
    print(i, litera)

for i in range(10):
    print(i)


krotka = (1, 2, 3,1, 1, 1)
print(type(krotka))
print(krotka)
print(krotka[0])


for el in krotka:
    print(el)

print(dir(krotka))
print(krotka.count(1))

krotka2 = ("Napis 1", "Napis 2", "Napis 1", 1, 2, 3)
print(krotka2.index("Napis 1"))
print(krotka2.count("Napis 1"))

print(type(()))

krotka = tuple()

x = "aaa"
y = x
print(id(x))
print(id(y))
x = x + "a"
print(id(x))
print(id(y))

x = (1,2,6,7,8,9,10)
x = x + (1,)
print(x)

# listy

lista = [1,3,5,7,9,2,4,6,8]
print(type(lista))
print(lista[1:5])
print(dir(lista))

print(lista)
print(id(lista))
lista.append("AA")
print(lista)
print(id(lista))
lista.extend(['a', 'b'])
print(lista)
lista.append(['a', 'b'])
print(lista)
print(lista[-1][-1])
print(" Jak działa pop")
print(lista)
print(lista.pop())
print(lista)

# print([].pop())
lista = [1,5,2,7,4,9]
print(lista)
print("Sortowanie")
posortowane = sorted(lista)
print("posortowane", posortowane)
print(lista.sort())
print(lista)

len(lista)
sum(lista)