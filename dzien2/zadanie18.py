lista = [1,2,3,5,6,432,13,64,23,4,5,79,6,4,2,-23,-1]

dodatnie = 0
ujemne = 0

for i in lista:
    if i > 0:
        dodatnie+=1
    elif i < 0:
        ujemne+=1
print("Licznik dodatnich: ", dodatnie)
print("Licznik ujemnych: ", ujemne)

dodatnie = len([x for x in lista if x > 0])
ujemne = len([x for x in lista if x < 0])

print("Licznik dodatnich: ", dodatnie)
print("Licznik ujemnych: ", ujemne)