# Программа клиента

from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 7777))   # Соединиться с сервером
msg = 'Привет, сервер! Как дела?' #сформировать presence-сообщение
s.send(msg.encode('utf-8')) #отправить сообщение серверу
data = s.recv(1000000) #получить ответ сервера
print('Сообщение от сервера: ', data.decode('utf-8')) #разобрать сообщение сервера
s.close() #завершить соединение
