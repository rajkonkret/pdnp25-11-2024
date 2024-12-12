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
