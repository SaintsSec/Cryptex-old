#!/usr/bin/python
# runs rot13 using caesar cipher [cc.py]

# imports
import os
import sys
import getpass 

# banners
help_menu = """
      +------------------------------------------------------+
      |  [+] ARGUMENTS Rotation13-Cipher                     |
      |  [+] ARG 1. Ciphering Process                        |
      |          [-e] ---------- Encrypt                     |
      |          [-d] ---------- Decrypt                     |
      +------------------------------------------------------+
      |  [+] ARG 2. Additional Aruments                      |
      |          [-t <plaintext>] --------- Input Text       |
      |          [-i <input file>] -------- Input File [.txt]|
      |          [-o <output file>] ------- Output File      |
      +------------------------------------------------------+ 
      |  [+] Example:                                        |
      |          cryptex -r13 -e -t hello                    |
      +------------------------------------------------------+
    """

# variables
username = getpass.getuser() # gets username
local_path = f'/home/{username}/.Cryptex' if username != 'root' else '/root/.Cryptex' # local path to cryptex
cipher = f'{local_path}/ciphers/' # local path to ciphers

if sys.argv[1:]:
    # execution
    string_args = ' '.join(sys.argv[1:])
    os.system(f'python3 {cipher}cc.py {string_args} -k 13')
else:
    print(help_menu)