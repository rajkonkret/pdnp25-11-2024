# słownik - dane typu para klucz-wartość
# {"user" : "Radek", "wiek" :78}
# {"klucz" : "warrtość"}
# {"firstName":"John", "lastName":"Doe"}
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = dict()
print(dictionary)  # {}

dictionary_1 = {}
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

dictionary['wiek'] = "45"
print(dictionary)  # {'imie': 'Radek', 'wiek': '45'}

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': '45'}

print(dictionary.keys())  # dict_keys(['imie', 'wiek']) klucze
print(dictionary.values())  # dict_values(['Tomek', '45']) wartości
print(dictionary.items())  # dict_items([('imie', 'Tomek'), ('wiek', '45')]) pary

# wypisanie elemmentu ze słownika
print(dictionary['imie'])  # Tomek
print(dictionary['wiek'])  # 45

# print(dictionary['Imie'])  # KeyError: 'Imie', brak klucza
print(dictionary.get("Imie"))  # None, gdy nie ma klucza
print(dictionary.get("Imie", 'default'))  # default, gdy nie ma klucza

dictionary.update({"date": "12-12-2024"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': '45', 'date': '12-12-2024'}

dict_small = {"x": 2}
dict_small.update([('y', 3), ("z", 7)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 7}

# input() - pobiera dane od użytkownika
# tekst = input("Podaj imię") # input zwraca <class 'str'>
# print(tekst)
# # Podaj imięRaadek
# # Raadek
# print(type(tekst))

# napisać aplikację kalkulator
# pobrac dwie liczby -> 2 x input
# wypisac wynik dodawanie -> print

# a = int(input("Podaj pierwszą liczbę"))
# b = input("Podaj drugą liczbę")
# print(a + float(b))
# # Podaj pierwszą liczbę6
# # Podaj drugą liczbę8
# # 14.0

# napisac aplikację pol-ang
# słownik ze słowkami i tłuamczeniami
# pobrac od uzytkownika o co pyta -> input
# wyswietlic tłumaczenie -> wartość klucza
pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
print("Mamy takie słówka", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia: ")
# print(pol_ang[odp.lower()])
# # ß - ss
# print(pol_ang[odp.casefold()])
print(f'Tłumaczenie {odp} : {pol_ang.get(odp.casefold().strip(), "Nie mo ;)")}')
# Mamy takie słówka dict_keys(['kot', 'pies', 'dach'])
# Podaj słówko do przetłumaczenia:  Kot
# Tłumaczenie  Kot : cat
#
# Process finished with exit code 0
