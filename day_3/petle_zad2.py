# while  - pętla sterowana warunkiem

# pętla nieskońćzona
# while True:
#     print("komuniakt !!!")


licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("komunikat 2 !!!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

lista = []
lista_int = []
#     A string is numeric if all characters in the string are numeric
# while True:
#     wej = input("Podaj liczbę")  # str
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))

print(lista)  # ['1', '2', '3', '4', '5']
print(lista_int)  # [5, 6, 7]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
# ctrl alt l
print(5 in my_list)
while 5 in my_list:
    my_list.remove(5)

print(my_list)
# True
# [1, 2, 3, 4, 6]