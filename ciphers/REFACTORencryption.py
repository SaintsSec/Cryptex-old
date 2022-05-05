from mods.clearScreen import clear_screen as cs
from mods.menu import encrypt, decrypt
import pyperclip as pc
import base64, hashlib
  
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