import pyperclip as pc
from mods.menu import cclogo2
from mods.clearScreen import clear_screen as cs

cs()
print(cclogo2)

mode = input("Enter mode (enc / dec): ")
message = input("Enter your text: ")
key = int(input("Enter a shift key (1 - 64): "))

SYMBOLS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

translated = ''

# enc is there just for the sake of it being more understadable
if mode == 'dec':
    key *= -1

for symbol in message:
    symbolIndex = SYMBOLS.index(symbol)

    translatedIndex = symbolIndex + key
    translatedIndex %= len(SYMBOLS)

    translated += SYMBOLS[translatedIndex]

pc.copy(translated)
print(f"\n\nYour output is: \n{translated}\n\n... Output copied to clipboard")
input("\n\nPress enter to go back...")
