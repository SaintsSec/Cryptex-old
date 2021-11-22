## Cryptex a simple CLI encoder / decoder  
As of right now the only thing this can do is encode / decode to and from hex.  
  
#### Requirements:  
Python3
  
#### Future plans:  
  - Add more encoders and decoders  

#### Install:  
1.) Clone the repo  
```
gh repo clone CythesOut/Cryptex
```
2.) cd into the directory  
```
cd Cryptex/
```
3.) run the script  
```
python3 cryptex.py
```

##### Optional:  
change permissions to +x on pyencode.py  
```
sudo chmod +x cryptex.py
```
Copy cryptex.py into /usr/bin  
```
sudo cp cryptex.py /usr/bin
```
set system alias(BASH | ZSH):  
```
sudo nano ~/.zshrc
#alternatively you can edit bashrc as well: sudo nano ~/.bashrc
#Add this line to the bottom of the file.
alias cryptex="python3 /usr/bin/cryptex.py
```  
You should now be able to run the script by simply typing **cryptex**  
  
**Enjoy!**
