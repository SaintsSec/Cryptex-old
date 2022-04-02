from mods.menu import encryptionMenu, exitMessage
from mods.clearScreen import clear_screen as cs

run = True
while run:
    #Clear the screen
    cs()
    #Print the main menu
    print(encryptionMenu)
    #Ask user for input
    menuOption = input("Enter a short code: \n").lower()
    if menuOption == "hex":
        exec(open("CryptexTools/encryption/hex.py").read())
    if menuOption == "b64":
        exec(open("CryptexTools/encryption/base64.py").read())
    if menuOption == "256":
        exec(open("CryptexTools/encryption/256.py").read())
    if menuOption == "cc":
        exec(open("CryptexTools/encryption/caesar.py").read())
    if menuOption == "ogcc":
        exec(open("CryptexTools/encryption/OGCaesar.py").read())
    if menuOption == "ch":
        exec(open("CryptexTools/encryption/caesarHacker.py").read())
    if menuOption == "rc":
        exec(open("CryptexTools/encryption/reverse.py").read())
    if menuOption == "pc":
        exec(open("CryptexTools/encryption/playfair.py").read())    
    if menuOption == "mm":
        exec(open("main.py").read())
    #Option to exit the program
    elif menuOption == "e":
      print(exitMessage)
      exit()
    #Failsafe incase if someone presses a non-menu item
    elif menuOption !="":
      print("\n Not Valid Choice Try again")