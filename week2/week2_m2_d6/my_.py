#!/usr/bin/env python


import socket
import platform
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 6553))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected by {address}")
        print(f"{platform.platform}, {platform.architecture}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall()
