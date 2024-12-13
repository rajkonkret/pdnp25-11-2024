# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(45, 90))  # -45
odejmij2 = lambda a, b: a - b
print(odejmij2(45, 78))  # -33

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 10, 20, 30, 100, 200, 500]

print([i * 2 for i in lista])
# [2, 4, 6, 20, 40, 60, 200, 400, 1000]

lista_wyn = []


def zmien(x):
    return x * 2


for i in lista:
    lista_wyn.append(zmien(i))
print(lista_wyn)  # [2, 4, 6, 20, 40, 60, 200, 400, 1000]

# map() - mapowanie danych, zmiana danych wg zadanej funkcji
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [2, 4, 6, 20, 40, 60, 200, 400, 1000]

# Lambda jako funkcja anonimowa - wykonanie w miejscu dekalracji
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 5, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 12, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x / 2, lista))}")
# Zastosowanie map() [2, 4, 6, 20, 40, 60, 200, 400, 1000]
# Zastosowanie map() [4, 8, 12, 40, 80, 120, 400, 800, 2000]
# Zastosowanie map() [5, 10, 15, 50, 100, 150, 500, 1000, 2500]
# Zastosowanie map() [12, 24, 36, 120, 240, 360, 1200, 2400, 6000]
# Zastosowanie map() [0.5, 1.0, 1.5, 5.0, 10.0, 15.0, 50.0, 100.0, 250.0]

# filtrowanie danych
# filter() - zwraca elementy spełniające warunek zadany funkcją
# funkcje wyzszego rzedu
print(f"Zastosowanie filter {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter [1, 2]
print(f"Zastosowanie filter {list(filter(lambda x: x > 20, lista))}")
print(f"Zastosowanie filter {list(filter(lambda x: x > 20 and x < 200, lista))}")
print(f"Zastosowanie filter {list(filter(lambda x: 20 < x < 200, lista))}")
# Zastosowanie filter [1, 2]
# Zastosowanie filter [30, 100, 200, 500]
# Zastosowanie filter [30, 100]
# Zastosowanie filter [30, 100]
