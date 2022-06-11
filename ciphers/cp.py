#!/usr/bin/python

# created by : C0SM0

# TODO: list
''' 
- make powershell code into formatted docsrting
'''

# help menu for cipheringing process
# TODO: arguments
'''
# payloads

# renditions
- hak5 tool incorporation?
    - output to hak5
- user interaciton [cpp v pwsh]
'''
help_menu = """
+----------------------------------------------------------+
| [✓] ARG 2. Additional Aruments                           |
|         [-wh <webhook>] ------------ Discord Webhook     |
|         [-wc] ---------------------- Web Credentials     |
|         [-ml] ---------------------- Mail Credentials    |
|         [-wf] ---------------------- WiFi Credentials    |
|         [-rw] ---------------------- Custom Ransomware   |
|         [-pe] ---------------------- Payload Encoder     |
|         [-dl] ---------------------- DialUp Credentials  |
|         [-sam] --------------------- SAM Grabber         |
|         [-o <output-method>] ------- Output File         |
|             <rd> ------------------- USB RubberDucky     |
|             <bb> ------------------- Bash Bunny          |
|             <omg> ------------------ O.MG Cable          |
|             <exe> ------------------ Portable Executable |
|             <ps1> ------------------ PowerShell Script   |
+----------------------------------------------------------+
| [✓] Example:                                             |
|  cryptex cp -wc -wh https://... -o ps1                   |
+----------------------------------------------------------+
"""

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Encoding | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]

# decode function [!] Each Cipher Must Have This <---------- [!]
def decode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Decoding | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Bruteforcing | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]

'''
//RESOURCES

RAWPATH - https://raw.githubusercontent.com/AlexKollar/Cryptex/master/payloads

function random-text {

    return -join ((65..90) + (97..122) | Get-Random -Count 10 | ForEach-Object {[char]$_})

}
'''
