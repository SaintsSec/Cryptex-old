#!/usr/bin/env python3

# created by : Mart | marvhus

import hashlib

# help menu for cipheringing process
help_menu = """
+------------------------------------------------------+
| [✓] ARGUMENTS MD5                                    |
| [✓] ARG 1. Ciphering Process                         |
|         [-e] .......... Encrypt                      |
|         [-b] .......... Brute Force                  |
| [✓] ARG 2. Additional Aruments                       |
|         [-t <plaintext>] --------- Input Text        |
|         [-i <input file>] -------- Input File [.txt] |
|         [-o <output file>] ------- Output File       |
|         [-w <input file>] -------- Wordlist          |
|             [Required for bruteforcing '-b']         |
+------------------------------------------------------+
| [✓] Example:                                         |
|  cryptex md5 -e -t hello                             |
|  cryptex md5 -b -t alksdjakdsj                       |
+------------------------------------------------------+
"""

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(input):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = input.text

    if text:
        # Run Decode
        output = f'Encoding | {text}'

        result = hashlib.md5( text.encode('utf-8')  ).hexdigest()

        output += f"\nMD5 Sum | {result}"

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return [f'"{text}" is not a valid input for -t', False]

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(input):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = input.text
    wordlist = input.wordlist

    # TODO (Mart): Find a way to brute force the hash using the utf-8 charset and a length/range

    if text and wordlist:
        # Run Decode
        output = f'Bruteforcing | {text}'

        length = len(wordlist)

        print()
        for i, word in enumerate(wordlist):
            print(f'Checking {i + 1}/{length}', end='\r')
            guess = hashlib.md5( word.encode('utf-8') ).hexdigest()
            if guess.lower() == text.lower():
                output += f'\nDecoded MD5: | {word}'
                return [output, True]
            continue
        print()

        output = "Not found in wordlist"
        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output, False]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output

        if not wordlist:
            return ['Wordlist error', False]

        return [f'"{text}" is not a valid input for -t', False]
