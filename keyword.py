from ciphers import cipher

import string


class Keyword(Cipher):

    def __init__(self, keyword='keyword'):
        """
        Initializes the Keyword class & creates a list containing
        the letters of the alphabet. The for loop rids the keyword
        of any repeated letters

        """


        self.alpha = list(string.ascii_uppercase)
        self.keyword = []
        for letter in keyword.upper():
            if letter not in keyword:
                self.keyword.append(letter)


    def encrypt(self, txt):
        


