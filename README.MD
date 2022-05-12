<!-- variables -->
[ccs]: https://www.cosmodiumcs.com
[saints]: https://www.saintssec.com
[youtube]: https://www.youtube.com/c/CosmodiumCS

<!-- title -->
# Cryptex [INCOMPLETE]
---

<!-- image -->
<img src="https://github.com/AlexKollar/Cryptex/blob/gh-pages/Gallery/Lock.png" width="285"/></p>

> "Locks only exist to keep honest people honest" 

## Overview:
Cryptex is an advanced cryptography hacking tool created by a joint development between [The SAINTS][saints] and [Cosmodium CyberSecurity][ccs]. It was originally two separte tools, one reffered to as "Cryptex" and the other as "[The Codex Project](https://github.com/CosmodiumCS/the-codex-project)". But on May 2, 2022, the lead developers [Cythes](https://github.com/AlexKollar) and [Blue Cosmo](https://github.com/CosmodiumCS) joined forces to build a central cryptography tool. Since then, plenty of others have joined the project to build it into what we one day hope to be, the "Metasploit of Cryptography".

Cryptex is capable of advanced encryption, decryption, and breaking ciphers through various mehtods. These methods include but are not limited to bruteforcing, cryptographic wordlising, letter frequencies, plaintext formatting, and cracking.

## Resources:
- [YouTube Video]()
- [YouTube Channel][youtube]
- [Saints Site][saints]
- [Cosmodium Site][ccs]

## Requirements:
- Debian based Linux OS
- Python 3.x

## Set-Up & Installation:
1. Clone repository
```
git clone https://github.com/AlexKollar/Cryptex.git
```
2. Execute installer
  - **YES** the Cryptex directory **IS** supposed to dissapear
```
cd Cryptex
sh install.sh
```
3. Restart your terminal

## Executing Cryptex
Run the following for help
```
cryptex --help
```
- The help menu will return a list of all available ciphers
- You can append the flag for a cipher after `cryptex` to get help for a cipher
- Here as an example for the Caesar Cipher `cc`
```
cryptex cc
``` 
- The returned arguments can be passed in addition
- These arguments are the most popular among the ciphers
- `-e` - encryption
- `-d` - decryption
- `-b` - breaking/bruteforcing
- `-k` - encryption key
- `-t` - input text
- `-i` - input file
- `-o` - output file
- However, each cipher will have its own uniqe arguments for additional features
```
cryptex cc -e -t "hello world" -k 5
```

## Cryptconsole:
The Cryptconsole is a more expansive way of using Cryptex. It allows the user to open a console in their terminal connected to the Cryptex libraries; comparable to [Metasploit](https://www.metasploit.com/) or [OnlyRAT](https://github.com/CosmodiumCS/OnlyRAT). The Cryptconsole can allow users to run multiple ciphers back to back to back.
- We can execute the cryptconsole by running the following
```
cryptex
```
- Now multiple ciphers can be run back to back with ease
```
[~] root@cryptex $ cc -e -t "hello world" -k 5
...
[~] root@crytpex $ vc -e -t "hello world" -k hello
```
- Cryptex also has various commands for console interaction
- `help` - displays help menu
- `update` - updates crytpex to latest version
- `version` - displays current version
- `exit` - exits cryptconsole
- Any other command are run through the commandline

## Updating Cryptex:
The development team will continuously be pushing out new versions of Cryptex. To prevent users from continously having to clone the repository, we made an update function.
- Argument Parsing
```
cryptex --update
```
- CryptConsoloe
```
cryptex
[~] root@crytpex $ update
```

## Uninstalling Cryptex:
If at anypoint you are unsatisfied or need to rid of the cryptex project [and its awesomeness]. You can run the following to get it off of your computer.
- Argument Parsing
```
cryptex --remove
```
- CryptConsoloe
```
cryptex
[~] root@crytpex $ remove
```
## All Release Versions

| Version | Name                  |
|---------|-----------------------|
| 0.1     | Earth Invader         |
| 0.2     | Oven Sandwich         |
| 0.3     | Back Door Bytes       |
| 0.4     | Tentacle Grape        |
| 0.5     | Cryptic Fun Facts     |
| 0.6     | Knowloon Showdown     |
| 0.9     | The Game              |
| 1.0     | Industry Invader      |

---

## Current

## 0.05

| Version | Name                  |
|---------|-----------------------|
| 0.05    |                       |
---

## Next

| Version | Name                  |
|---------|-----------------------|
| 0.1     | Earth Invader         |

---

## About Us
**[Cythes](https://twitter.com/CythesOut): Project Manager**
I started learning computers around middle school age with my discovery & passion of PC Gaming.  A few years later I'd stumbled into Ubuntu 8.04 soon started learning programming, hacking on and off, while over the next decade working on projects ranging from Android personal safety applications to light game development.

My current obsession being the development of a cryptography toolkit aptly named CrypteX as part of CICADA while attempting to avoid SVT from all the caffeine I main line in a given day.

**[BlueCosmo](https://twitter.com/CosmodiumCS): Lead Developer**
Started Cosmodium at 17 and since then has made significant changes in the cybersecurity community.  A reasonably known content creator and python programming whiz to say the least.    
  
**[Fyzz](): Lead Developer**   
...

**[Mart](): Developer**
I started tinkering with computers I think around primary school, then in junior high school I started doing more tech stuff, then in high school I started learning more proper programming, and I began to do a lot of programming in my spare time, and at school, but I was always at least 10 steps ahead of what my class was learning, and eventually I ended up finding this place.

**[Soul](): Developer**
...

**Enjoy! If you like what you see, consider hitting that sponosor button! :)**

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)  
![status](https://img.shields.io/pypi/status/st?logo=git&style=plastic)
![commits](https://img.shields.io/github/last-commit/CythesOut/Cryptex?logo=github)
![downloads](https://img.shields.io/github/downloads/CythesOut/Cryptex/total) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/9666bf9839f94e47b28c786b426fa5e4)](https://www.codacy.com/gh/AlexKollar/Cryptex/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AlexKollar/Cryptex&amp;utm_campaign=Badge_Grade)</p>
