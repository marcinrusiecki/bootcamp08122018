def utworz_trojkat(n):
    a = [[1]]
    i = 1

    for i in range(1,n):
        a.append[[1]]
        for j in range(1,i):
            a[i].append[i-1[j-1]+a[a-1][j]]
        a[i].append[i]
    return a

