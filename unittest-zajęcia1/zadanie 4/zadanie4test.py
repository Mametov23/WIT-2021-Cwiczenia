import zadanie4
import unittest

class Zadanie4Test(unittest.TestCase):
    def test_add(self, x = 1, y = 1):
        if ((type(x) and type(y)) == (int or float)):
            self.assertEqual(zadanie4.add(x, y), 2)
        else:
            raise ValueError('Not a number entered')

    def  test_subtract(self, x = 4, y = 2):
        if ((type(x) and type(y)) == (int or float)):
            self.assertEqual(zadanie4.subtract(x, y), 2)
        else:
            raise ValueError('Not a number entered')
    
    def test_multiply(self, x = 2, y = 5):
        if ((type(x) or type(y)) == (int or float)):
            self.assertEqual(zadanie4.multiply(x, y), 10)
        else:
            raise ValueError('Not a number entered')
        
    def test_divide(self, x = 1, y = 0):
        if ((type(x) and type(y)) == (int or float)):   
          with self.assertRaises(ValueError):
              zadanie4.divide(x, y)

        else:
            raise ValueError('Not a number entered')


if __name__ == '__main__':
    unittest.main()