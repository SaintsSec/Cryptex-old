from mods.menu import reverseLogo
import pyperclip as pc
from mods.clearScreen import clear_screen as cs

cs()
print(reverseLogo)

message = input("What would you like to reverse: \n")
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

pc.copy(translated)
print(translated)
input("The Cipher has been copied: Press enter to go back")