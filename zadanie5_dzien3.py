liczby = [100,2,3,4,5,6,7,8,98,23,43,12,1]



for i in range(len(liczby)):
    index_min = i
    for j in range(i, len(liczby)):
        if liczby[j]<liczby[index_min]:
            index_min = j
    liczby[i], liczby[index_min] = liczby[index_min], liczby[i]

print(liczby)



