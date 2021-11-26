# Cryptex a simple CLI lockpicking tool   
[![forthebadge](https://forthebadge.com/images/badges/it-works-why.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)  
![status](https://img.shields.io/pypi/status/st?logo=git&style=plastic)
![commits](https://img.shields.io/github/last-commit/CythesOut/Cryptex?logo=github)
![downloads](https://img.shields.io/github/downloads/CythesOut/Cryptex/total)  

# So why?  
Honestly, I'm not sure why I am doing this. The project started with a post on facebook in which was encrypted text in Base64. I thought to myself "I wonder if I can make a program to decrypt this on my own."  
I started with HEX then moved into Base64. The current plan is to expand into harder encryption / decryption and make it an actual decent program. Eventually I would like to add an optional GUI but this is going to always be a CLI program first. Anyway.

#### What can it do:
- Encode / Decode Hex
- Encode / Decode Base64
- Break Randomly :D 
  
#### Requirements:  
- Python3 
- Linux as your Host OS (Though it can hypothetically work on windows.)
  
#### linkies:  
  [Check out the project board](https://github.com/CythesOut/Cryptex/projects/)  
  [Join or start the discussion](https://github.com/CythesOut/Cryptex/discussions)  
  [Check out my twitter page](https://twitter.com/CythesOut)

# Install:  
1.) Clone the repo  
```
gh repo clone CythesOut/Cryptex
```
2.) cd into the directory  
```
cd Cryptex/cryptex
```
3.) run the script  
```
python3 cryptex.py
```
<!---
##### Optional:  
change permissions to +x on cryptex.py  
```
sudo chmod +x cryptex.py
```
Copy cryptex.py into /usr/bin  
```
sudo cp cryptex.py /usr/bin
```
set system alias(BASH | ZSH):  
```
cd
sudo nano ~/.zshrc
#alternatively you can edit bashrc as well: sudo nano ~/.bashrc
#Add this line to the bottom of the file.
alias cryptex="python3 /usr/bin/cryptex.py
#reload zshrc
source ~/.zshrc
```  
You should now be able to run the script by simply typing **cryptex**  
--->
**Enjoy!**
