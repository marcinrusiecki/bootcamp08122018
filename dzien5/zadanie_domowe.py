def z_dwoch(a,b):
    if a>b:
        return a
    else:
        return b


def max(x, y, z):
    return z_dwoch(x,z_dwoch(y,z))

print(max(3,5,2))