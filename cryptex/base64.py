import os
import base64
import pyperclip as pc
from menu import b64Menu

ans = True
while ans:
  print(b64Menu)
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
    text2b64 = input("What would you like to encrypt:\n")
    #Convert the text from UTF-8 into Base64.
    text2b64_bytes = str.encode(text2b64) 
    base64_bytes = base64.b64encode(text2b64_bytes)
    base64_message = base64_bytes.decode('ascii')
    #Print out the hex string
    pc.copy(base64_message)
    print("\nHere is your encoding: \n\n" + base64_message + "\n\nEncoding copied to clipboard.")
    #TODO Enable | automagic copy of output to clipboard 
    input("\nPress enter to return to main menu...")
    os.system("clear")
  elif ans=="dec":
      os.system("clear")
      print("""
   ___                        __ 
  / _ \___ __________ _____  / /_
 / // / -_) __/ __/ // / _ \/ __/
/____/\__/\__/_/  \_, / .__/\__/ 
                 /___/_/ 
      """)
      #Ask user for text they wish to encode
      b642text = input("What would you like to decrypt:\n")
      #Convert the text from Base64 into Text.
      decoded = base64.b64decode(b642text)
      finaltext = decoded.decode('ascii')
      #Print out the hex string
      print("\nHere is your encoding: \n\n" + finaltext)
      #TODO Enable | automagic copy of output to clipboard 
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