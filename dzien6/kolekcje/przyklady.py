# napis = "abcdabcde"
#
# for litera in napis:
#     print(litera)
#
# for i in range(len(napis)):
#     print(napis[i])
#
# print(dir(napis))
# print(napis.endswith('cdef'))
# print("abcd" in napis)
# print(napis.upper())
#
# # instrukcja = input("co ma zrobić? [k] by zakończyć")
# # if instrukcja.lower() == 'k':
# #     print("Zakończyłem")
#
# napis2 = "ala ma kota"
# print(napis2.capitalize())
# title = napis2.title()
# print(title.istitle())
# print(napis2.istitle())
#
# print(help(napis2.istitle))
#
#
# # Słownik
#
# # pusty słownik:
# d = dict()
#
# print(type(d))
# d['a'] = 1
# d['b'] = 2
# print(d)
# print(dir(d))
# print(d.keys())
# print(d.values())
# print(d.items())
#
#
# slownik = {
#     'parametr1': 10,
#     'parametr2': 20,
#     'x': 3
# }
#
# print(slownik)
#
# slownik2 = dict(a=1, b=2)
# print(slownik2)
#
# for k, v in slownik.items():
#     print(k, v)
#
#
# for k in slownik:
#     print(k, slownik[k])
#
#
liczby = [9, 2, 6, 8, 4, 3, 1, 0]

for i in range(len(liczby)):
    for j in range(i, len(liczby)):
        print(j, liczby[j])
    print("-"*10)
