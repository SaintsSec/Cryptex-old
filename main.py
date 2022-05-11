#!/usr/bin/python
# New Arg Parse and Cipher Call
# created by : Fyzz

import argparse
import mods.bits as b
import importlib
import readline
import sys
import os


def update():

    print("\n[*] Checking for updates...")

    # get latest version nubmer
    os.system(f"curl https://raw.githubusercontent.com/AlexKollar/Cryptex/master/version.txt | tee ~/.Cryptex/latest.txt")

    # save version nubmers to memory
    current_version = float(open(f"{b.local_path}/version.txt", "r").read())
    latest_version = float(open(f"{b.local_path}/latest.txt", "r").read())

    # remove version number file
    os.system("rm -rf ~/.Cryptex/latest.txt")

    # if new version is available, update
    if latest_version > current_version:
        print("\n[+] Update found")
        print("[~] Update Cryptex? [y/n]\n")

        # user input, option
        option = input(f"{b.header}")

        # update
        if option == "y":
            os.system(f"sh ~/.Cryptex/resources/update.sh")

    # otherwise, run main code
    else:
        print("\n[+] Cryptex already up to date")

# Output
def output(data, output): 
    if data:
        if data[1] == True and data[1]:
            #File
            if output:
                with open(output, 'w') as f:
                    f.write(data[0])
                print(f'{b.SUCCESS}[✓] File Output Successful{b.END}')

            #CLI
            else:
                print(f'\n{b.SUCCESS}[✓] Output:{b.END}\n{data[0]}\n')
        else:
            #Fail Catch
                print(f'\n{b.FAIL}[✖] Failed:{b.END}\n{data[0]}\n')


# Main
def cli(args_exist):

    if args_exist:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print(b.help_menu)
        else:
            parser = argparse.ArgumentParser(add_help=False, usage="")
            parser.add_argument('cipher', type=str)
            parser.add_argument('-e', '--encode', dest='encode', action='store_true')
            parser.add_argument('-d', '--decode', dest='decode', action='store_true')
            parser.add_argument('-b', '--brute', dest='brute', action='store_true')
            parser.add_argument('-i', '--input', dest='input', type=str)
            parser.add_argument('-o', '--output', dest='output', type=str)
            parser.add_argument('-t', '--text', help='String Input\n', dest='text', type=str)
            parser.add_argument('-k', '--key', help='Int Key\n', dest='key', type=str)
            parser.add_argument('-ex', '--exclude', help='Exclude Character\n', dest='exclude', type=str)
            parser.add_argument('-w', '--wordlist', help='Wordlist File\n', dest='wordlist', type=str)
            parser.add_argument('-r', '--range', help='Range\n', dest='range', type=str)
            args = parser.parse_args()

            if args.input:
                args.text = open(args.input, 'r').read()

            try:
                module = importlib.import_module(f'ciphers.{args.cipher}')
            except:
                print(f"{b.FAIL}\n[✖] Cipher May Not Exist\nTry 'cryptex -h' to see all ciphers{b.END}\n")
            else:
                if args.encode:
                    output(module.encode(args), args.output)
                elif args.decode:
                    output(module.decode(args), args.output)
                elif args.brute:
                    output(module.brute(args), args.output)
                else:
                    print(module.help_menu)
    else:
        # display banner
        print(b.banner)
        print('[~] Type "help" for help menu :')

        # loop code
        while True:
            # get user input
            user_input = input(b.header)

            if user_input == 'help':
                print(b.help_menu)

            elif user_input == 'version':
                print(version)

            elif user_input == 'exit' or user_input == 'quit':
                exit()
                break

            elif user_input == 'update':
                update()

            elif user_input == 'clear':
                os.system('clear')

            else:
                # Runs Main Again With Console ARGS
                
                os.system(f'python3 main.py {user_input.replace("cryptex", "")}')
                        
                # otherwise, run input through the commandline
                # else:
                #     os.system(user_input)

def main():
    try:
        sys.argv[1]
    except IndexError:
        args_exist = False
    else:
        args_exist = True
    
    cli(args_exist)

if __name__ == '__main__':
    main()