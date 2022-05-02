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
    elif menuOption == "b64":
        exec(open("CryptexTools/encryption/base64.py").read())
    elif menuOption == "256":
        exec(open("CryptexTools/encryption/256.py").read())
    elif menuOption == "cc":
        exec(open("CryptexTools/encryption/caesar.py").read())
    elif menuOption == "ogcc":
        exec(open("CryptexTools/encryption/OGCaesar.py").read())
    elif menuOption == "ch":
        exec(open("CryptexTools/encryption/caesarHacker.py").read())
    elif menuOption == "rc":
        exec(open("CryptexTools/encryption/reverse.py").read())
    elif menuOption == "pc":
        exec(open("CryptexTools/encryption/playfair.py").read()) 
    elif menuOption == "xor":
        exec(open("CryptexTools/encryption/hexor.py").read())  
    elif menuOption == "bin":
        exec(open("CryptexTools/encryption/binary.py").read())  
    elif menuOption == "fe":
        exec(open("CryptexTools/encryption/fileencryption/fileencryption.py").read())
    elif menuOption == "mm":
        exec(open("main.py").read())
    #Option to exit the program
    elif menuOption == "e":
      print(exitMessage)
      exit()
    #Failsafe incase if someone presses a non-menu item
    elif menuOption !="":
      print("\n Not Valid Choice Try again")
