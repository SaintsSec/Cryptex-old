from mods.menu import sha526logo, exitMessage
from mods.clearScreen import clear_screen as cs
from libs.encryption import SHAEncrypt

ans = True
while ans:
  cs()
  print(sha526logo)
  ans = input("What would you like to do: ").lower()
  if ans == "enc":
    SHAEncrypt()
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