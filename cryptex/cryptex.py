import os
"""
TODO Error Checking | IE: If the user fat fingers 
something it will warn that the encryption is not valid
"""
menuText = """
  _____              __         
 / ___/_____ _____  / /______ __
/ /__/ __/ // / _ \/ __/ -_) \ /
\___/_/  \_, / .__/\__/\__/_\_\ 
 V:0.0.1/___/_/ @CythesOut  
    -----{Main menu}-----
    1.Hex Encoder
    2.Base64 Encoder
    3.Password Generator
    4.Information
    5.Exit/Quit
    ---------------------
"""
information = """
       --------------{Program Information}----------------
      Author: @CythesOut(https://twitter.com/CythesOut)
      Github: https://github.com/CythesOut
      
      Description: 
      A simple text to hex encoder / decoder. 
      I might do more with it later.
      -----------------------------------------------------
"""
ans=True
while ans:
    #print out menu and ask user what they want to do.
    print(menuText)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      os.system("clear")
      #os.system("python3 ~/encodehex.py")
      exec(open("encodehex.py").read())
    elif ans=="2":
      os.system("clear")
      #os.system("python3 ~/encodebase64.py")
      exec(open("encodebase64.py").read())
    elif ans=="3":
      os.system("clear")
      #os.system("python3 ~/CryptexPass.py")
      exec(open("cryptexpass.py").read())    
    elif ans=="4":
      os.system("clear")
      print(information) 
      input("\nPress enter to return to main menu...")
      os.system("clear")
    elif ans=="5":
      #exit the script
      print("\n Goodbye\n\n")
      exit() 
    elif ans !="":
      #Failsafe incase if someone presses a non-menu item
      print("\n Not Valid Choice Try again") 