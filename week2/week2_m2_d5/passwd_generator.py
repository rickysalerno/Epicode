#!/usr/bin/env python


""" L'applicazione creera un generatore di password """


import string
import random


def crea_password():
    """ Creazione Pass In base alla complessità """
    while True:
        complessita = input("Seleziona la tipologia di password:   semplice/complessa\n")
        if complessita != "semplice" and complessita != "complessa":
            print("Scelta sbagliata, seleziona tra: semplice e complessa\n")
            continue
        else:
            break
    match complessita:
        case "semplice":
            print(f"Hai generato una tipologia di password {complessita}")
            print("La password sarà priva di simboli e sarà di 8 caratteri")
            caratteri = string.ascii_lowercase + string.ascii_uppercase + string.digits
            grandezza = 8
        case "complessa":
            print(f"Hai selezionato una tipologia di password {complessita}")
            print("La password sarà con simboli e sarà di 20 caratteri")
            grandezza = 20
            caratteri = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    combinazione = "".join(random.choice(caratteri) for i in range(grandezza))
    print(f"\nLa grandezza della password è di: {grandezza} caratteri\n")
    print(f"La password è: {combinazione}\n")


crea_password()