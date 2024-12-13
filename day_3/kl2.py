class Human:
    """
    Klasa Human
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Mam na imię", self.imie)


cz1 = Human("Anna", 27, 168)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Anna
# 27
# 168
# k

cz2 = Human("Radek", 45, 190, "m")
print(cz2.imie)
print(cz2.wiek)
print(cz2.wzrost)
print(cz2.plec)
# Radek
# 45
# 190
# m
cz2.powitanie()
cz1.powitanie()
# Mam na imię Radek
# Mam na imię Anna
