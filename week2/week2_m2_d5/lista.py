#!/usr/bin/env python

lista = []

def lista_a():
    """Inserisci una serie di parole che andarnno conteggiate dopo"""
    print("Inserisci 10 elementi da aggiungere alla lista:   ")
    while True:
        lista.append(input("Inserisci elemento:   "))
        if len(lista) == 10:
            break
    print(f"La lista è composta da {len(lista)} elementi")
    print(f"La lista è composta da {lista}")


def lista_b():
    """Conteggio dei numeri di stringhe per indice"""
    print("Adesso eseguiamo il conteggio degli elementi della lista, e quante parole sono presenti per elemento.\n")
    count = 1
    for i in enumerate(lista):
        print(f"Elemento: {i}\n")
    for i in range(0, len(lista)):
        count = 0
        for j in lista[i]:
            count+=1
        print(f"L'elemento {i} è composta da: {count} elementi.")


lista_a()
lista_b()
