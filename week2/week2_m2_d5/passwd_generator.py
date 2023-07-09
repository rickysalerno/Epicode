#!/usr/bin/env python


""" L'applicazione è un generatore di password """


import string
import random


def complexity(grandezza):
    """In base alla complessità genero una password"""
    if grandezza == 8:
        caratteri = (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.digits
            )
    elif grandezza == 20:
        caratteri = (
            string.ascii_lowercase +
            string.ascii_uppercase +
            string.punctuation +
            string.digits
            )
    return "".join(random.choice(caratteri) for i in range(grandezza))


def crea_password():
    """
    Creazione Pass In base alla complessità:
    semplice == 8 e senza simboli,
    complessa == 20 e con simboli.
    """

    while True:
        complessita = input("Seleziona la tipologia di password, semplice/complessa     ---->    ")
        if complessita != "semplice" and \
            complessita != "complessa":
            print("Scelta sbagliata, seleziona tra: semplice e complessa\n")
            continue
        break
    match complessita:
        case "semplice":
            print(f"\nHai generato una tipologia di password {complessita}")
            print("\nLa password sarà priva di simboli e sarà di 8 caratteri")
            password = complexity(8)
        case "complessa":
            print(f"\nHai selezionato una tipologia di password {complessita}")
            print("\nLa password sarà con simboli e sarà di 20 caratteri")
            password = complexity(20)
    print(f"La password è: {password}\n")


crea_password()