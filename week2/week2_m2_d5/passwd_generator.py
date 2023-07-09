#!/usr/bin/env python


import string
import random


def crea_password(grandezza):
    letters = string.ascii_lowercase + string.digits + string.punctuation
    combinazione = "".join(random.choice(letters) for i in range(grandezza))
    print(f"La grandezza della password è di: {grandezza} caratteri\n")
    print(f"La password è: {combinazione}\n")
    return combinazione


crea_password(15)