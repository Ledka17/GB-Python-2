# Программа клиента

from socket import *
import time, sys
rom errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from jim.config import *
from jim.utils import send_message, get_message

import threading

import logging


def get_addr_port(): # Получить адрес и порт
    try: #Получаем адрес
        addr = sys.argv[1]
    except:
        addr = 'localhost'

    try: #Получаем номер порта
        port = int(sys.argv[2])
    except:
        port = 7777
    return [addr, port]

@log
def create_presence(account_name="Guest"): # ФОрмирование сообщения
    if not isinstance(account_name, str): # Если имя не строка
        raise TypeError # Генерация ошибки неверный тип
    if len(account_name) > 25: # Если имя больше 25 символов
        raise UsernameToLongError(account_name) # Генерация ошибки слишком длинное имя

    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        } # Формируем словарь сообщения
    }
    return message # Возвращаем сообщение в виде словаря


@log
def translate_message(response): # Разбор ответа сервера
    if not isinstance(response, dict): # Если ответ не словарь
        raise TypeError # Ошибка
    if RESPONSE not in response: # Если нет ключа response
        raise MandatoryKeyError(RESPONSE) # Ошибка

    code = response[RESPONSE]
    if len(str(code)) != 3: # Если длина кода не 3 символа
        raise ResponseCodeLenError(code) # Ошибка
    # неправильные коды символов
    if code not in RESPONSE_CODES: # Если таких кодов ошибки нет
        raise ResponseCodeError(code) # Ошибка
    return response # Возврат ответа

def read_messages(client, account_name): # Чтение клиентом сообщений
    while True:
        message = get_message(client) # Получаем сообщение
        print(message['message']) # Печатаем в консоли

def create_message(message_to, text, account_name='Guest'): # Создать сообщение
    return {ACTION: MSG, TIME: time.time(), TO: message_to, FROM: account_name, MESSAGE: text}


# Запуск клиента
if __name__ == '__main__':
    addr, port = get_addr_port()
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    client.connect((addr, port))   # Соединиться с сервером
    presence = create_presence(account_name) # Сформировать сообщение
    send_message(client, presence) # Отправить сообщение серверу
    response = get_message(client) # Получить ответ сервера
    response = translate_message(response) # Разобрать ответ сервера
    if response['response'] == OK: # Если ответ без ошибок
        t = threading.Thread(target=read_messages, args=(client, account_name)) # Создать поток
        t.start()

        while True: # Отправка и получение сообщений
            message_str = input('>>')
            if message_str.startswith('message'):
                params = message_str.split()
                try:
                    to = params[1]
                    text = ' '.join(params[2:])
                except IndexError:
                    print('Не задан получатель или текст сообщения')
                else:
                    message = create_message(to, text, account_name)
                    send_message(client, message)

            elif message_str == 'help':
                print('message <получатель> <текст> - отправить сообщение')
            elif message_str == 'exit':
                break
            else:
                print('Неверная команда, для справки введите help')

        client.disconnect()
