mniejsza_liczba = float('inf')
pozycja = -1

array = []

for _ in range(10):
    number = int(input("Wpisz liczbe"))
    array.append(number)

mniejsza_liczba = min(array)
pozycja = array.index(mniejsza_liczba)

print("mniejsza_liczba : ", mniejsza_liczba)
print("pozycja:", pozycja)