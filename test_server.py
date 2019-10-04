import unittest
import server

# создаем тестовый случай                                                                                                         
class TestClient(unittest.TestCase):
    # создаем сам тест                                                                                                            
    def test_get_addr_port(self): #Проверка считывания аргументов функции                                                        
        self.assertTrue(get_addr_port[1] > 0) # Проверяем что значение порта больше 0


if __name__ == '__main__':
    unittest.main()
