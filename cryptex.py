import os
"""
TODO Error Checking | IE: If the user fat fingers 
something it will warn that the encryption is not valid
"""
menuText = """
    -----{Main menu}-----
    1.Convert to Hex
    2.Convert from Hex
    3.Program info
    4.Exit/Quit
    ---------------------
"""
ans=True
while ans:
    #print out menu and ask user what they want to do.
    print(menuText)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        #Clear the screen and take user to text to hex encoder
        os.system("clear")
        print("Text > HEX encoder!\n")
        #Ask user for text they wish to encode
        text2hex = input("What would you like to encode:\n")
        #Convert the text from UTF-8 into hex. 
        hexIn = text2hex.encode("utf-8").hex()
        #Print out the hex string
        print("\nHere is your encoding: \n\n" + hexIn)
        #TODO Enable | automagic copy of output to clipboard 
        input("\nPress enter to return to main menu...")
        os.system("clear")
    elif ans=="2":
        #Clear the screen and take user to Hex to Text decoder
        os.system("clear")
        print("HEX > Text encoder!\n")
        #Ask user what they want to convert
        hex2txt = input("\nWhat would you like to convert:\n")
        #Decrypt the text and print it out
        textOut = bytes.fromhex(hex2txt).decode("utf-8")
        print("\nHere is your encoding: \n\n" + textOut)
        #TODO Enable | Automagic copy of output into clipboard
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
      #exit the script
      print("\n Goodbye\n\n")
      exit() 
    elif ans !="":
      #Failsafe incase if someone presses a non-menu item
      print("\n Not Valid Choice Try again") 