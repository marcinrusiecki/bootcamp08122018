def porownaj(napis):
    napis = napis.lower().split()
    napis = "".join(napis)
    lewy = 0
    prawy = len(napis)-1
    while prawy >= lewy:
        if not napis[lewy] == napis[prawy]:
            return False
        lewy +=1
        prawy -=1
    return True



#return napis == napis[::-1]

print(porownaj("Kobyła ma m bok")==True)
