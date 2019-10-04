import prog3
import unittest

class Test_prog3(unittest.TestCase):
    # создаем сам тест
    def test_a_rep(self):
        # используем функцию assertEqual модуля unittest
        self.assertEqual(prog3.a_rep(['a', 'aa', 'abC', 'aa', 'ac', 'abc', 'bcd', 'a']), {'ac': 1, 'a': 2, 'abc': 2, 'bcd': 1, 'aa': 2})
        self.assertEqual(prog3.a_rep(['a', 'A', 'a']), {'a': 3})

if __name__ == '__main__':
    unittest.main()
