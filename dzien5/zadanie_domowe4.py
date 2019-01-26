def pangram(napis):
    napis = napis.lower().split()
    napis = "".join(napis)
    alfabet = "pchnąćwtęłódźjeżalubośmskrzyńfig"
    if set(napis) == set(alfabet):
        return True
    else:
        return False




print(pangram("Pchnąć w tę łódź jeża lub ośm skrzyń fig"))