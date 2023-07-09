#!/usr/bin/env python


import string
import random


def crea_password(grandezza):
    caratteri = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    combinazione = "".join(random.choice(caratteri) for i in range(grandezza))
    print(f"\nLa grandezza della password è di: {grandezza} caratteri\n")
    print(f"La password è: {combinazione}\n")
    return combinazione


crea_password(15)