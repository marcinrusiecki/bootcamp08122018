import pytest
def silnia(n):
    if n < 0:
        raise ValueError("Argument musi być podany")
    if n >1:
        return n * silnia(n - 1)
    elif n in (0,1):
        return 1





print(silnia(-5))
def test_silnia_0():
    assert silnia(0) == 1
def test_silnia_dla_innej_liczby():
    assert silnia(5) == 120
def test_silnia_dla_ujemnej_liczby():
    with pytest.raises(ValueError) as e:
        silnia(-5)

def dodaj(liczba):
    if liczba ==0:
        return 0
    else:
        return liczba + (liczba -1)

print(dodaj(5))