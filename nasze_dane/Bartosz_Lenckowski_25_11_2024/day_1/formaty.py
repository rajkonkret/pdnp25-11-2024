user = "Tomek"
wiek = 39
wersja = 3.900
print(type(wersja))
liczba = 56888888888
print("Witaj %s, masz teraz %d lat" % (user, wiek))


print("Używamy wersji pythona %i" % 3)#Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)#Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)#Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)#Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)#Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)#Używamy wersji pythona 4
#zaokrągla do wyświetlania

wynik=3.876
print("Wynik= %.2f " %wynik)
print("Wynik bez zmian", wynik)


user="Tomek"
print(f"{user:>10}")
print(f"{user:>15}")
print(f"{user:>20}")

print (liczba)
print(f" Nasza liczba {liczba:,}")
print(f" Nasza liczba {liczba:_}")
print(f" Nasza liczba {liczba:_}".replace("_","."))
print(f" Nasza liczba {liczba:_}".replace("_"," "))


