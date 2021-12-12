from zadanie2 import Employee
import unittest

class TestZadanie2(unittest.TestCase):
    def test_introduce_self(self):
        nn = Employee('eldar', 'mametov', '18', 8000 )
        self.assertEqual(nn.introduce_self(), 'My name is eldar mametov and I am 18 years old')
    
    def test_raise_salary(self, ratio = 1):
        nnn = Employee('eldar', 'mametov', '18', 8000)
        self.assertNotEqual(nnn.raise_salary(ratio = 1), 5000)
        
    def test_check_age(self):
        nn = Employee('eldar', 'mametov', 14, 8000 )
        self.assertEqual(nn.check_age(), 'Underage employee')

    def test_get_email(self):
        nn = Employee('eldar', 'mametov', 14, 8000 )
        self.assertEqual(nn.get_email(), 'eldarmametov@company.com')



if __name__ == '__main__':
     unittest.main()