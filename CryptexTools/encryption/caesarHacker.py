from mods.menu import chackerLogo
from mods.clearScreen import clear_screen as cs

cs()
print(chackerLogo)

message = input("What would you like to decrypt: \n")
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?.,'

for key in range(len(symbols)):
    translated = ''
    for symbol in message:
        if symbol in symbols:
            symbolIndex = symbols.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(symbols)
            translated = translated + symbols[translatedIndex]
        else:
          translated = translated + symbol
    print('key #%s: %s' % (key, translated))
input("\npress enter to go back...")