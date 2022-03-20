import pyperclip as pc
from mods.menu import cclogo2
from mods.clearScreen import clear_screen as cs

cs()
print(cclogo2)

mode = input("Enter mode (encrypt / decrypt): ")
message = input("Enter your text: ")
key = int(input("Enter a shift key (1 - 64): "))

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?.,'

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        if mode == 'decrypt':
            translatedIndex = symbolIndex - key
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

pc.copy(translated)
print(f"\n\nYour output is: {translated} \n ... Output copied to clipboard")
input("\n\nPress enter to go back...")