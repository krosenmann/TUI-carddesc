#!/usr/bin/env python3
import socket
import sys
from _thread import start_new_thread


HOST = '192.168.60.13'
PORT = 4444


def client_thread(conn):
    conn.send(b'Welcome to the server\n')
    while True:
        data = conn.recv(1024)
        reply = 'Ok... ' + data
        if not data:
            break

        conn.sendall(reply)
    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(msg)
    sys.exit()

s.listen(10)
print('Listening {}:{}'.format(HOST, PORT))

while 1:
    conn, addr = s.accept()
    print('Connected with {}:{}'.format(addr[0], addr[1]))

    start_new_thread(client_thread, (conn,))
s.close()
