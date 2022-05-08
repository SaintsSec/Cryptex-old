#!/usr/bin/python
# New Template for the the codex project
# created by : Fyzz

# imports
import getopt
import sys

#---------------------------------------------------------------------------------| Help Menu |
# Make sure to edit this for your specific cipher
help_menu = """
      +------------------------------------------------------+
      |  [+] ARGUMENTS Phonetic Alphabet                     |
      |  [+] ARG 1. Process                                  |
      |          [-e] ---------- Encrypt                     |
      |          [-d] ---------- Decrypt                     |
      +------------------------------------------------------+
      |  [+] ARG 2. Additional Aruments                      |
      |          [-t <plaintext>] --------- Input Text       |
      |          [-i <input file>] -------- Input File [.txt]|
      |          [-o <output file>] ------- Output File      |
      +------------------------------------------------------+ 
      |  [+] Example:                                        |
      |          cryptex -pho -e -t hello                    |
      +------------------------------------------------------+
        """

phonetic ={
        "A" : "Alfa",
        "B" : "Brava",
        "C" : "Charlie",
        "D" : "Delta",
        "E" : "Echo",
        "F" : "Foxtrot",
        "G" : "Golf",
        "H" : "Hotel",
        "I" : "India",
        "J" : "Juliett",
        "K" : "Kilo",
        "L" : "lima",
        "M" : "Mike",
        "N" : "November",
        "O" : "Oscar",
        "P" : "Papa",
        "Q" : "Quebec",
        "R" : "Romeo",
        "S" : "Sierra",
        "T" : "Tango",
        "U" : "Uniform",
        "V" : "Victor",
        "W" : "Whiskey",
        "X" : "X-Ray",
        "Y" : "Yankee",
        "Z" : "Zulu",
        " " : "(space)"
        }

phoneticInverse = dict((v,k) for (k,v) in phonetic.items())

#-----------------------------------------------------------------------------------| Encoding |
def encode(plain_content, print_cnt):

    encoded_cnt = plain_content.upper() # This is the string input for -t or -i
    output = []

    for character in encoded_cnt:
        if character in phonetic:
            output.append(phonetic[character])
        else:
            output.append(character)
         
    # output content to cli
    if print_cnt == True:
        print(f'\nEncrypted Content:\n{" ".join(output)}\n')

    # output content to file
    else:
        with open(print_cnt, 'w') as f:
            f.write(" ".join(output))
        print('Output written to file sucessfully')

#-----------------------------------------------------------------------------------| Decoding |
def decode(plain_content, print_cnt):

    encoded_cnt = plain_content.split(" ") # This is the string input for -t or -i
    output = ''

    for character in encoded_cnt:
        if character in phoneticInverse:
            output += phoneticInverse[character]
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

# -------------------------------------------------------------------------------| Arg Parsing |
# Add more args here if there are more than the default -t -i -o [ Example: -k ]
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


# ---------------------------------------------------------------------------------| CLI Args |
# Edit this if you have more than the default -t -i -o [ Example: -k ]
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

            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encodes octal
                if ciphering_process == '-e':
                    encode(inputted_content, print_content)

                # decodes octal
                elif ciphering_process == '-d':
                    decode(inputted_content, print_content)
                
                # exeption
                else:
                    print(f'[!!] No Key or Argument was specified\n{help_menu}')

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu 
    else:
        print(help_menu)


# ---------------------------------------------------------------------------------| Main Code |
# [!!] Shouldnt have to edit this 
def main_code():

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
    main_code()