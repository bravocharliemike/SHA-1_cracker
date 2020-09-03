import hashlib
import argparse

# Initialise parser object to handle command line arguments
parser = argparse.ArgumentParser(description='Attempts to crack a SHA-1 password hash.')
parser.add_argument('hash', action='store', help='SHA-1 hash to crack.')
parser.add_argument('passfile', action='store', help='file with passwords to search.')
parser.add_argument('--salted', '-s', dest='use_salts', action='store_true', help='set parameter use_salts to True.')

arguments = parser.parse_args()


def crack_sha1_hash(hash, use_salts=False):
    """
    The function takes in a SHA-1 hash of a password and returns the password if it is one of the passwords stored in the passfile used. 
    If the SHA-1 hash is NOT of a password in the database, return "Not found in database".
    
    The function hashes each password from the passfile and compare it to the hash passed into the function.
    
    The function takes an optional second argument named use_salts. If set to true, each salt string from the file `known-salts.txt` 
    is appended and prepended to each password from the passfile before hashing and before comparing it to the hash 
    passed into the function.
    """

    # Prepare the file for hashing the cleartext passwords
    with open(arguments.passfile) as fin:
        passwords = fin.read()

    # Key is hex digest and value the clear text password
    hashed_passwords = dict()

    # Loop over the entire file creating single passwords for hashing
    for password in passwords.split('\n'):
        single_pwd = password
        if use_salts:
            with open('known-salts.txt') as f:
                salts = f.read().split()
                for salt in salts:
                    for password in passwords.split('\n'):
                        single_pwd_1 = salt + password + salt
                        hashed_pwd = hashlib.sha1(single_pwd.encode())
                        hex_pwd = hashed_pwd.hexdigest()
                        hashed_passwords[hex_pwd] = password

        hashed_pwd = hashlib.sha1(single_pwd.encode())
        hex_pwd = hashed_pwd.hexdigest()
        hashed_passwords[hex_pwd] = single_pwd

    # Check if the hash has matching clear text password
    for digest, clear_pwd in hashed_passwords.items():
        if hash == digest:
            return f'[+] Cracked: {clear_pwd}'

    return '[-] Not found in database'   # The password was not cracked


def main():
    cracked = crack_sha1_hash(arguments.hash, arguments.use_salts)
    print('\nAttempting to crack...\n')
    print(cracked)


if __name__ == '__main__':
    main()
