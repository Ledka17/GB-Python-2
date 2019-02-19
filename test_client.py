import unittest
import client

# создаем тестовый случай
class TestClient(unittest.TestCase):
    # создаем сам тест
    def test_get_addr_port(self): #Проверка считывания аргументов функции
        self.assertTrue(get_addr_port[0])
        self.assertTrue(get_addr_port[1])

    def test_server_res(self): #Проверка получения сообщений от сервера
        s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
        s.connect(('localhost', 7777))   # Соединиться с сервером
        s.send("Hello".encode('utf-8'))
        self.assertTrue(server_res(s))

if __name__ == '__main__':
    unittest.main()
