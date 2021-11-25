import os
import base64
import pyperclip as pc
menuText = """
   ___                 ____ ____
  / _ )___ ____ ___   / __// / /
 / _  / _ `(_-</ -_) / _ \/_  _/
/____/\_,_/___/\__/  \___/ /_/ 

    -----{Main menu}-----
    1.Encrypt
    2.Decrypt
    3.Main Menu
    4.Exit/Quit
    ---------------------
"""

ans = True
while ans:
  print(menuText)
  ans = input("What would you like to do: ")
  if ans == "1":
    os.system("clear")
    print("""
   ____                       __ 
  / __/__  __________ _____  / /_
 / _// _ \/ __/ __/ // / _ \/ __/
/___/_//_/\__/_/  \_, / .__/\__/ 
                 /___/_/   
    """)
    #Ask user for text they wish to encode
    text2b64 = input("What would you like to encode:\n")
    #Convert the text from UTF-8 into Base64.
    text2b64_bytes = str.encode(text2b64) 
    base64_bytes = base64.b64encode(text2b64_bytes)
    base64_message = base64_bytes.decode('ascii')
    #Print out the hex string
    pc.copy(base64_message)
    print("\nHere is your encoding: \n\n" + base64_message)
    #TODO Enable | automagic copy of output to clipboard 
    input("\nPress enter to return to main menu...")
    os.system("clear")
  elif ans=="2":
      os.system("clear")
      print("""
   ___                        __ 
  / _ \___ __________ _____  / /_
 / // / -_) __/ __/ // / _ \/ __/
/____/\__/\__/_/  \_, / .__/\__/ 
                 /___/_/ 
      """)
      #Ask user for text they wish to encode
      b642text = input("What would you like to encode:\n")
      #Convert the text from Base64 into Text.
      decoded = base64.b64decode(b642text)
      finaltext = decoded.decode('ascii')
      #Print out the hex string
      print("\nHere is your encoding: \n\n" + finaltext)
      #TODO Enable | automagic copy of output to clipboard 
      input("\nPress enter to return to main menu...")
      os.system("clear")
  elif ans == "3":
    os.system("clear")
    #os.system("python3 ~/cryptex.py")
    exec(open("cryptex.py").read())
  elif ans == "4":
    #exit the script
    print("\n Goodbye\n\n")
    exit()   
  else:
    print("Invalid option try again!")