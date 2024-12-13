# klasa - szablon, przepis
# cechy i funkcje
# obiekt - zbudowany wg przepisu
# klasa musi byc najpierw zadekalrowana
# budowanie obiektu klasy uruchamia metode inicjalizujaca
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja


class Human:
    """
    Klasa Human w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


print(Human.__doc__)  # Klasa Human w pythonie
cz1 = Human()  # tworzenie obiektu klasy
print(cz1)  # <__main__.Human object at 0x00000258B7576900>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.imie = "Anna"
cz1.wiek = 27
print(cz1.imie)  # Anna
print(cz1.wiek)  # 27
print(cz1.plec)  # k
# Anna
# 27
# k

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 45
cz2.plec = "m"
print(cz2.imie)  # Anna
print(cz2.wiek)  # 27
print(cz2.plec)
# Radek
# 45
# m
