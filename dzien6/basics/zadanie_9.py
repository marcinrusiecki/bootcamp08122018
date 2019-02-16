import date time

current_year = datetime.datetime.now().year

bd_year = int(input("Podaj rok urodzenia: "))

if current_year - bd_year >= 18:
    print("Jesteś pełnoletni. Możesz iśc do pracy")
else:
    print("Możesz bumelować. Rodzice płacą")