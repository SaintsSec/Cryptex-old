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

# check for arguments
if [[ $# -eq 0 ]] ; then
    echo -e "${red}No arguments specified. Use --help to see a list of possible arguments.${reset}"
    exit 0
fi

# check if run with sudo
if [ "$EUID" -ne 0 ]; then
    continue
else
    echo -e "${red}Do not run as root. The script will prompt you for root access.${reset}"
    exit 0
fi

debian=false
arch=false
void=false

# arguments
while [ -n "$1" ]
do
case "$1" in

--help) 
  echo "
        --debian    installer for debain
        --arch      installer for arch
        --void      installer for void
  "     
  exit 0
;;

--debian) 
    debian=true
;;

--arch) 
    arch=true
;;

--void)
    void=true
;;

*) 
  echo -e "${red}$1 is not an option. See --help for a list of arguments. ${reset}" 
  exit 0
;;
esac
shift
done

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

if [ "$debian" = true ]
    then
    # installing tools for debian
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo apt update
    sudo apt-get install python3
    sudo apt-get install python3-pip python-dev
    pip install qrcode
    pip install Cryptography
    pip install googletrans==3.1.0a0
    pip install colorama
    echo -e "${green}[+] Completed${reset}"
fi

if [ "$void" = true ]
    then
    # installing tools for void
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo xbps-install -S python3
    pip install qrcode
    pip install Cryptography
    pip install googletrans==3.1.0a0
    pip install colorama
    echo -e "${green}[+] Completed${reset}"
fi

if [ "$arch" = true ]
    then
    # installing tools for arch
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo pacman -Syu
    sudo pacman -S python python-pip
    python3 -m pip install qrcode
    python3 -m pip install Cryptography
    python3 -m pip install googletrans==3.1.0a0
    python3 -m pip install colorama
    echo -e "${green}[+] Completed${reset}"
fi

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