import os
from affine import Affine
from atbash import Atbash
from keyword_cipher import Keyword


def clear_screen():
    """clears screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def quit():
    "This quits the application"
    print("Thank you for your time. Goodbye.")
    exit()

def main():
    cipher = ""
    print("Welcome to the Secret Messages project\n")
    print("**** Press 'q' at anytime to exit this program ****\n")
    print("Below are the available ciphers. Please pick one.")
    ciphers = ['Affine', 'Atbash', 'Keyword']
    for cipher in ciphers:
        print("-{}".format(cipher))

    while True:

        cipher_choice = input("Which cipher would you like to use? ")
        clear_screen()
        if cipher_choice.lower() == 'affine':
            cipher = Affine()
        elif cipher_choice.lower() == 'atbash':
            cipher = Atbash()
        elif cipher_choice.lower() == 'keyword':
            keyword = input("What would you like your keyword to be? ")
            cipher = Keywords(keyword)
        elif cipher_choice.lower() == 'q':
            quit()
        else:
            print("I'm sorry. Please choose a cipher from the list.")

        choice = input("Would you like encrypt or decrypt a message? ")

        message = input("What message would you like to {}? ".format(choice))

        if choice.lower() == 'encrypt':
            cipher.encrypt(message)
        elif choice.lower() == 'decrypt':
            cipher.decrypt(message)
        elif cipher_choice.lower() == 'q':
            quit()
        else:
            print("Please choose either encryption or decryption.")


if __name__ == "__main__":
    main()
