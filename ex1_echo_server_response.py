import time
import select
from socket import socket, AF_INET, SOCK_STREAM

def read_requests(r_clients, all_clients): # Чтение запросов клиентов
    responses = {}      # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients: # Считываем сокет от каждого клиента
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except: # Если клиент октлючился
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock) # Удаляем его

    return responses


def write_responses(requests, w_clients, all_clients): # Ответ от сервера клиентам с запросами
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8') # Сформировать ответ
                sock.send(resp) # Отправить ответ всем клиентам
            except:                 # Если  клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock) # Удалить его


def new_listen_socket(address): # Работа с сокетом
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5) # Считываем 5 запросов
    sock.settimeout(0.2)   # Таймаут для операций с сокетом (повышение эффективности)

    return sock


def mainloop(): # Цикл бработки запросов клиентов
    address = ('', 7777) # 7777 порт по умолчанию
    clients = []
    sock = new_listen_socket(address) # Прослушиваем сокет

    while True:
        try:
            conn, addr = sock.accept()  # Проверка подключений
        except OSError as e:
            pass                     # timeout вышел
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            clients.append(conn)
        finally:
            w, r = [], []
            try: # Проверить наличие ввода-вывода
                r, w, e = select.select(clients, clients, [], wait)

            except Exception as e: # Если клиент отключился
                pass            # Пропустить
            
            requests = read_requests(r, clients)      # Считываем запросы клиентов
            if requests:
                write_responses(requests, w, clients)     # Отправка ответов клиентам


print('Запущен эхо-сервер')
mainloop()
