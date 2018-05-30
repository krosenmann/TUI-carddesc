#!/usr/bin/env python3
import socket
import sys
import argparse
from _thread import start_new_thread


HOST = ''
PORT = 4444


def client_thread(conn):        # Нужен?
    conn.send(b'Welcome to the server\n')
    while True:
        data = conn.recv(1024)
        reply = 'Ok... ' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', '--host', '-p', '--port')
    return parser


def main(*args, **kwargs):
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


if __name__ == '__main__':
    main(sys.argv)
