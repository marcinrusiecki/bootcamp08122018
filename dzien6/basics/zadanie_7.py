# Napisz program sprawdzajacy czy podana przez uzytkownika liczba
# # jest podzielna przez 2, podzielna przez 3 i wieksza od 10 lub jest to
# # liczba 7.
# # ctr + alt + L - pep8
# ctr + /

liczba = int(input("Podaj liczbę: "))

wynik = (liczba == 7) or (liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10)
