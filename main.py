from mods.menu import menu, information, exitMessage
from mods.clearScreen import clear_screen as cs
import CryptexTools

run = True
while run:
    #Clear the screen
    cs()
    #Print the main menu
    print(menu)
    #Ask user for input
    menuOption = input("Enter a short code: \n")
    if menuOption == "i":
        print(information)
        input("Press enter to return to main menu")
    if menuOption == "hex":
        exec(open("CryptexTools/hex.py").read())
    if menuOption == "b64":
        exec(open("CryptexTools/base64.py").read())
    if menuOption == "256":
        exec(open("CryptexTools/256.py").read())
    if menuOption == "md5":
        exec(open("CryptexTools/md5crack.py").read())
    if menuOption == "qr":
        exec(open("CryptexTools/QR.py").read())
    if menuOption == "cc":
        exec(open("CryptexTools/caesar.py").read())
    if menuOption == "pg":
        exec(open("CryptexTools/passwordgen.py").read())
    #Option to exit the program
    elif menuOption == "e":
      print(exitMessage)
      exit() 
    #Failsafe incase if someone presses a non-menu item
    elif menuOption !="":
      print("\n Not Valid Choice Try again") 