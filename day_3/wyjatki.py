# wyjątki - błędy generowane przez działąnie programu

# print(5 / 0)
# # Traceback (most recent call last):
# #   File "C:\Users\CSComarch\PycharmProjects\pdnp25-11-2024\day_3\wyjatki.py", line 3, in <module>
# #     print(5 / 0)
# #           ~~^~~
# # ZeroDivisionError: division by zero
# print("Dalsza część programu")

try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Brak klucza")
    wynik = 90 / 34
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # tylko gdy nie ma błedu
    print("Wynik", wynik)
finally:
    print("Wykona się zawsze")

print("Dalsza część programu")
# Nie dziel przez zero
# Dalsza część programu
# Bład typu
# Dalsza część programu
# Bład wartości
# Dalsza część programu
# Bład 'Brak klucza'
# Dalsza część programu
# Wynik 2.6470588235294117
# Dalsza część programu
# try - except [else - finally]