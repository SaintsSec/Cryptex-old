from mods.menu import miscMenu, exitMessage
from mods.clearScreen import clear_screen as cs

run = True
while run:
    #Clear the screen
    cs()
    #Print the main menu
    print(miscMenu)
    #Ask user for input
    menuOption = input("Enter a short code: \n").lower()
    if menuOption == "pg":
        exec(open("CryptexTools/misc/passwordgen.py").read())
    if menuOption == "qr":
        exec(open("CryptexTools/misc/QR.py").read())
    if menuOption == "mm":
        exec(open("main.py").read())
    #Option to exit the program
    elif menuOption == "e":
      print(exitMessage)
      exit()
    #Failsafe incase if someone presses a non-menu item
    elif menuOption !="":
      print("\n Not Valid Choice Try again")