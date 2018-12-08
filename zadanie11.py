pozycja_x = int(input("Podaj pozycję gracza X: "))
pozycja_y = int(input("Podaj pozycję gracza Y: "))

if (pozycja_x < 0 or pozycja_y < 0) or (pozycja_x > 100 or pozycja_y > 100):
    print("Jesteś poza planszą")
elif (pozycja_x > 0 and pozycja_x < 10) and (pozycja_y > 0 and pozycja_y <= 10):
    print("Jesteś w lewym dolnym rogu")
elif (pozycja_x > 10 and pozycja_x < 90) and (pozycja_y > 0 and pozycja_y <= 10):
    print("Jesteś w dolnej krawędzi")
elif (pozycja_x > 90 and pozycja_x < 100) and (pozycja_y > 0 and pozycja_y <= 10):
    print("Jesteś w dolnym prawym rogu")
elif (pozycja_x > 0 and pozycja_x < 10) and (pozycja_y > 10 and pozycja_y <= 90):
    print("Jesteś w lewej krawedzi")
elif (pozycja_x > 0 and pozycja_x < 10) and (pozycja_y > 90 and pozycja_y <= 100):
    print("Jesteś w lewym górnym rogu")
elif (pozycja_x > 10 and pozycja_x < 90) and (pozycja_y > 90 and pozycja_y <= 100):
    print("Jesteś w górnej krawędzi")
elif (pozycja_x > 90 and pozycja_x < 100) and (pozycja_y > 90 and pozycja_y <= 100):
    print("Jesteś w prawym górnym rogu")
elif (pozycja_x > 90 and pozycja_x < 100) and (pozycja_y > 10 and pozycja_y <= 90):
    print("Jesteś w prawej krawedzi")
else:
    print("Jesteś w centrum")