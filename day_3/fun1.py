# funkcje - wydzielony fragment kodu, który można uruchomić w dowolnym momencie
# funkcja musi być najpierw zadeklarowane
# w miejscu deklaracji nic się nie uruchamia
# aby uruchomić funkcję, należy ją wywołać

a = 8
b = 6


# deklaracja funkcji
# PEP8 - dwie linijki odstępu od reszty programu
def dodaj():
    print(a + b)


def dodaj2(a, b):  # dwa obowiązkowe argumenty do przekazania
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# uruchmienie funkcji
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# argumenty przekazywane po pozycji
dodaj2(5, 89)  # 94
odejmij(1, 2)
odejmij(1, 2, 3)
# -1
# -4

# argumenty przelkazywane po nazwie
odejmij(b=9, a=19)
odejmij(b=9, a=19, c=87)
# 10
# -77

# mieszane arg
odejmij(1, c=87, b=12)  # -98

# pozycyjne muszą być przed nazwany
# odejmij(a=5, 2, 3) # SyntaxError: positional argument follows keyword argument

# print zwraca None
# print(dodaj() + odejmij(6, 9))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(dodaj())


# 14
# None

# funkcje zwracające wynik
# konczą sie return - zwróc wynik
#
def dodaj3(a, b):
    return a + b  # zwróć wynik


print(dodaj3(4, 7))  # 11
wyn = dodaj3(5, 8)
print("Wynik", wyn)  # Wynik 13
print(dodaj3(5, 9) + dodaj3(2, 89))  # 105
