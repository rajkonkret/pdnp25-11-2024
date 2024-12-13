# działania z plikami
# context manager
# with
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:
    fh.write('Powitanie\n')
    fh.write('Drugie\n')
    fh.write('Kolejne\n')

# with open('test.log', "x", encoding='utf-8') as f:
#     f.write("Test\n")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp25-11-2024\day_3\pliki_zad1.py", line 20, in <module>
#     with open('test.log', "x") as f:
#          ~~~~^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: 'test.log'

# "w" - nadpisze istnięjący plik
with open('test.log', 'w', encoding='utf-8') as fh:
    fh.write('NAdpisane\n')

with open("test.log", "a", encoding='utf-8') as file:
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dopisane\n")
    file.write("Dośdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
