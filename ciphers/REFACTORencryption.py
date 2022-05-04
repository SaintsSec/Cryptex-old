from mods.clearScreen import clear_screen as cs
from mods.menu import encrypt, decrypt
import pyperclip as pc
import base64, hashlib


#All code regarding hex 
def hexEncrypt():
  cs()
  print(encrypt)    
  #Ask user for text they wish to encode
  text2hex = input("What would you like to encrypt:\n")
  #Convert the text from UTF-8 into hex. 
  hexIn = text2hex.encode("utf-8").hex()
  #Print out the hex string
  pc.copy(hexIn)
  print(f"\nHere is your encoding: \n\n {hexIn} \n\n... Encoding copied.")
  input("\nPress enter to return to main menu...")
  cs()

def hexDecrypt():
  cs()
  print(decrypt)
  #Ask user what they want to convert
  hex2txt = input("\nWhat would you like to decrypt:\n")
  #Decrypt the text and print it out
  textOut = bytes.fromhex(hex2txt).decode("utf-8")
  pc.copy(textOut)
  print(f"\nHere is your decryption: \n\n {textOut}\n\n... Decryption copied")
  input("\nPress enter to return to main menu...")
  cs()
  
# All code for SHA256
def SHAEncrypt():
    cs()
    print(encrypt)
    #Ask user for text they wish to encode
    str = input("What would you like to encrypt: \n")
    encode = hashlib.sha256(str.encode())
    encodeHex = encode.hexdigest()
    pc.copy(encodeHex)
    print(f"Here is the encryption: \n\n {encodeHex} \n\n... Encryption copied")
    input("\nPress enter to return to main menu...")
    cs()