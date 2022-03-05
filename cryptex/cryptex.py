import os
from menu import menu, information

ans=True
while ans:
    #print out menu and ask user what they want to do.
    os.system("clear")
    print(menu)
    ans=input("Enter a shortcode. ").lower() 
    if ans == "hex": 
      os.system("clear")
      #os.system("python3 ~/encodehex.py")
      exec(open("hex.py").read())
    elif ans == "b64":
      os.system("clear")
      #os.system("python3 ~/encodebase64.py")
      exec(open("base64.py").read())
    elif ans == "256":
      os.system("clear")
      #os.system("python3 ~/encodebase64.py")
      exec(open("256.py").read())
    elif ans == "md5":
      os.system("clear")
      #os.system("python3 ~/encodebase64.py")
      exec(open("md5crack.py").read())
    elif ans == "cc":
      os.system("clear")
      #os.system("python3 ~/encodebase64.py")
      exec(open("cCypher.py").read())
    elif ans == "qr":
      os.system("clear")
      exec(open("QR.py").read())
    elif ans == "pg":
      os.system("clear")
      #os.system("python3 ~/CryptexPass.py")
      exec(open("cryptexpass.py").read())    
    elif ans == "i":
      os.system("clear")
      print(information) 
      input("\nPress enter to return to main menu...")
      os.system("clear")
    elif ans == "e":
      #exit the script
      print("\n Goodbye\n\n")
      exit() 
    elif ans !="":
      #Failsafe incase if someone presses a non-menu item
      print("\n Not Valid Choice Try again") 