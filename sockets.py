import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.conect(('data.py4e.org', 80))
