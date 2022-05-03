from mods.menu import menu, information, exitMessage
from mods.clearScreen import clear_screen as cs

import os 
import sys

# command line interface
def cli(arguments):

    # if arguments exist
    if arguments:
        # TODO: incorporate argument parsing
        print(True)

    else:
        while True:
            #Clear the screen
            cs()
            #Print the main menu
            print(menu)
            #Ask user for input
            menuOption = input("Enter a short code: \n").lower()
            if menuOption == "i":
                cs()
                print(information)
                input("Press enter to return to main menu")
            if menuOption == "enc":
                exec(open("mods/navigation/encryptionMenu.py").read())
            if menuOption == "crack":
                exec(open("mods/navigation/crackerMenu.py").read())
            if menuOption == "misc":
                exec(open("mods/navigation/miscMenu.py").read())
            #Option to exit the program
            elif menuOption == "e":
                print(exitMessage)
                exit()
            #Failsafe incase if someone presses a non-menu item
            elif menuOption !="":
                print("\n Not Valid Choice Try again") 

# main code
def main():
    # clear screen
    # cs()

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    # run command line interface
    cli(arguments_exist)

# run main code
if __name__ == '__main__':
    main()