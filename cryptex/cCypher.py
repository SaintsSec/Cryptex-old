import pyperclip as pc

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]

from ceasarArt import logo
print(logo)

def ceasar(startText, shiftAmmount, cypherDirection):
    endText = ""
    if cypherDirection == "decode":
        shiftAmmount *= -1
    for char in startText:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + shiftAmmount
            endText += alphabet[newPosition]
        else:
            endText += char
    print(f"the {cypherDirection}d text is: {endText}")
    if cypherDirection == "encode":
        pc.copy(endText)
        print("\nYour encoding has been copied to the clipboard!")

shouldContinue = True
while shouldContinue:        
    direction = input("Type \'encode\' to encode a message or type \'decode\' to decode a message: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type your shift number:\n"))
    #avoid absurd numbers for shift codes
    shift = shift % 26
        
    #Run the function :D
    ceasar(startText=text, shiftAmmount=shift, cypherDirection=direction)
    result = input("\nType 'yes' if you want to go again. Otherwise Type 'no'\n")
    if result == "no":
        shouldContinue = False
        print("Goodbye!")