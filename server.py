# Программа сервера

from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 7777))                # Присваивает порт 7777
s.listen(3)                       # Переходит в режим ожидания запросов (не более 3)

while True:
    client, addr = s.accept() #принимает запрос на установку соединения
    data = client.recv(1000000) #принимает сообщение клиента
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr) #выводит сообщение
    msg = {
        "response": 200,
        "time": int(time.time()),
        "alert": "OK"
    }#формирует ответ клиенту
    client.send(msg.encode('utf-8')) #отправляет ответ клиенту
    client.close() #закрывает соединение 
