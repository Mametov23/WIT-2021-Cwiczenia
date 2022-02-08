import zadanie3
import unittest

class TestZadanie3(unittest.TestCase):
    def test_is_numeric(self):
        numm = zadanie3.is_numeric(4)
        self.assertTrue(numm)

    def test_is_negative(self):
        self.skipTest(self)

    def test_calculate_saving(self, starting_amount, monthly_payment, monthly_deductions):
        pass

#Długo myślałem, jak to zrobić, ale tam i nie mógł wykonać

       



    




if __name__ == '__main__':
    unittest.main()