# Write your unit tests here!
import unittest
from optimal_change import my_optimal_change


class OptimalChangeTestCase(unittest.TestCase):
    """Tests for optimal_change.py"""

    def test_first_case(self):
        '''Check for plurals and comma'''
        output_1 = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        self.assertEqual(my_optimal_change(62.13, 100), output_1)

    def test_second_case(self):
        '''Check for plural and commas'''
        output_2 = "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
        self.assertEqual(my_optimal_change(31.51, 50), output_2)

    def test_third_case(self):
        '''Check for plural and commas'''
        output_3 = "This customer gets no change."
        self.assertEqual(my_optimal_change(36.51, 36.51), output_3)
    
    def test_fourth_case(self):
        '''Check for plural and commas'''
        output_4 = "The optimal change for an item that costs $25.19 with an amount paid of $100 is 1 $50 bill, 1 $20 bill, 4 $1 bills, 3 quarters, 1 nickel, and 1 penny."
        self.assertEqual(my_optimal_change(25.19, 100), output_4)

    def test_fifth_case(self):
        '''Check for plural and commas'''
        output_5 = "The optimal change for an item that costs $1.22 with an amount paid of $20 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 3 quarters, and 3 pennies."
        self.assertEqual(my_optimal_change(1.22, 20), output_5)
    
    def test_sixth_case(self):
        '''Check for plural and commas'''
        output_6 = "The optimal change for an item that costs $4.98 with an amount paid of $5 is 2 pennies."
        self.assertEqual(my_optimal_change(4.98, 5), output_6)
    
    def test_seventh_case(self):
        '''Check for plural and commas'''
        output_7 = "The optimal change for an item that costs $2.25 with an amount paid of $10 is 1 $5 bill, 2 $1 bills, and 3 quarters."
        self.assertEqual(my_optimal_change(2.25, 10), output_7)

if __name__ == '__main__':
    unittest.main()