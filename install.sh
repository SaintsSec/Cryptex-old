#!/bin/bash
# installer for Cryptex
# created by : C0SM0

# declare variables
red="\e[0;91m"
green="\e[0;92m"
blue="\e[0;94m"
bold="\e[1m"
reset="\e[0m"

# check if run with sudo
if [ "$EUID" -ne 0 ]
    then echo -e "${red}Please run as root${reset}"
    exit 0
fi

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

#  get tools
echo -e "${blue}[*] Installing tools...${reset}"
sudo apt update
sudo apt-get install python3
sudo apt-get install python3-pip python-dev
pip install qrcode
pip install Cryptography
echo -e "${green}[+] Completed${reset}"

# set up alias workflow
echo -e "${blue}[*] Setting up alias...${reset}"
echo "alias cryptex=\"python3 $(pwd)/main.py\"" >> ~/.bashrc
echo "alias cryptex=\"python3 $(pwd)/main.py\"" >> ~/.zshrc
echo -e "${green}[+] }Completed${reset}"

# clean up
echo -e "${green}[+] Installation Successful"
echo -e "[+] Please Restart your terminal"
echo -e "[+] type 'cryptex' launch Cryptex${reset}"