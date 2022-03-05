import hashlib
import os
import pyperclip as pc
from menu import sha526logo

ans = True
while ans:
  print(sha526logo)
  ans = input("What would you like to do: ").lower()
  if ans == "enc":
    os.system("clear")
    print("""
   ____                       __ 
  / __/__  __________ _____  / /_
 / _// _ \/ __/ __/ // / _ \/ __/
/___/_//_/\__/_/  \_, / .__/\__/ 
                 /___/_/   
    """)
    #Ask user for text they wish to encode
    str = input("What would you like to encrypt: \n")
    encode = hashlib.sha256(str.encode())
    encodeHex = encode.hexdigest()
    pc.copy(encodeHex)
    print(f"Here is the encryption: \n{encodeHex} \n\nCopied to clipboard...")
    input("\nPress enter to return to main menu...")
    os.system("clear")
  elif ans == "mm":
    os.system("clear")
    #os.system("python3 ~/cryptex.py")
    exec(open("cryptex.py").read())
  elif ans == "e":
    #exit the script
    print("\n Goodbye\n\n")
    exit()   
  else:
    print("Invalid option try again!")