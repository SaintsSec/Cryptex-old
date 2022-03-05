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
    str = input("What would you like to encrypt: ")
    encode = hashlib.sha256(str.encode())
    encodeHex = encode.hexdigest()
    pc.copy(encodeHex)
    print(f"Here is the encryption: \n{encodeHex} \n\nCopied to clipboard...")
    input("\nPress enter to return to main menu...")
    os.system("clear")
#  elif ans=="dec":
#      os.system("clear")
#      print("""
#   ___                        __ 
#  / _ \___ __________ _____  / /_
# / // / -_) __/ __/ // / _ \/ __/
#/____/\__/\__/_/  \_, / .__/\__/ 
#                 /___/_/ 
#      """)
      #Ask user for text they wish to encode
#      b642text = input("What would you like to decrypt:\n")
      #Convert the text from Base64 into Text.
#     decoded = base64.b64decode(b642text)
#      finaltext = decoded.decode('ascii')
      #Print out the hex string
#      print("\nHere is your encoding: \n\n" + finaltext)
      #TODO Enable | automagic copy of output to clipboard 
#      input("\nPress enter to return to main menu...")
#      os.system("clear")  
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
