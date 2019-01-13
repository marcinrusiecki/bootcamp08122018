

def test_splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            for el in test_splaszcz(element):
                out.append(el)
        else:
            out.append(element)
    print(out)
    return out




test_splaszcz(([1,2,3,7,[1,9,4,[9,10,[8],7]]]))
