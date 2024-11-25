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
