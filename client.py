# Программа клиента

from socket import *
import time, sys

try: #Получаем адрес
    addr = sys.argv[1]
except:
    addr = 'localhost'

try: #Получаем номер порта
    port = int(sys.argv[2])
except:
    port = 7777

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((addr, port))   # Соединиться с сервером
presence_msg = {
        "action": "presence",
        "time": int(time.time()),
        "type": "status",
        "user": {
                "account_name":  "Leonarda",
                "status":      "I'm here!"
        }
} #сформировать presence-сообщение
s.send(msg.encode('utf-8')) #отправить сообщение серверу
data = s.recv(1000000) #получить ответ сервера
print('Сообщение от сервера: ', data.decode('utf-8')) #разобрать сообщение сервера
s.close() #завершить соединение
