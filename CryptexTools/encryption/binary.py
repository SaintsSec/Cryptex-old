from mods.clearScreen import clear_screen as cs
import pyperclip as pc

from mods.menu import exitMessage, binaryLogo

cs()
print(binaryLogo)
choice = input("\nenter [1] for string to binary, [2] for binary to string, [b] to go back : ")

if choice == "1":
    str2bin = input("Enter a string to convert to binary: ")
    output = ' '.join(format(ord(x), 'b') for x in str2bin)
    pc.copy(output)
    print(f"Encoding: \n\n... {output} \n\n...copied to clipboard")
    input("\npress enter to continue...")
if choice == "2":
    output = ''
    dec2str= input("Enter a binary number to convert to string: ")
    binary_list = dec2str.split(' ')
    # print(binary_list)
    for binary in binary_list:
        output += f'{chr(int(binary, 2))}'
    pc.copy(output)
    print(f"Decoding: \n\n... {output} \n\n...copied to clipboard")
    input("\nPress enter to continue...")
if choice == "b":
    input("\n\nPress enter to go back...")