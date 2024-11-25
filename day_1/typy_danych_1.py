import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))
# 36.6
# <class 'float'>

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788 wynik float

print(rok // wiek)  # cześć całkowita 43
print(rok % wiek)  # modulo, reszta z dzielenia, wynik 3
print(10 % 3)  # wynik 1, bo 10 / 3 to 3 całe i 1 reszty

print(wiek ** rok)  # potęgowanie

# len() - długosc zbioru
print(len(str(wiek ** rok)))  # 3385 długość liczby
# print(len(str(wiek ** rok ** 2))) #
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
print(1 / 3)  # 0.3333333333333333

print(54 - 5 * 43 + 8 / 2 + 8 / 2)  # -153.0
print(54 - 5 * 43 + (8 / 2 + 8) / 2)  # -155.0

# liczby float mają bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004

#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# najbliższe przybliżenie
# przechowywane są w postaci wykłądniczej
# 1.23 x 2 ^ 34
# decimal - pozwala ominać problem zaokrągleń
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15, mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")
# Sprawdzenie zmiennej 36.6 47

print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda fałsz
# True False - z dużej litery
# 1 - prawda, 0 - fałsz

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, typ logiczny

print(int(True))  # 1
print(int(False))  # 0

# bool() - zamiana na typ logiczny
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False, None - nic, stan nieokreślony, nie wiem -> null

# działania logiczne
# and -> i
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False

print(True and False)  # Faalse
print(True and True)  # True

# or - lub
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
print(True or False)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

a = 8
b = 6
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 8 <= 6 = False
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 8 >= 6 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 8 >= 6 = True
print(f"Porównanie {a} >= {b} = {a >= b = }")  # Porównanie 8 >= 6 = a >= b = True
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie         Porównanie 8 == 6 = False
print(f"Porównanie {a} != {b} = {a != b}")  # czy rózne          Porównanie 8 != 6 = True
# czy a równa się b?
print(a == b)  # False
print(f"{a==b = }")  # a==b = False
