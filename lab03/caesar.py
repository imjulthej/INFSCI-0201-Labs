class Caesar:
    def __init__(self, key=0):
        self._key = key

    def set_key(self, key):
        self._key = key

    def get_key(self):
        return self._key
    
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    shifted = ord(char) + self._key
                    ciphertext += chr((shifted - ord('a')) % 26 + ord('a'))
                else:
                    shifted = ord(char) + self._key
                    ciphertext += chr((shifted - ord('A')) % 26 + ord('A'))
            elif char.isspace():
                ciphertext += char
            else:
                ciphertext += chr((ord(char) + self._key) % 128)
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    shifted = ord(char) - self._key
                    plaintext += chr((shifted - ord('a')) % 26 + ord('a'))
                else:
                    shifted = ord(char) - self._key
                    plaintext += chr((shifted - ord('A')) % 26 + ord('A'))
            elif char.isspace():
                plaintext += char
            else:
                plaintext += chr((ord(char) - self._key) % 128)
        return plaintext

# Example
cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt("hello WORLD!"))
print(cipher.decrypt("khoor zruog$"))

cipher.set_key(6)
print(cipher.encrypt("zzz"))
print(cipher.decrypt("FFF"))

cipher.set_key(-6)
print(cipher.encrypt("FFF"))
print(cipher.decrypt("zzz"))
