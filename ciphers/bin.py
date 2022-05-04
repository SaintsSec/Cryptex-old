#!/usr/bin/python
# binary [enc | dec] for Cryptex

# imports
import sys
import getopt

# help menu for ciphering process
help_menu = """
        [+] ARGUMENTS Binary
        [+] ARG 2. Additional Aruments
                [-t <plaintext>] --------- Input Text
                [-i <input file>] -------- Input File [.txt]
                [-o <output file>] ------- Output File

        [+] Example:
        cryptex -bin -e -t hello
        """

# encrypt binary
def encrypt(plain_content, print_cnt):
    output = ' '.join(format(ord(x), 'b') for x in plain_content)

    # output content to cli
    if print_cnt == True:
        print(f'Binary:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# decrypt binary
def decrypt(plain_content, print_cnt):
    binary_list = plain_content.split(' ')
    print(plain_content)
    print(binary_list)
    output = ''

    for binary in binary_list:
        output += chr(int(binary, 2))

    # output content to cli
    if print_cnt == True:
        print(f'Decoded Content:\n{output}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(output)
        print('Output written to file sucessfully')

# parse all arguments
def binary_parser():
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
            arguments = binary_parser()

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
                    inputted_content = inputted_content[2::2]

                # file does not exist
                except FileNotFoundError:
                    print('[!!] he attached file does not exist')

            # checks if output was specified
            if ('-o' in arguments):
                print_content = arguments.get('-o')

            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encodes binary
                if ciphering_process == '-e':
                    encrypt(inputted_content, print_content)

                # decodes binary
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
def binary_main():

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
    binary_main()
