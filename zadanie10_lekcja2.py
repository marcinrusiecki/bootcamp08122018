slowo = input("Podaj wyraz: ")
napis = slowo.lower()
alfabet = ["a","b","c","d","e","ą","ę","ć","f","g","h","i","j","k","l","m","n","ń","o","ó","p","r","s","ś","t","u","w","y","z","ź","ż"]

dt = {}

for i in napis:
    if i in alfabet:
        dt.setdefault(i,0)
        dt[i]+=1
print(dt)



