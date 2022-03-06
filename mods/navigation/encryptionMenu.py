from mods.menu import encryptionMenu, exitMessage
from mods.clearScreen import clear_screen as cs
import CryptexTools

run = True
while run:
    #Clear the screen
    cs()
    #Print the main menu
    print(encryptionMenu)
    #Ask user for input
    menuOption = input("Enter a short code: \n")
    if menuOption == "hex":
        exec(open("CryptexTools/encryption/hex.py").read())
    if menuOption == "b64":
        exec(open("CryptexTools/encryption/b64.py").read())
    if menuOption == "256":
        exec(open("CryptexTools/encryption/256.py").read())
    if menuOption == "cc":
        exec(open("CryptexTools/encryption/caesar.py").read())
    if menuOption == "mm":
        exec(open("main.py").read())
    #Option to exit the program
    elif menuOption == "e":
      print(exitMessage)
      exit() 
    #Failsafe incase if someone presses a non-menu item
    elif menuOption !="":
      print("\n Not Valid Choice Try again") 