ILE_DNI = 7

temp = 0
i = 0
while i <= ILE_DNI:

    komenda = input("Podaj temperaturę jaka była w dniu 1 lub zakoncz k ")
    if komenda == "k":
        break
    temp_i = float(komenda)
    temp += temp_i
    i += 1
print("średnia wynosi: ", temp/i)










