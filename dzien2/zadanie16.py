tupla = (1,2,3,4,5,6,7,8,9,10)
print(tupla[1])
print(tupla[-2])
print(tupla[2:7])
print(tupla[::3])
print(tupla[::-2])
print(len(tupla))

lista = [1,2,3,4,5,6,7,8]
print(type(lista))
print(dir(lista))

lista.append("AA")
print(lista)
lista.extend(["AA", "BB"])
print(lista)