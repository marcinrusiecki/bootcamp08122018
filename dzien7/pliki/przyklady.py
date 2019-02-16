import sys

try:
    print(sys.argv)
except IndexError:
    print("Podaj nazwę pliku")
    exit()
print("Sciezka do pliku to:", sys.argv[1])

with open(sys.argv[1]) as f:

    for i, line in enumerate(f):
        print(i, line)


import sys

try:
    with open("readme.txt") as f:
        for i in enumerate(f):
            print(i)
except IOError:
    print("Nie można otworzyć pliku")

