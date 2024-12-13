tekst="Witaj dobry swiecie"
print(tekst)
print(type(tekst)) #<class 'str'>

#wszystko jest obietktem
tekst.upper()
print(tekst) #Witaj
print(tekst.upper())

tekst_upper=tekst.upper()
print(tekst_upper)

tekst_lower= tekst.lower()
print(tekst_lower)

print(tekst.count("i"))
print(tekst.count("j",0,4))

tekst_zamiana = "Witaj dobry swiecie"
print(tekst_zamiana.replace("dobry",""))
print(tekst_zamiana.replace("dobry",""))

#strip() usunie białe znaki, z spacje z początku i konca tekstu
print(tekst.removeprefix("Witaj"))
print(tekst.removeprefix("Witaj").strip())
print(tekst.removesuffix("swiecie"))
print(tekst.removesuffix("swiecie").strip())
print(tekst.removesuffix("Witaj").strip())

print(tekst[4])#indeks numer 4,j

encode_s=tekst.encode('utf-8')
print(encode_s)#b'Witaj' typ bajtowy
print(type(encode_s)) #<class 'bytes'>
print(encode_s.decode('utf-8'))#b'Witaj świecie


imie="Bartek"
tekst_format =f"MAm na imie {imie} i lubie"
print(tekst_format)
tekst_format =f"\tMAm na imie {imie}\n i lubie.\b"
print(tekst_format)
#	MAm na imie Bartek
#i lubie
#t tabulator, n nowa linia, b backspace

starszy="Witaj %s!" #Witaj Bartek! pod % zmienna imię wstawiona
print(starszy % imie)