#!/usr/bin/python

# Rot13 package for the the codex project
# created by : C0SM0 | Fyzz

# imports
import os

# help menu for cipheringing process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Rotation13-Cipher                      |
|  [+] ARG 1. Ciphering Process                         |
|          [-e] ---------- Encrypt                      |
|          [-d] ---------- Decrypt                      |
+-------------------------------------------------------+
|  [+] ARG 2. Additional Aruments                       |
|          [-t <plaintext>] --------- Input Text        |
|          [-i <input file>] -------- Input File [.txt] |
|          [-o <output file>] ------- Output File       |
+-------------------------------------------------------+ 
|  [+] Example:                                         |
|          cryptex r13 -e -t hello                      |
+-------------------------------------------------------+
"""

def encode(input):
    text = input.text
    os.system(f'python3 ~/.Cryptex/main.py cc -e -t "{text}" -k 13')

def decode(input):
    text = input.text
    os.system(f'python3 ~/.Cryptex/main.py cc -d -t "{text}" -k 13')
