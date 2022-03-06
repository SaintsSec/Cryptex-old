from mods.menu import crackerMenu, exitMessage
from mods.clearScreen import clear_screen as cs

run = True
while run:
    #Clear the screen
    cs()
    #Print the main menu
    print(crackerMenu)
    #Ask user for input
    menuOption = input("Enter a short code: \n").lower()
    if menuOption == "md5":
        exec(open("CryptexTools/crackers/md5crack.py").read())
    if menuOption == "mm":
        exec(open("main.py").read())
    #Option to exit the program
    elif menuOption == "e":
      print(exitMessage)
      exit()
    #Failsafe incase if someone presses a non-menu item
    elif menuOption !="":
      print("\n Not Valid Choice Try again")
