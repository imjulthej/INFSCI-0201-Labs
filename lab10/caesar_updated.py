def shift_char(c, key):
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        return chr((ord(c) - base + key) % 26 + base)
    elif c.isspace():
        return c
    else:
        return chr((ord(c) + key) % 128)

def encrypt(text, key):
    return ''.join(map(lambda c: shift_char(c, key), text))

def decrypt(text, key):
    return ''.join(map(lambda c: shift_char(c, -key), text))

# Example
def main():
    print(encrypt("hello WORLD!", 3))
    print(decrypt("khoor ZRUOG$", 3))

    print(encrypt("zzz", 6))
    print(decrypt("FFF", 6))

    print(encrypt("FFF", -6))
    print(decrypt("zzz", -6))

if __name__ == "__main__":
    main()