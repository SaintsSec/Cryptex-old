from os import urandom
import pyperclip as pc
from mods.menu import xorLogo, exitMessage
from mods.clearScreen import clear_screen as cs

cs()
encoding = "utf-8"

def genkey(length: int) -> bytes:
    """Generate key."""
    return urandom(length)

def xor_strings(s, t) -> bytes:
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

print(xorLogo)

message = input("Plaintext: ")
key = genkey(len(message))
print('\nKey:', key)
cipherText = xor_strings(message.encode(encoding), key)
print('\ncipherText:', cipherText)

decrypt = input("\n\nWould you like to decrypt this message? [y/n]: ")
if decrypt == "y":
    print('\n\ndecrypted:', xor_strings(cipherText, key).decode(encoding))
    input("\n\nPress enter to continue...")
if decrypt == "n":
    print(exitMessage)
    input()
    exit()