user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001  # <class 'float'>
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 5678907654321  # int

print("Witaj %s, masz teraz %d lat" % (user, wiek))  # Witaj Tomek, masz teraz 39 lat
# %d: formatowanie liczb całkowitych
# %f: formatowanie liczb zmiennoprzecinkowych
# %s - łańcuch znaków (string)

# sprawdza typy
# print("Witaj %d, masz teraz %s lat" % (user, wiek))
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp25-11-2024\day_1\formaty.py", line 12, in <module>
#     print("Witaj %d, masz teraz %s lat" % (user, wiek))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
# TypeError: %d format: a real number is required, not str

print("Witaj %(user)s, Lubię Cię %(user)s" % {"user": user})
# Witaj Tomek, Lubię Cię Tomek

print("Witaj {}, masz teraz {} lat.".format(user, wiek))
# Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring, tekst sformatowany

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4, zaokraglił
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4
# zaokrągla do wyswietlania
wynik = 3.8765
print("Wynik = %.2f" % wynik)  # Wynik = 3.88
print("Wynik nadal nie zmieniony", wynik)  # Wynik nadal nie zmieniony 3.8765

print(f"Uzywamy wersji pythona {wersja}")  # Uzywamy wersji pythona 3.90001
print(f"Uzywamy wersji pythona {wersja:.1f}")  # Uzywamy wersji pythona 3.9
print(f"Uzywamy wersji pythona {wersja:.2f}")  # Uzywamy wersji pythona 3.90
print(f"Uzywamy wersji pythona {wersja:.0f}")  # Uzywamy wersji pythona 4
print(f"Uzywamy wersji pythona {wersja:.f}")  # ValueError: Format specifier missing precision
