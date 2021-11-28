import random
import pyperclip as pc
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("""
   ___                                 __  _____                      __             
  / _ \___ ____ ____    _____  _______/ / / ___/__ ___  ___ _______ _/ /____  ____   
 / ___/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/   
/_/   \_,_/___/___/__,__/\___/_/  \_,_/  \___/\__/_//_/\__/_/  \_,_/\__/\___/_/      
                                     v1.0.0                                            
      """)
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordList = []

for char in range(1, nr_letters + 1):
  passwordList += random.choice(letters)

for char in range(1, nr_symbols + 1):
  passwordList += random.choice(symbols)
  
for char in range(1, nr_numbers + 1):
  passwordList += random.choice(numbers)

random.shuffle(passwordList)
password = ""
for char in passwordList:
  password += char
print(f"\nYour new password is: \n\n{password}")
pc.copy(password)
input("\nYour new password has been copied to the clipboard \nPress Enter to go to main menu")