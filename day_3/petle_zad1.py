# pętle - możliwość wykonania tego samego kodu wielokrotnie
# for - pętla iteracyjna
import random  # do działań na liczbach pseudolosowych

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(1000):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("To jest pętla")
    # print(_)

print(random.randint(1, 100))  # od 1 do 100
print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(6))  # od 0 do 5
print(random.random())  # 0.7939280418518934, float od 0 do 0,9999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # 42

lista_kule = list(range(1, 50))
print(lista_kule)

lista_wylosowona = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wylosowona.append(wyn)

print(lista_wylosowona)  # [26, 28, 7, 12, 47, 4]

print(random.choices(lista_kule, k=6))  # [16, 41, 16, 13, 9, 18] losuje z powtórzeniami
print(random.sample(lista_kule, k=6))  # [44, 4, 45, 12, 47, 9] losuje unikalne

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowona:
    if c > 10:
        print("Większe od 10")
    else:
        print("Mniejsze lub równe od 10")
# Większe od 10
# Mniejsze lub równe od 10
# Większe od 10
# Większe od 10
# Większe od 10
# Większe od 10

dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}  # słownik

# wyswietli klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyswietlic wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# pary
for i in dictionary.items():
    print(i)
    # ('imie', 'Radek')
    # ('nazwisko', 'Kowalski')

# k, v = ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
