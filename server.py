# Программа сервера

from socket import *
import time, sys, logging, select
from jim.utils import get_message, send_message
from jim.config import *

def get_addr_port(): # Взять адрес и порт
    try: #Получаем адрес
        addr = sys.argv[1]
    except:
        addr = ''

    try: #Получаем номер порта
        port = int(sys.argv[2])
    except:
        port = 7777
    return [addr, port]

def read_requests(r_clients, all_clients): # Чтение сообщений от других клиентов
    messages = [] # Список входящих сообщений

    for sock in r_clients:
        try:
            message = get_message(sock) # Получаем сообщения
            print(message)
            messages.append((message, sock)) # Добавляем сообщения в список
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return messages # Возвращаем словарь сообщений

def write_responses(messages): # Отпрака сообщений клиентам
    for message, sender in messages:
        if message['action'] == MSG: # Получаем кому отправить
                to = message['to']
                sock = names[to]
                msg = message['message']
                send_message(sock, message)

@log
def presence_response(presence_message): # Формирование ответа клиенту
    if ACTION in presence_message and \
                    presence_message[ACTION] == PRESENCE and \
                    TIME in presence_message and \
            isinstance(presence_message[TIME], float): # Прохождение проверок
        return {RESPONSE: 200} # Отправляем ОК
    else:
        return {RESPONSE: 400, ERROR: 'Неверный запрос'} # Отправляем код ошибки



# Запуск сервера
if __name__ == '__main__':
    addr, port = get_addr_port()    
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind((addr, port))                # Привязывает сокет к IP-адресу и порту машины
    s.listen(3)                       # Переходит в режим ожидания запросов (не более 3)
    clients = [] # Список объектов клиентских сокетов
    names = {}

    while True:
        try:
            conn, addr = server.accept()  # Проверка подключений
            presence = get_message(conn) # ПОлучаем сообщение от клиента

            client_name = presence['user']['account_name']
            response = presence_response(presence) # Формируем ответ
            send_message(conn, response) # Отправляем ответ клиенту
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            names[client_name] = conn

            clients.append(conn)
        finally:
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait) # Проверить наличие событий ввдоа-вывода
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)  # Получаем входные сообщения
            write_responses(requests)  # Выполним отправку входящих сообщений
