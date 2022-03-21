menu = """
      _____              __         
     / ___/_____ _____  / /______ __
    / /__/ __/ // / _ \/ __/ -_) \ /
    \___/_/  \_, / .__/\__/\__/_\_\ 
     V:1.0.1/___/_/ @CythesOut
    Locks only exist to keep honest 
            people honest
-------------{Main menu}--------------         
|    options:          | Shortcodes: |
|  1.Encryption        |    (enc)    | 
|  2.Crackers          |    (crack)  |
|  3.Misc Tools        |    (misc)   |
|  4.Information       |    (i)      |
|  5.Exit/Quit         |    (e)      |
--------------------------------------
"""
encryptionMenu = """
----------{Encryption Menu}-----------         
|       options:       | Shortcodes: |
|----------------------|-------------|
|                      |             |
|  1.Hex               |    (hex)    | 
|  2.Base64            |    (b64)    |
|  3.SHA256            |    (256)    |
|                      |             |
|------{Ciphers*}------|-------------|
|                      |             |
|  1.Caesars Cipher    |    (cc)     |
|  2.Caesars Hacker    |    (ch)     |
|  3.Reverse Cipher    |    (rc)     |
|                      |             |
|--------{Menu}--------|-------------|
|                      |             |
|  1.Main Menu         |    (mm)     | 
|  2.Exit/Quit         |    (e)      |
|                      |             |
--------------------------------------
"""
crackerMenu = """
-----------{Cracker Menu}-------------         
|    options:          | Shortcodes: |
|  1.MD5 Cracker       |    (md5)    | 
|  2.Main Menu         |    (mm)     |
|  5.Exit/Quit         |    (e)      |
--------------------------------------
"""
miscMenu = """
-------------{MISC Menu}--------------         
|    options:          | Shortcodes: |
|  1.Password Generator|    (pg)     | 
|  2.QR Generator      |    (qr)     |
|  3.Main Menu         |    (mm)     |
|  5.Exit/Quit         |    (e)      |
--------------------------------------
"""

exitMessage = "\nGoodbye, Thank you for using Cryptex.\n\nHappy hacking!"

information = """
      -----------------{Program Information}-------------------
      | Author: @CythesOut(https://twitter.com/CythesOut)     |
      | Github: https://github.com/CythesOut                  |
      | Art:    https://patorjk.com/software/taag/            |
      ---------------------------------------------------------
      | Description:                                          | 
      | What started out as a basic encoder / decoder for hex |
      | turned into way more. Cryptex can now do everything it|
      | states on the main menu with more features being added|
      | as time goes on. While its still very basic I am      |
      | personally mega proud of it.                          |
      |                                                       |
      | How you can help:                                     |
      | Honestly its a cryptography program get involved any  |
      | way you think you might be able to. Be it testing,    |
      | adding features, custom art if you can think it.      |
      | I'm more than willing to see where it goes.           |
      | That is the beauty of open source.                    |
      |                                                       |
      | ABOVE ALL: Thank you for checking this out.           |
      | -Cy                                                   |
      ---------------------------------------------------------
"""
encrypt = """
   ____                       __ 
  / __/__  __________ _____  / /_
 / _// _ \/ __/ __/ // / _ \/ __/
/___/_//_/\__/_/  \_, / .__/\__/ 
                 /___/_/   
"""

decrypt = """   ___                        __
  / _ \___ __________ _____  / /_
 / // / -_) __/ __/ // / _ \/ __/
/____/\__/\__/_/  \_, / .__/\__/ 
                 /___/_/ 
"""

passlogo = """
   ___                                 __  _____                      __             
  / _ \___ ____ ____    _____  _______/ / / ___/__ ___  ___ _______ _/ /____  ____   
 / ___/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/   
/_/   \_,_/___/___/__,__/\___/_/  \_,_/  \___/\__/_//_/\__/_/  \_,_/\__/\___/_/      
                                            
"""
qrLogo = """
   ____    ____     ______                           __            
  / __ \  / __ \   / ____/__  ____  ___  _________ _/ /_____  _____
 / / / / / /_/ /  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /_/ / / _, _/  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
\___\_\/_/ |_|   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/                                                                     
"""
md5Logo = """
    __  _______  ______   ______                __            
   /  |/  / __ \/ ____/  / ____/________ ______/ /_____  _____
  / /|_/ / / / /___ \   / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
 / /  / / /_/ /___/ /  / /___/ /  / /_/ / /__/ ,< /  __/ /    
/_/  /_/_____/_____/   \____/_/   \__,_/\___/_/|_|\___/_/  
"""
reverseLogo = """
    ____                                   _______       __                 
   / __ \___ _   _____  _____________     / ____(_)___  / /_  ___  _____    
  / /_/ / _ \ | / / _ \/ ___/ ___/ _ \   / /   / / __ \/ __ \/ _ \/ ___/    
 / _, _/  __/ |/ /  __/ /  (__  )  __/  / /___/ / /_/ / / / /  __/ /        
/_/ |_|\___/|___/\___/_/  /____/\___/   \____/_/ .___/_/ /_/\___/_/         
                                              /_/     
"""

cclogo = """
   ______                              _______       __             
  / ____/___ ____  _________ ______   / ____(_)___  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  ) /_/ / /     / /___/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/      \____/_/ .___/_/ /_/\___/_/     
                                          /_/  
                
                ----------{Main menu}---------
                | Options:     | Shortcodes: | 
                | 1.Encrypt    | (enc)       |
                | 2.Decrypt    | (dec)       |
                | 3.Main Menu  | (mm)        |
                | 4.Exit/Quit  | (e)         |
                ------------------------------
"""
cclogo2 = """
   ______                              _______       __             
  / ____/___ ____  _________ ______   / ____(_)___  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  ) /_/ / /     / /___/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/      \____/_/ .___/_/ /_/\___/_/     
                                          /_/  
"""
chackerLogo = """
  _____                        __ __         __          
 / ___/__ ____ ___ ___ _____  / // /__ _____/ /_____ ____
/ /__/ _ `/ -_|_-</ _ `/ __/ / _  / _ `/ __/  '_/ -_) __/
\___/\_,_/\__/___/\_,_/_/   /_//_/\_,_/\__/_/\_\\__/_/                                                                   
"""

sha526logo = """   _____ __  _____   ___   ___________
  / ___// / / /   | |__ \ / ____/ ___/
  \__ \/ /_/ / /| | __/ //___ \/ __ \ 
 ___/ / __  / ___ |/ __/____/ / /_/ / 
/____/_/ /_/_/  |_/____/_____/\____/  
                                    
   ----------{Main menu}---------
   | Options:     | Shortcodes: | 
   | 1.Encrypt    | (enc)       |
   | 2.Back       | (back)      |   
   | 3.Main Menu  | (mm)        |
   | 4.Exit/Quit  | (e)         |
   ------------------------------
"""
hexMenu = """
   __ __                __        _            __
  / // /____ _____ ____/ /__ ____(_)_ _  ___ _/ /
 / _  / -_) \ / _ `/ _  / -_) __/ /  ' \/ _ `/ / 
/_//_/\__/_\_\\_,_/\_,_/\__/\__/_/_/_/_/\_,_/_/

    ----------{Main menu}---------
    | Options:     | Shortcodes: | 
    | 1.Encrypt    | (enc)       |
    | 2.Decrypt    | (dec)       |
    | 3.Back       | (back)      | 
    | 4.Main Menu  | (mm)        |
    | 5.Exit/Quit  | (e)         |
    ------------------------------
"""
b64Menu = """
        ___                 ____ ____
       / _ )___ ____ ___   / __// / /
      / _  / _ `(_-</ -_) / _ \/_  _/
     /____/\_,_/___/\__/  \___/ /_/ 

    ----------{Main menu}---------
    | Options:     | Shortcodes: | 
    | 1.Encrypt    | (enc)       |
    | 2.Decrypt    | (dec)       |
    | 3.Back       | (back)      | 
    | 4.Main Menu  | (mm)        |
    | 5.Exit/Quit  | (e)         |
    ------------------------------
"""

