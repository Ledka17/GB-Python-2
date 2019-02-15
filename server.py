# Программа сервера

from socket import *
import time, sys

try: #Получаем адрес
    addr = sys.argv[1]
except:
    addr = ''

try: #Получаем номер порта
    port = int(sys.argv[2])
except:
    port = 7777
    
s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((addr, port))                # Привязывает сокет к IP-адресу и порту машины
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
