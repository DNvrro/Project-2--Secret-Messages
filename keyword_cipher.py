import string

from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self, keyword="keyword"):
        """
        Initializes the Keyword class & creates a list containing
        the letters of the alphabet. The for loop rids the keyword
        of any repeated letters. Default keyword is "keyword".

        """

        self.keyword = []
        self.alpha = list(string.ascii_uppercase)

        for letter in keyword.upper():
            if letter not in self.keyword:
                self.keyword.append(letter)

    def encrypt(self, txt):
        """
        Encrypts the txt by using the keyword. The alphabet is is placed into
        a dict where the values begin w/ the keyword proceeded by the beginning
        of the alphabet. The values being the encrypted alphabet
        Ex. A:K, B:E, C:Y, D:W, E:O, F:R, G:D, H:A, I:B, etc.

        """

        txt = txt.upper()
        encrypted_txt = []
        cipher_letters = []
        cipher_letters[:len(self.keyword)] = self.keyword

        cipher_letters.extend(
            [letter for letter in self.alpha if letter not in cipher_letters])

        cipher_key = {key: value for key, value in
                      zip(self.alpha, cipher_letters)}

        for letter in txt:
            if letter in cipher_key.keys():
                encrypted_txt.append(cipher_key[letter])
            else:
                encrypted_txt.append(letter)
        print("".join(encrypted_txt))

    def decrypt(self, txt):
        """
        Decrypts the txt by using the keyword. The alphabet is is placed into
        a dict where the keys begin w/ the keyword proceeded by the beginning
        of the alphabet. The values being the decrypted alphabet
        Ex. K:A, E:B, Y:C , W:D , O:E , R:F , D:G , A:H , B:I , etc.

        """

        txt = txt.upper()
        decrypted_txt = []
        cipher_letters = []
        cipher_letters[:len(self.keyword)] = self.keyword

        cipher_letters.extend(
            [letter for letter in self.alpha if letter not in cipher_letters])
        cipher_key = {key: value for key, value in
                      zip(cipher_letters, self.alpha)}

        for letter in txt:
            if letter in cipher_key.keys():
                decrypted_txt.append(cipher_key[letter])
            else:
                decrypted_txt.append(letter)
        print("".join(decrypted_txt))

