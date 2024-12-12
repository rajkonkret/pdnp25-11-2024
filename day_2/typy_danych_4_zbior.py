# zbiór (set) - przechowuje unikalne wartosci
# nie zachowuje kolejności przy dodawaniu elementów
# nie ma indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamimana na zbior, set
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# utworzenie pustego zbioru
zb2 = set()
print(zb2)  # set()

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop()
print(zbior.pop())  # 33, pierwszy element

zbior_copy = zbior.copy()
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
print(zbior_copy)  # {66, 18, 22, 24, 777, 11, 44}
print(id(zbior))
print(id(zbior_copy))
# 3143691191456
# 3143691475136

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - nowy zbiór
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {24, 777, 66, 22}
print(zbior.difference(zbior_2))  # {24, 777, 66, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

# modyfikuje zbiór bazowy
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

print(999 in zbior)  # True

print(sorted(zbior))  # zwraca listę, nie zmieni zbioru
# [11, 12.34, 18, 22, 24, 44, 52, 62, 66, 667, 777, 999]
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
