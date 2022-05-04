#!/bin/bash
# installer for Cryptex
# created by : C0SM0

# staging
echo [*] Staging process...
mkdir ~/.Cryptex
cd ..
# mv Cryptex/* ~/.Cryptex
cp Cryptex/* ~/.Cryptex
# rm -rf Cryptex
cd ~/.Cryptex
echo [+] Completed

#  get tools
echo [*] Installing tools...
sudo apt update
sudo apt-get install python3
sudo apt-get install python3-pip python-dev
pip install pyperclip 
pip install qrcode
pip install Image
pip install Cryptography
echo [+] Completed

# set up alias workflow
echo [*] Setting up alias...
echo "alias cryptex=\"python3 $(pwd)/main.py\"" >> ~/.bashrc
echo "alias cryptex=\"python3 $(pwd)/main.py\"" >> ~/.zshrc
echo [+] Completed

# clean up
echo [+] Installation Completed
echo "- please restart your terminal"
echo "- type 'cryptex' launch Cryptex"