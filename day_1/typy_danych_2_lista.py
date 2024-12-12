# kolekcje
#  mogą przechowywać wilele elementów, różnego typu na raz
# Lista - przechowuje dowolna ilośc elelmentów, róznego rodzaju na raz
# zachowuje kolejność przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie elementów do listy
lista.append("Radek")
lista.append("Grzegorz")
lista.append("Maciek")
lista.append("Marek")
lista.append("Zośka")
lista.append("Zenek")
lista.append("Dariusz")

print(lista)
# ['Radek', 'Grzegorz', 'Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz']
#     0          1          2        3         4       5          6  - indeksy
#     -7         -6         -5       -4        -3     -2         -1
print(lista[0])  # Radek, numer indeksu
print(lista[2])  # Maciek
print(lista[4])  # Zośka
# ctrl alt l - formatowanie zgodne z PEP8

print(len(lista))  # len() - długość listy, 7
# print(lista[7])  # IndexError: list index out of range

print(lista[len(lista) - 1])  # Dariusz
print(lista[-1])
print(lista[-2])
print(lista[-3])
# Dariusz
# Zenek
# Zośka

# ['Radek', 'Grzegorz', 'Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz']
#     0          1          2        3         4       5          6  - indeksy
#     -7         -6         -5       -4        -3     -2         -1
# wyswietlanie fragmentu listy (slicowanie)
print(lista[0:3])  # [start:stop], ['Radek', 'Grzegorz', 'Maciek'] -> indeksy 0 1 2
print(lista[:3])  # [start:stop], ['Radek', 'Grzegorz', 'Maciek'] -> 0 1 2
print(lista[2:5])  # -> 234 ['Maciek', 'Marek', 'Zośka']
print(lista[2:])  # ['Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz'] -> 2 3 4 5 6
print(lista[2:6])  # 2345, ['Maciek', 'Marek', 'Zośka', 'Zenek']

print(lista[2:10])  # ['Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz']
print(lista[10:20])  # [] pusta lista
print(lista[2:2])  # []
print(lista[2:3])  # ['Maciek']
print(lista[:])  # ['Radek', 'Grzegorz', 'Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz']

# ['Radek', 'Grzegorz', 'Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz']
#     0          1          2        3         4       5          6  - indeksy
#     -7         -6         -5       -4        -3     -2         -1
print(lista[-2:0])  # [5:0] -> []
print(lista[0:-2])  # [0:5] ['Radek', 'Grzegorz', 'Maciek', 'Marek', 'Zośka']
print(lista[-6:-2])  # ['Grzegorz', 'Maciek', 'Marek', 'Zośka']

print(lista[-1])  # Dariusz

lista_15 = list(range(15))  # 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [start:stop:krok] co druga
# [0, 2, 4, 6, 8, 10, 12, 14]

print(list(range(0, 15, 2)))  # od 0 do 14 co drugą [0, 2, 4, 6, 8, 10, 12, 14] start, stop, krok
print(lista_15[-10])  # 5

# nadpisanie elementu
print(lista)  # ['Radek', 'Grzegorz', 'Maciek', 'Marek', 'Zośka', 'Zenek', 'Dariusz']
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Grzegorz', 'Maciek', 'Mikołaj', 'Zośka', 'Zenek', 'Dariusz']

# dopisanie lementu do listy we wskazanym indeksie
lista.insert(1, "Marek")
print(lista)  # ['Radek', 'Marek', 'Grzegorz', 'Maciek', 'Mikołaj', 'Zośka', 'Zenek', 'Dariusz']

# sprawdzenie indeksu dla elementu, pierwsze wystąpienie
print(lista.index("Zenek"))  # indeks numer 6

# usunięcie elemntu z listy, pierwsze wystąpienie
lista.append("Zenek")  # dodanie na końcu
print(lista)
# ['Radek', 'Marek', 'Grzegorz', 'Maciek', 'Mikołaj', 'Zośka', 'Zenek', 'Dariusz', 'Zenek']
lista.remove("Zenek")  # remove() - usnięcie Zenek,
print(lista)  # ['Radek', 'Marek', 'Grzegorz', 'Maciek', 'Mikołaj', 'Zośka', 'Dariusz', 'Zenek']

# usunięcie z listy po indeksie, zwraca co usunęło
print(lista.pop(5))  # Zośka
print(lista)
# ['Radek', 'Marek', 'Grzegorz', 'Maciek', 'Mikołaj', 'Dariusz', 'Zenek']
print(lista.pop(-2))  # Dariusz
print(lista.pop())  # Zenek, ostatni element
print(lista)  # ['Radek', 'Marek', 'Grzegorz', 'Maciek', 'Mikołaj']
