import zadanie1
import unittest

class Zadanie1Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(zadanie1.add(1, 2), 3)

    def  test_subtract(self):
        self.assertEqual(zadanie1.subtract(4, 2), 2)
    
    def test_multiply(self):
        self.assertEqual(zadanie1.multiply(2, 5), 10)
        
    def test_divide(self):
          with self.assertRaises(ValueError):
              zadanie1.divide(1, 0)
if __name__ == '__main__':
    unittest.main()