# warunki - instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if - sterowana awarunkiem
from idlelib.debugger_r import CodeProxy

odp = True
# odp = False
print(bool(odp))
if odp:
    # obowiązkowe 4 spacje
    # wykona się gdy warunek spełniony
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część progrramu")  # niezależna od if instrukcja
# IndentationError: unexpected indent - bład wcięcia
# False
# Dalsza część progrramu
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza część progrramu

odp = "Radek"
print(bool(odp))  # True
print(odp == "Radek")  # == porównanie, True

if odp:
    print("Nie pusty string")

if odp == "Radek":
    print("Radek")
# Nie pusty string
# Radek

if odp == "Tomek":
    print('To jest Tomek')
else:  # w przeciwnym wypadku
    print('To nie jest Tomek')
# To nie jest Tomek

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 30_000:
#     podatek = 0.2
# elif zarobki < 100_000:  # kolejny if
#     podatek = 0.4
# else:
#     podatek = 0.9

# print("Podatek wynosi", podatek * zarobki)
# podatek 0.2 dla dochodów od 10000 do 29999

# napisac aplikację test
# zadać pytanie
# pobrac odpowiedz od uzytkownika
# wypisac wynik

punkty = 0
odp = input("Podaj rok Bitwy pod Grunwaldem")  # str
if odp.strip() == '1410':
    print("Zdałeś")
    punkty += 1  # punkty = punkty + 1
else:
    print("Musisz uczyć się dalej")
# Podaj rok Bitwy pod Grunwaldem1410
# Zdałeś
# Podaj rok Bitwy pod Grunwaldem1000
# Musisz uczyć się dalej
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
print(f"Zdobyłeś {punkty} punkty.")
