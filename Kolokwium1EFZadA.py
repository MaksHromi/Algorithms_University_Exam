Najmniejsza_liczba = 0

liczba = int(input("wpisz liczbe - "))

while liczba != 0:
    if liczba > Najmniejsza_liczba:
        Najmniejsza_liczba = liczba
    print(liczba)
    liczba = int(input("wpisz liczbe: "))

print("Najmniejsza liczba to -", Najmniejsza_liczba)
