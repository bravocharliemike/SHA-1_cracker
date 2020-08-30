import hashlib

def crack_sha1_hash(hash: str) -> str:
    # Prepare the file for hashing the cleartext passwords
    with open('top-10000-passwords.txt') as fin:
        data = fin.readlines()

    # Key is clear text password and value its hash digest in hex
    hash_dict = {}
    # Loop over the entire file creating single passwords for hashing
    for line in data:
        clear_password = line.strip()
        hashed_pwd = hashlib.sha1(clear_password.encode())
        hex_format = hashed_pwd.hexdigest()     # Hexadecimal format of SHA-1 hash
        hash_dict[clear_password] = hex_format

    # Check if the hash has matching clear text password
    for k, v in hash_dict.items():
        if hash == v:
            return 'The password is ' + k

    return "PASSWORD NOT IN DATABASE"   # The password was not cracked


# Testing the function
# Password should crack and equal goldfish
cracked_password1 = crack_sha1_hash("fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
print(cracked_password1)

# Password should crack and equal football
cracked_password2 = crack_sha1_hash("2d27b62c597ec858f6e7b54e7e58525e6a95e6d8")
print(cracked_password2)

# Password should crack and equal master
cracked_password3 = crack_sha1_hash("4f26aeafdb2367620a393c973eddbe8f8b846ebd")
print(cracked_password3)

# Password should not crack but it's equal to ambulancia
cracked_password4 = crack_sha1_hash("98d58c0a38d8a9aa221ec88cf6514df80d1bf944")
print(cracked_password4)

