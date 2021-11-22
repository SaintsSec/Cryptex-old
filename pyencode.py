import os
ans=True
while ans:
    print ("""

    -----{Main menu}-----
    1.Convert to Hex
    2.Convert from Hex
    3.Program info
    4.Exit/Quit
    ---------------------
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        os.system("clear")
        print("Text > HEX encoder!\n")
        text2hex = input("What would you like to encode:\n")
        hexIn = text2hex.encode("utf-8").hex()
        print("\nHere is your encoding: \n\n" + hexIn)
        input("\nPress enter to return to main menu...")
        os.system("clear")
    elif ans=="2":
        os.system("clear")
        print("HEX > Text encoder!\n")
        hex2txt = input("\nWhat would you like to convert:\n")
        textOut = bytes.fromhex(hex2txt).decode("utf-8")
        print("\nHere is your encoding: \n\n" + textOut)
        input("\nPress enter to return to main menu...")
        os.system("clear")
    elif ans=="3":
      os.system("clear")
      print("""
       --------------{Program Information}----------------
      Author: @CythesOut(https://twitter.com/CythesOut)
      Github: https://github.com/CythesOut
      
      Description: 
      A simple text to hex encoder / decoder. 
      I might do more with it later.
      -----------------------------------------------------
      """) 
      input("\nPress enter to return to main menu...")
      os.system("clear")
    elif ans=="4":
      print("\n Goodbye\n\n")
      exit() 
    elif ans !="":
      print("\n Not Valid Choice Try again") 