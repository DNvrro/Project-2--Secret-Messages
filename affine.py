import string

from ciphers import Cipher


class Affine(Cipher):

    def __init__(self):
        self.letters = string.ascii_uppercase
        # creates a dict assigning each letter of the alphabet a numeric value
        self.letter_keys = {key: value for key, value in zip(self.letters,
                                                             range(26))}

    def encrypt(self, txt):
        """
        Encrypts string using the affine formula
        (3x + 7)  % 26. 65 is added to the final
        value to obtain the encrypted letter

        """

        txt = txt.upper()
        encrypted_txt = []

        for letter in txt:
            if letter in self.letter_keys.keys():
                (encrypted_txt.append(chr((self.letter_keys[letter]
                                           * 3 + 7) % 26 + 65)))
            else:
                encrypted_txt.append(letter)
        print("".join(encrypted_txt))

    def decrypt(self, txt):
        """
        Decrypts the string using the formula
        9(x - 7) % 26. 9 being the multiplicitive
        inverse of 3 which was used in the Encrpyt.
        formula. Again, 65 is added to obtain the
        decrypted letter

        """

        txt = txt.upper()
        decrypted_txt = []

        for letter in txt:
            if letter in self.letter_keys.keys():
                (decrypted_txt.append(chr(((self.letter_keys[letter] - 7)
                                           * 9) % 26 + 65)))
            else:
                decrypted_txt.append(letter)
        print("".join(decrypted_txt))



