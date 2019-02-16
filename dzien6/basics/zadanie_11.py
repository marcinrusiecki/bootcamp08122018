x = int(input("Podaj X: "))
y = int(input("Podaj Y: "))

# czy jest poza planszą
if x < 0 or x > 100 or y < 0 or y > 100:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w górnym prawym rogu")
elif x > 90 and y < 10:
    print("Jesteś w dolnym prawym rogu")
elif x < 10 and y < 10:
    print("Jesteś w dolnym lewym rogu")
elif x < 10 and y > 90:
    print("Jesteś w górnym lewym rogu")
elif x < 10:
    print("Jesteś na lewej krawędzi")
elif x > 90:
    print("Jesteś na prawej krawędzi")
elif y < 10:
    print("Jesteś na dolnej krawędzi")
elif y > 90:
    print("Jesteś na górnej krawędzi")
else:
    print("Jesteś w centrum!")
