liczby = [56,3,5,1]
print(liczby)
indeks_min, indeks_max = None, None
temp_max = None
for i, v in enumerate(liczby):
    print(v, "[",i,"]")

index_min = liczby[0]
index_max = liczby[3]
temp_max = index_max
index_min = index_max
temp_max = index_min
print(index_min, index_max)
#assert [1, 3, 5, 56] == liczby



