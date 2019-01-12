SAMOGLOSKI = ('aeiouy')
samo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y':0}
napis = input("Podaj słowo: ")
male = napis.lower()
dt ={}
for i in SAMOGLOSKI:
    samo[i] = male.count(i)
print(samo)

for y in male:
    if y in ['a','e','i','o','u','y']:
        dt.setdefault(y,0)
        dt[y] +=1
print(dt)




