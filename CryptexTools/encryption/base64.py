from mods.menu import b64Menu, exitMessage
from mods.clearScreen import clear_screen as cs
from libs.encryption import b64Encrypt, b64Decrypt

ans = True
while ans:
  cs()
  print(b64Menu)
  ans = input("What would you like to do: ").lower()
  if ans == "enc":
    b64Encrypt()
  elif ans=="dec":
    b64Decrypt()
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