x = 0

while x <= 100:
    if x % 10 == 0:
        x += 1
        continue
    print(x**2)
    x += 1