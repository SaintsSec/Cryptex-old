#!/usr/bin/python

# reverse cipher package for the the codex project
# created by : C0SM0

# imports
import sys
import getopt

# help menu for ciphering process
help_menu = """
      +------------------------------------------------------+
      |  [+] ARGUMENTS Hexadecimal                           |
      |  [+] ARG 2. Additional Aruments                      |
      |          [-t <plaintext>] --------- Input Text       |
      |          [-i <input file>] -------- Input File [.txt]|
      |          [-o <output file>] ------- Output File      |
      +------------------------------------------------------+  
      |  [+] Example:                                        |
      |          cryptex -hex -t hello                       |  
      +------------------------------------------------------+
    """

# encode hex
def encrypt(plain_content, print_cnt):
    # encode to hex
    output = plain_content.encode("utf-8").hex()

    # output content to cli
    if print_cnt == True:
        print(f'\nEncrypted Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# decode hex
def decrypt(plain_content, print_cnt):
    # decode to hex
    output = bytes.fromhex(plain_content).decode("utf-8")

    # output content to cli
    if print_cnt == True:
        print(f'Decoded Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# parse all arguments
def parser():
    opts, args = getopt.getopt(sys.argv[2:], 'i:t:o:', ['inputFile', 'inputText', 'outputFile'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
        # input options
        if opt == '-i':
            arg_dict['-i'] = arg
        if opt == '-t':
            arg_dict['-t'] = arg

        # output options
        if opt == '-o':
            arg_dict['-o'] = arg

    return arg_dict

# command line interface
def cli(argument_check):

    # one liners
    if argument_check == True:

        # tries to get all arguments
        try:
            arguments = parser()

        # catches arguments with no value
        except getopt.GetoptError:
            print(f'[!!] No value was given to your argument\n{help_menu}')

        # continues with recieved arguments
        else:    
            # getting variables for ciphering process
            inputted_content = arguments.get('-t')
            print_content = True
            
            # checks users output type
            if ('-i' in arguments):
                # tries to read file
                try:
                    inputted_content = open(arguments.get('-i'), 'r').read()

                # file does not exist
                except FileNotFoundError:
                    print('[!!] he attached file does not exist')

            # checks if output was specified
            if ('-o' in arguments):
                print_content = arguments.get('-o')

            # check ciphering process
            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encodes base64
                if ciphering_process == '-e':
                    encrypt(inputted_content, print_content)

                # decodes base64
                elif ciphering_process == '-d':
                    decrypt(inputted_content, print_content)

                # exeption
                else:
                    print(f'[!!] No Key or Argument was specified\n{help_menu}')

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu 
    else:
        print(help_menu)

# main code
def reverse_main():

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# runs main function if file is not being imported
if __name__ == '__main__':
    reverse_main()
