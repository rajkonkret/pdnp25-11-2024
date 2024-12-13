# komentarz
# PEP8 - zasady formatowania kodu
# ctrl alt l
import sys
print()  # wypisz/wydrukuj

print("Bartek")
print('Bartek')
# ctrl d powielanie linii

# ctrl / komentraz zazanaczinegoi fragmentu

print("Nazywam się 'Bartek'")

# typ tekstowy - dane umiesczone w cudzysłowach

print(type("Bartek"))  # <class 'str'>

# dane liczbowe
print(26)
print(type(26))  # <class 'int'> liczby całkowite

print(39 + 39)  # 78
print("39" + "39")  # kontaktenacja łaczenie tekstów

print(int("39") + 39)  # rzutowanie na int, 78
print(("39") + str(39))  # rzutowanie na tekst, 3939

# nazwy znienych z małej litery
# typowanie dynamiczne można e zmie aić typy jakie przechowuje zmienna
liczba = 39
print(type(liczba))  # <class 'int'>
print(liczba)  # 39

print(sys.int_info)