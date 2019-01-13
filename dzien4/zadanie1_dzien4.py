
def policz_znaki(napis, start="<", stop=">"):
    poziom = 0
    wynik = 0
    for znak in napis:
        if znak == start:
            poziom += 1
        elif znak == stop:
            poziom -= 1
        elif poziom:
            wynik += poziom
    return wynik


def test_policz_znaki_zerowy_poziom():
    assert policz_znaki("") == 0

def test_policz_znaki_bez_poziomu():
    assert policz_znaki("Ala ma kota") == 0

def test_policz_znaki_pierwszy_poziom():
    assert policz_znaki("Ala <makat> kota") == 5

def test_policz_znaki_drugi2_poziom():
    assert policz_znaki("Ala <makatmama> <ma> kota") == 11

def test_policz_znaki_drugi3_poziom():
    assert policz_znaki("Ala <mak<atm>ama> <ma> kota") == 14
