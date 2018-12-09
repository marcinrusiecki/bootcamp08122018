from random import randint

#losujemy pozycje gracza

gracz_x = randint(1,10)
gracz_y = randint(1,10)

#losujemy pozycje skarbu

skarb_x = randint(1,10)
skarb_y = randint(1,10)

min_liczba_krokow = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
liczba_krokow = 0
DEBUG = True

while True:
    min_liczba_krokow_prze_ruchem = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    print (f"Twoja pozycja to:  {gracz_x} {gracz_y}")

    if DEBUG:
        print(f"Pozycja skarbu to:  {skarb_x} {skarb_y}")
        print(f"Minimalna liczba krokow: ", min_liczba_krokow)
        print(f"Liczba krokow: ", liczba_krokow)
    kierunek = input("Podaj kierunek w-gora, s-dol, a-lewo, d-prawo")
    if kierunek == "w":
        gracz_y +=1
    elif kierunek == "s":
        gracz_y -=1
    elif kierunek == "a":
        gracz_x -=1
    elif kierunek == "d":
        gracz_x +=1
    liczba_krokow += 1

    min_liczba_krokow_po_ruchu = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    if gracz_x <1 or gracz_x >10 or gracz_y <1 or gracz_y >10:
        print("Przegrałeś")
        break
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print("Wygrałeś")
        print("Minimalna liczba kroków wynosiła: ", min_liczba_krokow)
        break


    los = randint(1,5)
    if los!=5:
        if min_liczba_krokow_po_ruchu < min_liczba_krokow_prze_ruchem:
            print("Ciepło")
        else:
            print("Zimno")

    if liczba_krokow >= min_liczba_krokow * 2:
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        liczba_krokow = 0
        min_liczba_krokow = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        print("Przekroczyles maksymalną ilość kroków. Skarb zmienił położenie")





