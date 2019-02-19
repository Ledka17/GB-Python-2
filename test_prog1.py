import prog1
import unittest

# создаем тестовый случай
class Test_prog1(unittest.TestCase):
    # создаем сам тест
    def test_def_year(self):
        # используем функцию assertEqual модуля unittest
        self.assertEqual(prog1.def_year(2015), 'Обычный')
        self.assertEqual(prog1.def_year(1800), 'Обычный')
        self.assertEqual(prog1.def_year(1975), 'Обычный')
        self.assertEqual(prog1.def_year(89), 'Обычный')
        self.assertEqual(prog1.def_year(1), 'Обычный')
        self.assertEqual(prog1.def_year(2016), 'Високосный')
        self.assertEqual(prog1.def_year(2000), 'Високосный')
        self.assertEqual(prog1.def_year(400), 'Високосный')
        self.assertEqual(prog1.def_year(1976), 'Високосный')
        self.assertEqual(prog1.def_year(1812), 'Високосный')
        self.assertEqual(prog1.def_year(964), 'Високосный')

if __name__ == '__main__':
    unittest.main()
