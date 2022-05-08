#!/usr/bin/python

# leetspeek for [cryptex] project
# created by : Fyzz

# imports
import getopt
import sys

# help menu for cipheringing process
help_menu = """
      +-----------------------------------------------------+
      | [+] ARGUMENTS L33T 5P34K                            |
      | [+] ARG 1. Process                                  |
      |         [-e] ---------- Encrypt                     |
      |         [-d] ---------- Decrypt                     |      
      +-----------------------------------------------------+                                             
      | [+] ARG 2. Additional Aruments                      |
      |         [-t <plaintext>] --------- Input Text       | 
      |         [-i <input file>] -------- Input File [.txt]|
      |         [-o <output file>] ------- Output File      |
      +-----------------------------------------------------+
      | [+] Example:                                        |
      |         cryptex -l33t -e -t hello                   |
      +-----------------------------------------------------+
    """

#
leet_dictionary_enc = {
    "a":"4",
    "b":"8",
    "e":"3",
    "g":"6",
    "h":"#",
    "i":"1",
    "o":"0",
    "r":"2",
    "s":"5",
    "t":"7"
}

leet_dictionary_dec = {
    "4":"a",
    "8":"b",
    "3":"e",
    "6":"g",
    "#":"h",
    "1":"i",
    "0":"o",
    "2":"r",
    "5":"s",
    "7":"t"
}

# encode leet
def encode_leet(plain_content, print_cnt):

    encoded_cnt = plain_content.lower()
    output = ''

    for character in encoded_cnt:
        if character in leet_dictionary_enc:
            output += leet_dictionary_enc[character]
        else:
            output += character

    # output content to cli
    if print_cnt == True:
        print(f'\nEncrypted Content:\n{output.capitalize()}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output.capitalize())
        print('Output written to file sucessfully')

# decode leet
def decode_leet(plain_content, print_cnt):

    encoded_cnt = plain_content.lower()
    output = ''

    for character in encoded_cnt:
        if character in leet_dictionary_dec:
            output += leet_dictionary_dec[character]
        else:
            output += character

    # output content to cli
    if print_cnt == True:
        print(f'Encrypted Content:\n{output.capitalize()}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output.capitalize())
        print('Output written to file sucessfully')

# parse all arguments
def leet_parser():
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
            arguments = leet_parser()

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

            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encodes leet
                if ciphering_process == '-e':
                    encode_leet(inputted_content, print_content)

                # decodes leet
                elif ciphering_process == '-d':
                    decode_leet(inputted_content, print_content)

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
def leet_main():

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
    leet_main()