from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca Ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca (konstruktor)
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # " Kura dziedziczy po klasie Ptak"
    """Klasa Kura"""

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # obowiazkowe

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    # musimy tą metodę nadpisac w klasie, która dziedziczy
    def wydaj_odglos(self):
        print("ko ko ko ")


class Orzel(Ptak):
    """
    Klasa Orzel
    """

    def wydaj_odglos(self):
        print("Kir kier kir")


# po oznaczeniu jako abstrakcyjna nie da sie tworzyc obiektów kalsy Ptak
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
or2 = Orzel("Orzeł Bielik", 45)
or2.latam()  # Tu Orzeł Bielik Lecę z szybkością 45

# polimorfizm  obiekty różnych klas maja wspolne cechy
lista = [or2, kur2]  # obiekty róznych klas
for i in lista:
    i.wydaj_odglos()
# Kir kier kir
# ko ko ko
