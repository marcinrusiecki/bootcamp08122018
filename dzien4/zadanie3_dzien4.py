def wykonaj(operacje, *args):
    print(args)
    return operacje(args)

print(wykonaj(min, 10,20,40))


def napisy(*args):
    return "\n".join(args)

print(napisy("a10","b20","c40"))

def formatowanie(*args, **kwargs):
    wynik = '\\'.join(args)
    print(kwargs)
    for zmienna in kwargs:
        wynik = wynik.replace(f"${zmienna}", kwargs[zmienna])
    return wynik


print(formatowanie(
    'koszt $cena PLN',
    'kwota $cena brutto',
    cena = 10,

))


