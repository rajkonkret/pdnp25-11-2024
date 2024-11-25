from itertools import count

tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
# wszystko jest obiektem
# """ Return a copy of the string converted to uppercase. """
tekst.upper()  # nie zmienia orginalnego
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

# zamienic na małe litery
print(tekst.lower())  # witaj świecie
tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie

# Witaj Świecie
# 0123456789012...

print(tekst.count("i"))  # 3 występuje 3 razy
# start 0, stop 4 niewłacznie!
print(tekst.count("j", 0, 4))  # indeksy 0123 -> występuje 0 razy

# testowanie tabnine
print(tekst.find("j"))  # 4
print(tekst.find("j", 7))  # -1, nie ma takiego znaku
print(tekst.find("j", 13))  # -1, nie ma takiego znaku

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", ""))  # "Witaj  Świecie"
print(tekst_zamiana.replace("dobry ", ""))  # "Witaj Świecie"

# strip() - usunie białe znaki, spacje z początku i końća tekstu
print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removeprefix("Witaj").strip())  # "Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "
print(tekst.removesuffix("Świecie").strip())  # "Witaj"
print(tekst.removesuffix("Witaj").strip())  # "Witaj Świecie"

print(tekst[4])  # indeks numer 4, j

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie', b - typ bajtowy
print(type(encode_s))  # <class 'bytes'>
# \xc5\x9a, \x liczba w sytemie szesnastkowym -> \xc5 - 197
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f - fstring - tekst sforamtowany
tekst_format = f"Mam na imię {imie} i lubię pythona"
print(tekst_format)  # Mam na imię Radek i lubię pythona
tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	 Mam na imię Radek
#  i lubię pythona"
# \t tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek! pod %s wstawiona zostanie wartość zmiennej imie

print("Witaj {}".format(imie))  # Witaj Radek

print("Witaj", imie)  # Witaj Radek

print("""
Tekst 
    wielolinijkowy
""")
# "Tekst
#     wielolinijkowy"
# ctrl / - komentarz zaznaczonego fragmentu
