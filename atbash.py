import string

from ciphers import Cipher


class Atbash(Cipher):

    def __init__(self):
        """
        Initializes the Atbash class & creates variables for
        the alphabet and the alphabet reversed
        """
        self.alpha = string.ascii_uppercase
        self.reverse_alpha = self.alpha[::-1]

    def encrypt(self, txt):
        """
        Encrypts the txt by creating a dict where each key is a letter
        of the alphabet & its value its reversed counter part.
        Ex. A:Z, B:Y, C:X, etc.


        """

        txt = txt.upper()
        encrypted_txt = []
        encrypt = {}

        for x in range(26):
            encrypt[self.alpha[x]] = self.reverse_alpha[x]

        for letter in txt:
            if letter in encrypt:
                encrypted_txt.append(encrypt[letter])
            else:
                encrypted_txt.append(letter)

        return "".join(encrypted_txt)

    def decrypt(self, txt):
        """
        Decrypts the txt by creating a dict where each key is a letter
        of the reversed alphabet & its value its standard alphabetical
        counter part.
        Ex. Z:A, Y:B, X:C, etc.

        """

        txt = txt.upper()
        decrypted_txt = []
        decrypt = {}

        for x in range(26):
            decrypt[self.reverse_alpha[x]] = self.alpha[x]

        for letter in txt:
            if letter in decrypt:
                decrypted_txt.append(decrypt[letter])
            else:
                decrypted_txt.append(letter)
        return "".join(decrypted_txt)
