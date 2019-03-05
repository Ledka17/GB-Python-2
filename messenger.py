# Скрипт запуска/остановки приложения мессенджер

from subprocess import Popen, CREATE_NEW_CONSOLE
import time

p_list = [] # Список запущенных процессов

while True:
    user = input("Запустить сервер и клиентов (s) / Выйти (q)")

    if user == 's': # Если выбран запуск сервера

        p_list.append(Popen('python -i server.py',
                            creationflags=CREATE_NEW_CONSOLE)) # Запускаем скрипт сервера добавляем его в список
        print('Сервер запущен')
        time.sleep(1) # Ожидаем

        CONSOLE_COUNT = 2 # Запускаем 2 консольных клиентов
        for i in range(CONSOLE_COUNT): # Проходим по всем клиентам
            client_name = 'Client_{}'.format(i)
            p_list.append(Popen('python -i client.py localhost 7777 r {}'.format(client_name),
                                 creationflags=CREATE_NEW_CONSOLE)) # Запускаем скрипт клиента и добавляем его в список

        print('Клиенты запущены')
    elif user == 'q': # Если выбран выход
        print('Открыто процессов {}'.format(len(p_list)))
        for p in p_list: # Проходим по всему списку процессов
            print('Закрываю {}'.format(p))
            p.kill() # Завершение процесса
        p_list.clear() #  Очищаем список процессов
        print('Выход выполнен')
        break # Завершение выполнения скрипта
