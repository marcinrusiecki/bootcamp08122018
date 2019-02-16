import sys

if len(sys.argv) != 3:
    print("Brakuje jednego z argumentów: pliku wejściowego, nazwy pliku wyjąsiowego lub modułu")
    exit()

plik_wejsciowy = sys.argv[1]
plik_wyjsciowy = sys.argv[2]

with open(plik_wejsciowy) as f:
    unikalny_email = set()
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            unikalny_email.add(line)

emaile = sorted(unikalny_email)

with open(plik_wyjsciowy, 'w') as f:
    for email in emaile:
        f.write(email + '\n')
    print("Plik wyjsciowy został stworzony")

