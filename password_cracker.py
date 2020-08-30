import hashlib

#def crack_sha1_hash(hash):

with open('top-10000-passwords.txt') as fin:
    data = fin.readlines()
    # Loop over the entire file creating single passwords for hashing
    for line in data:
        single_password = line.strip()
        hashed_pwd = hashlib.sha1(single_password.encode())
        hex_format = hashed_pwd.hexdigest()     # Hexadecimal format of SHA-1 hash

        if hex_format == '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684':
            print(f'Found password and it is {hex_format}')