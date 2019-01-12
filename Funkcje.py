
def odpowiedz(odp):
    while odp not in ['t', 'y']:
        odp = input("Odpowiedz t lub y: ")
    return odp


pytanie = odpowiedz(input("Odpowiedz na pytanie t lub n: "))
print(pytanie)




