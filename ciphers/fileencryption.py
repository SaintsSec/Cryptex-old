from cryptography.fernet import Fernet
from mods.clearScreen import clear_screen as cs
from mods.menu import fileEncryptLogo, exitMessage

cs()
print(fileEncryptLogo)
def writeKey():
    key = Fernet.generate_key()
    with open ('key.key', 'wb') as key_file:
        key_file.write(key)
        
def loadKey():
    return open('key.key', 'rb').read()

def encryptFile(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        fileData = file.read()
    encryptedData = f.encrypt(fileData) 
    with open(filename, 'wb') as file:
        file.write(encryptedData)
        
def decryptFile(filename, key):
    f = Fernet(key)
    with open (filename, 'rb') as file:
        encryptedData = file.read()
    decryptedData = f.decrypt(encryptedData)
    with open(filename, 'wb') as file:
        file.write(decryptedData)


def main():   
    key = loadKey()
    filename = input("Enter the file name: ")    
    choice = input("\nWould you like to [1]encrypt or [2]decrypt a file? ")
    if choice == "1":
        encryptFile(filename, key)
        input("\n...File Encrypted\n\nPress enter to go back to encryption menu")
    elif choice == "2":
        decryptFile(filename, key)
        input("\n...File Decrypted\n\nPress enter to go back to encryption menu")

def ToKeyOrNotToKey():
    keyChoice = input("Would you like to generate a key? (y/n) ") 
    if keyChoice == 'y':
        writeKey()
        print("\nBe sure you save your key somewhere safe!\n")
        main()
    elif keyChoice == 'n':
        main()

ToKeyOrNotToKey()
