import os
import pyperclip as pc
menuText = """
   __ __                __        _            __
  / // /____ _____ ____/ /__ ____(_)_ _  ___ _/ /
 / _  / -_) \ / _ `/ _  / -_) __/ /  ' \/ _ `/ / 
/_//_/\__/_\_\\_,_/\_,_/\__/\__/_/_/_/_/\_,_/_/

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
    text2hex = input("What would you like to encode:\n")
    #Convert the text from UTF-8 into hex. 
    hexIn = text2hex.encode("utf-8").hex()
    #Print out the hex string
    pc.copy(hexIn)
    print("\nHere is your encoding: \n\n" + hexIn)
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
      #Ask user what they want to convert
      hex2txt = input("\nWhat would you like to convert:\n")
      #Decrypt the text and print it out
      textOut = bytes.fromhex(hex2txt).decode("utf-8")
      print("\nHere is your decoding: \n\n" + textOut)
      #TODO Enable | Automagic copy of output into clipboard
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