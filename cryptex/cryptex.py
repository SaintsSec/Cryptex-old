import os
from menu import menu, information

ans=True
while ans:
    #print out menu and ask user what they want to do.
    print(menu)
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
      #os.system("python3 ~/encodebase64.py")
      exec(open("cCypher.py").read())
    elif ans=="4":
      os.system("clear")
      #os.system("python3 ~/CryptexPass.py")
      exec(open("cryptexpass.py").read())    
    elif ans=="5":
      os.system("clear")
      print(information) 
      input("\nPress enter to return to main menu...")
      os.system("clear")
    elif ans=="6":
      #exit the script
      print("\n Goodbye\n\n")
      exit() 
    elif ans !="":
      #Failsafe incase if someone presses a non-menu item
      print("\n Not Valid Choice Try again") 