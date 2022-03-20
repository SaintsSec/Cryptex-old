from libs.crackers import crackMD5 as md5
from mods.menu import md5Logo, exitMessage
from mods.clearScreen import clear_screen as cs

cs()
print(md5Logo)

md5()

def menu():
    menuOption = input("\n\nwould you like to go again: \ntype 'yes' to start over, 'mm' to return to main menu or 'e' to exit\nwhat would you liked to do: ")
    if menuOption == "yes":
        exec(open("CryptexTools/md5crack.py").read())
    if menuOption == "mm":
        exec(open("main.py").read())
    if menuOption == "e":
        print(exitMessage)
        exit()
menu()