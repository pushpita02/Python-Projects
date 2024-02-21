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

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    length = int(input("Enter password length: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generate_random_password()