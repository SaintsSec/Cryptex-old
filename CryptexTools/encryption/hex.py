from mods.menu import hexMenu, exitMessage
from mods.clearScreen import clear_screen as cs
from libs.encryption import hexEncrypt, hexDecrypt

ans = True
while ans:
  cs()
  print(hexMenu)
  ans = input("What would you like to do: ").lower()
  if ans == "enc":
    hexEncrypt()
  elif ans=="dec":
    hexDecrypt()
  elif ans == "back":
    cs()
    exec(open("mods/navigation/encryptionMenu.py").read())
  elif ans == "mm":
    cs()
    exec(open("main.py").read())
  elif ans == "e":
    #exit the script
    print(exitMessage)
    exit()
  else:
    print("Invalid option try again!")