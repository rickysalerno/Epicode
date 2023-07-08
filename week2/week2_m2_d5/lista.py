#!/usr/bin/env python


def funzione_a(lista_a):
    """Attraverso questa funzione abbiamo in restituzione una lista vuota"""
    return lista_a


def conteggio_per_indice(lista_b):
    a = funzione_a(["ciao", "sono", "riccardo","salerno"])
    for i in enumerate(a):
        print(f"{i}\n\r")
    for i in a:
        lista_b.append(len(i))
    return lista_b


conteggio = conteggio_per_indice([])
print(f"{conteggio}\r\n")