import hashlib

def crackMD5():
    wordlist_location = str(input('Enter wordlist file location: '))
    hash_input = str(input('Enter hash to be cracked: '))

    with open(wordlist_location, 'r') as file:
        for line in file.readlines():
            hash_ob = hashlib.md5(line.strip().encode())
            hashed_pass = hash_ob.hexdigest()
            if hashed_pass == hash_input:
                print(f"Found cleartext password: \n{line.strip()}")