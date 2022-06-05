# high security password generator in python, written by vali-github
# Copyright © Alperen Yilmaz aka. vali-github 2022 - All Rights Reserved

import random
import string

def generate_password(length):
    # Generate a random password with multiple strings with 16 chars (ascii, digits, punctuation)
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password) for i in range(length))

print(generate_password(16))