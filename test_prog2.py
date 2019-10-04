import unittest, prog2

class TestSumKV(unittest.TestCase):
    # создаем сам тест
    def testequal(self):
        self.assertEqual(prog2.lst_new([4, 8, 0, 3, 4, 2, 0, 3]), [0, 3, 4])
        self.assertEqual(prog2.lst_new([10]), [])
        self.assertEqual(prog2.lst_new([1, 1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(prog2.lst_new([1, 1, 2, 2, 2, 3]), [1, 2])
        self.assertEqual(prog2.lst_new([]), [])
        self.assertEqual(prog2.lst_new([0, 0, 0, 0]), [0])

if __name__ == '__main__':
    unittest.main()
