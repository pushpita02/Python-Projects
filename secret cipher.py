#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Pushpita
#
# Created:     21/02/2024
# Copyright:   (c) Pushpita 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

def encrypt(plaintext, secret_key):
     ciphertext=""
     for character in plaintext:
        if character.isalpha():
            character=character.lower()
            char_index=alphabet.index(character)
            new_inddex=(char_index + secret_key) % 26
            cioher_char=alphabet[new_index].upper()
        else:
            cipher_char=character

        ciphertext += cipher_char

        print("Your ciphertext is: "+ ciphertext)
def decrypt(ciphertext, secret_key):
    plaintext = ""
    for character in ciphertext:
        if character.isalpha():
            character=character.lower()
            char_index=alphabet.index(character)
            new_index=(char_index - secret_key) % 26
            plain_char=alphabet[new_index]
        else:
            plain_char=character
        plaintext += plain_char
    print("Your plaintext id: " + plaintext)
