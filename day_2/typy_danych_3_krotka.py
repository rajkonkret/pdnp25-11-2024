# krotka, tuple - kolekcja do tylko do odczytu
# kolekcja niemutowalna
# pozwala lepiej zarządzać pamięcią
# krotka jednoelementowa - stała - zmienna

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla1 = ("Radek")
print(type(tupla1))  # <class 'str'>

tupla2 = "Radek",
print(type(tupla2))  # <class 'tuple'>

# PEP8 zaleca aby uzywac () w tuplach jednoelementowych
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna
# tupla_liczby[2] = 123 # TypeError: 'tuple' object does not support item assignment

tupla_imiona = "Radek", "Tomek", "Zenek", "Marcin", "Jacek", "Ania", "Zosia"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Jacek', 'Ania', 'Zosia')
print(type(tupla_imiona))  # <class 'tuple'>

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Ania"))  # występuje 1 raz

print(len(tupla_imiona))  # długosc 7

# sortowanie zwróci nową liste, nie zmieni krotki
print(sorted(tupla_imiona))  # ['Ania', 'Jacek', 'Marcin', 'Radek', 'Tomek', 'Zenek', 'Zosia']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Jacek', 'Ania', 'Zosia')

# rozpakowanie krotki
tup = 1, 2
a, b = 1, 2
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2
# a,b = tupla_imiona  # ValueError: too many values to unpack (expected 2)
a, *b = tupla_imiona
print(a, b)  # Radek ['Tomek', 'Zenek', 'Marcin', 'Jacek', 'Ania', 'Zosia']

# name1, name2, name3 = tupla_imiona
*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek', 'Marcin', 'Jacek'] Ania Zosia

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Marcin', 'Jacek', 'Ania'] Zosia

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Marcin', 'Jacek', 'Ania', 'Zosia']

liczby_michal = 1, 2, 3
a, b, c, *d = liczby_michal
print(a, b, c, d)  # 1 2 3 []

lista = list(tupla_liczby)
print(lista)  # [43, 55, 22.34, 11, 200]

print(200 in lista)  # True
