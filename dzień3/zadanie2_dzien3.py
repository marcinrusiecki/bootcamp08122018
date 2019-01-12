napis = input("Napisz zdanie zawierające nawias < >: ")

a = napis.index('<')
z = napis.index('>')
k = len(napis[a:z])-1
print(k)

licz = False
dlugosc = 0

for znak in napis:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False
        break
    elif licz:
        dlugosc+=1
print(dlugosc)
