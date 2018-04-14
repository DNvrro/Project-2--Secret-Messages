import os

from affine import Affine
from atbash import Atbash
from keyword_cipher import Keyword


def clear_screen():
    """clears screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def quit_program():
    """This quits the application"""
    print("Thank you for your time. Goodbye.")
    exit()


def greeting():
    print("\nWelcome to the Secret Messages project\n")
    print("**** Press 'q' at anytime to exit this program ****\n")


def secret():

    while True:
        cipher = ''
        print("\nBelow are the available ciphers. Please pick one.")
        ciphers = ['Affine', 'Atbash', 'Keyword']
        for cipher in ciphers:
            print("-{}".format(cipher))

        cipher_choice = input("\nWhich cipher would you like to use? ")
        clear_screen()
        if cipher_choice.lower() == 'affine':
            cipher = Affine()
        elif cipher_choice.lower() == 'atbash':
            cipher = Atbash()
        elif cipher_choice.lower() == 'keyword':
            keyword = input("What would you like your keyword to be? ")
            cipher = Keyword(keyword)
        elif cipher_choice.lower() == 'q':
            quit_program()
        else:
            print("I'm sorry. Please choose a cipher from the list.")
            secret()

        message = input("What would you like your message to be? ")

        choice = input("Would you like to encrypt or decrypt a message? ")

        if choice.lower() == 'encrypt':
            cipher.encrypt(message)
        elif choice.lower() == 'decrypt':
            cipher.decrypt(message)
        elif choice.lower() == 'q':
            quit_program()
        elif choice.lower() != 'encrypt' or 'decrypt':
            print("Please choose either encryption or decryption.")
            secret()


if __name__ == "__main__":
    greeting()
    secret()
