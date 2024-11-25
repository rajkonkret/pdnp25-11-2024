# komentarz
# PEP8 - zasady formatowania kodu
# ctrl alt l
import sys

print()  # wypisz/wydrukuj - pusta linia

print("Nazywam się Radek")
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d  powielanie linii
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# ctrl / - komentarz zaznaczonego fragmentu
# komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\pdnp25-11-2024\day_1\pierwszy.py", line 20
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 20)
# język interpretowany - tłumaczony przy każdym uruchomieniu na jezyk maszynowy znany procesorowi

print("Nazywam się 'Radek'")  # Nazywam się 'Radek'

# typ tekstowy - dane umieszczone w cudzysłowiach
# type() - sprawdzenie typu
print(type("Radek"))  # <class 'str'>, string, tekstowe
print("39")
print(type("39"))  # <class 'str'>, nadal tekstowe

# dane liczbowe
print(39)
print(type(39))  # <class 'int'>, integer, liczby całkowite

print(39 + 39)  # 78
print("39" + "39")  # 3939, konkatenacja, łaczenie tekstów

# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
# Process finished with exit code 1 - oznacza błąd

# jawnie musimy wskazac
print(int("39") + 39)  # int() - rzutowanie na int, 78
print("39" + str(39))  # str() - rzutowanie (zamiana) na tekst, 3939

print("Radek: " + str(39))  # Radek: 39

print(5 * "4")  # 44444
print(160 * 35)
print("160" * 35)
# 5600
# 160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160

# zmienna - pudełko na dane
# nazwy zmiennych z małej litery
# snake_case
# nazwa zmiennej powinna wskazywać co przechowuje

# typowanie dynamiczne - mozna zmieniac typy jakie przechowuje zmienna
liczba = 39
print(type(liczba))  # <class 'int'>
print(liczba)  # 39

liczba = "Radek"
print(liczba)
print(type(liczba))
# Radek
# <class 'str'>

name: str = "Radek"
print(name)
print(type(name))
# Radek
# <class 'str'>

name = 90
print(name)
print(type(name))
# 90
# <class 'int'>

age = 38
print(age)
print(type(age))

print(sys.int_info)
# ALT f7 - pokazuje uzycie danej funkcji
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)
