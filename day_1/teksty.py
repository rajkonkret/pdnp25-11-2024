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

print(tekst[4]) # indeks numer 4

