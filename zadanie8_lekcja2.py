napis = input("Napisz zdanie zawierające nawias < >: ")

a = napis.index('<')
z = napis.index('>')
k = len(napis[a:z])-1
print(k)


