#!/usr/bin/env python


def funzione_a(lista_a):
    """Attraverso questa funzione abbiamo in restituzione una lista vuota"""
    return lista_a


def conteggio_per_indice(lista_b):
    """Conteggia il numero di lettere per indice"""
    lista_a = funzione_a(["ciao", "sono", "riccardo","salerno"])
    for i in enumerate(lista_a):
        print(f"{i}\n\r")
    for i in lista_a:
        lista_b.append(len(i))
        print(f"Il primo oggetto ha: {len(i)} caratteri")
    return lista_b

conteggio_per_indice([])