import unittest
from primenumbersV02 import prime_numbers

class PrimeNumbersCorrect(unittest.TestCase):
    def number_in_returned_value (self):
        result = primenumbers(15)
        print result

    def expected_number_in_result(self):
        result = primenumbers(15)
        self.assertIn([2,3,5,7,11,13],result)

    def number_not_expected_in_result(self):
        result = primenumbers(15)
        self.assertNotIn([1,4,6,8,9,10,12,14],result)

    
    
    
        

    
