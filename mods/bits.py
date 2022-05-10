# import getpasscd
import sys
import os
import getpass

# Variables
username = getpass.getuser() # Get username
header = f'[~] {username}@cryptex $ ' # header for user input
remote_path = 'raw.githubusercontent.com/AlexKollar/Cryptex/master' # remote url path
local_path = f'/home/{username}/.Cryptex' if username != 'root' else '/root/.Cryptex' # local path to cryptex
cipher = f'{local_path}/ciphers/' # local path to ciphers

# Colors
SUCCESS = '\033[92m'
FAIL = '\033[91m'
END = '\033[0m'

version = open(f'{local_path}/version.txt').read().strip()
version = 0.5
banner = f'''

                 .--------.
                / .------. \\
               / /        \ \\
               | |        | |
              _| |________| |_
            .' |_|        |_| '.
            '._____ ____ _____.'
            |     .'____'.     |
            '.__.'.'    '.'.__.'
            '.__  |      |  __.'
            |   '.'.____.'.'   |
            '.____'.____.'____.'
            '.________________.'
       _____              __         
      / ___/_____ _____  / /______ __
     / /__/ __/ // / _ \/ __/ -_) \ /
     \___/_/  \_, / .__/\__/\__/_\_\ 
             /___/_/
Locks only exist to keep honest people honest
            Version : 0.{version}
'''

help_menu = """
    +-------------------------------------------------------------+
    | [+] EXAMPLE cryptex cc -d -t 'This is a string to encrypt'  |
    | [+] ARG 1. Cipher                                           |                                         
    |       [cc] --------- Caesar Cipher                          |
    |       [vc] --------- Vingenere Cipher                       |
    |       [rc] --------- Reverse Cipher                         |
    |       [mc] --------- Multiplicative Cipher                  |
    |       [dh] --------- Diffie Hellman Key Exchange            |
    |       [xor] -------- XOR Cipher                             |
    |       [r13] -------- ROT 13                                 |
    |       [r47] -------- ROT 47                                 |
    |       [b64] -------- Base64                                 |
    |       [bin] -------- Binary                                 |
    |       [hex] -------- Hex                                    |
    |       [oct] -------- Octal                                  |
    |       [1337] ------- L33T 5P34K                             | 
    |       [mor] -------- Morse Code                             | 
    |       [pho] -------- Phonetic Alphabet                      |
    |       [md5] -------- MD5                                    |
    |       [sha256] ----- Sha256                                 |
    |       [menc] ------- MENC                                   |
    +-------------------------------------------------------------+ 
    | [+] ARG 2. Cipher Method                                    |
    |       [-e] ---------- Encrypt                               |
    |       [-d] ---------- Decrypt                               |
    |       [-b] ---------- Break                                 |
    +-------------------------------------------------------------+
    | [+] Additional Arguments                                    |
    |       [-t] ---------- Input Text                            |
    |       [-i] ---------- Input File                            |
    |       [-o] ---------- Output File                           | 
    |       [-k] ---------- Encryption Key                        | 
    |       [-r] ---------- Range                                 | 
    |       [-w] ---------- Wordlist                              |
    +-------------------------------------------------------------+
    | [+] Cryptex Arguments                                       |
    |       [--help] ------ help                                  |
    |       [--version] --- version                               |    
    |       [--update] ---- update                                |
    +-------------------------------------------------------------+
"""
