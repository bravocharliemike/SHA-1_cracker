from password_cracker import crack_sha1_hash


def test_crack_sha1_hash_1():
    expected = "[+] Cracked: sammy123"  # include here a clear text password
    actual = crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec")
    assert actual == expected


def test_crack_sha1_hash_2():
    expected = "[+] Cracked: abacab" 
    actual = crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e")
    assert actual == expected


def test_crack_sha1_hash_3():
    expected = "[+] Cracked: password"
    actual = crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
    assert actual == expected


def test_crack_sha1_hash_4():
    expected = "[-] Not found in database"
    actual = crack_sha1_hash("91e692cb8cb1da51963da68abbe7cf1b2044bd79")
    assert actual == expected


def test_crack_sha1_hash_salted_1():
    expected = '[+] Cracked: superman'
    actual = crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
    assert actual == expected


def test_crack_sha1_hash_salted_2():
    expected = '[+] Cracked: q1w2e3r4t5'
    actual = crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)
    assert actual == expected

def test_crack_sha1_hash_salted_3():
    expected = '[+] Cracked: bubbles1'
    actual = crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True)
    assert actual == expected


