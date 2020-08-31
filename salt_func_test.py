import hashlib


def salt_passwords(file, use_salts=True):
    with open(file) as fin:
        data = fin.read().split()

    if use_salts:
        with open('salts.txt') as f:
            contents = f.read().split()
            salted_passwords = []
            for salt in contents:
                for password in data:
                    salted = salt + password + salt
                    salted_passwords.append(salted)
            # Write the lines to a new file
            final_file = open('final_passwords', 'w')
            for i in salted_passwords:
                i = hashlib.sha1(i.encode())
                final_file.write(i.hexdigest() + '\n')
            final_file.close()
    else:
        print(data)


salt_passwords('passwords.txt', use_salts=True)