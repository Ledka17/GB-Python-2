from socket import *
from select import select
import sys

ADDRESS = ('localhost', 7777)

def echo_client():
    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect(ADDRESS)   # Соединиться с сервером
        while True:
            msg = input('Введите сообщение: ') # Считываем сообщение клиента
            if msg == 'exit':
                break
            sock.send(msg.encode('utf-8'))     # Отправить сообщение серверу


if __name__ == '__main__':
    echo_client()
