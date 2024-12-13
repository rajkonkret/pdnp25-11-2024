a = 10
b = 10


def dodaj():
    # lokalne zmienne
    a = 7
    b = 8
    print(a + b)


def dodaj2():
    global a
    a = 9  # uzyje globalne a, zmieniamy wartość globalnego
    b = 89
    print(a + b)


def dodaj3():
    print(a + b)


print(f"Wartość a z góry {a=} {b=} (globalne)")  # Wartość a z góry a=10 b=10 (globalne)
dodaj()  # 15
print(f"Wartość a z góry {a=} {b=} (globalne)")  # Wartość a z góry a=10 b=10 (globalne)
dodaj3()  # 20
print(f"Wartość a z góry {a=} {b=} (globalne)")  # Wartość a z góry a=10 b=10 (globalne)
dodaj2()  # 98
print(f"Wartość a z góry {a=} {b=} (globalne)")  # Wartość a z góry a=9 b=10 (globalne)
dodaj3()  # 19
print(f"Wartość a z góry {a=} {b=} (globalne)")  # Wartość a z góry a=9 b=10 (globalne)
