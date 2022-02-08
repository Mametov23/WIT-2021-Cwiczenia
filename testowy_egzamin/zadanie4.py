import unittest
from hr import calculate_velocity

class TestCalc(unittest.TestCase): 
    def test_calculate_velocity(self):
        f = calculate_velocity('15', '23')
        self.assertFalse(f)
    
    def test_calculate_velocity(self):
        d = calculate_velocity(15, 23)
        self.skipTest(self)






if __name__ == "__main__":
    unittest.main()