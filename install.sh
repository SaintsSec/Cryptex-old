#!/bin/bash
# installer for Cryptex
# created by : C0SM0
# DO NOT FUCK WITH THIS SCRIPT

# color variables
red="\e[0;91m"
green="\e[0;92m"
blue="\e[0;94m"
bold="\e[1m"
reset="\e[0m"

# staging
# echo -e "${blue}[*] Staging process...${reset}"
# mkdir ~/.Cryptex
# cd ..
# mv Cryptex/* ~/.Cryptex
# rm -rf Cryptex
# cd ~/.Cryptex
# echo -e "${green}[+] Complete${reset}"

# staging for testing
echo -e "${blue}[*] Staging process...${reset}"
mkdir ~/.Cryptex
cd ..
cp Cryptex/* ~/.Cryptex -r
cd ~/.Cryptex
echo -e "${green}[+] Completed${reset}"

# installing tools
echo -e "${blue}[*] Installing tools...${reset}"
sudo apt update
sudo apt-get install python3
sudo apt-get install python3-pip python-dev
pip install qrcode
pip install Cryptography
pip install googletrans==3.1.0a0
pip install colorama

echo -e "${green}[+] Completed${reset}"

# set up alias workflow
echo -e "${blue}[*] Setting up alias...${reset}"

# check if it already exists in bashrc
if ! cat ~/.bashrc | grep "CRYPTEX_PATH" > /dev/null; then
echo "export CRYPTEX_PATH=\"~/.Cryptex\"" >> ~/.bashrc
echo "alias cryptex=\"python3 ~/.Cryptex/main.py\"" >> ~/.bashrc
fi

#check if it already exists in zshrc
if ! cat ~/.zshrc | grep "CRYPTEX_PATH" > /dev/null; then
echo "export CRYPTEX_PATH=\"~/.Cryptex\"" >> ~/.zshrc
echo "alias cryptex=\"python3 ~/.Cryptex/main.py\"" >> ~/.zshrc
fi

echo -e "${green}[+] Completed${reset}"

# clean up
echo -e "${green}[+] Installation Successful"
echo -e "[+] Please Restart your terminal"
echo -e "[+] type 'cryptex' launch Cryptex${reset}"
bash