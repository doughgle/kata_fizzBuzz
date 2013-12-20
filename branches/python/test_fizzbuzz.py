'''
Created on Jul 25, 2013

@author: HP
'''
import unittest
from fizzbuzz import FizzBuzzGame


class Test(unittest.TestCase):

    def setUp(self):
        self.g = FizzBuzzGame()

    def assertNumberEquals(self, expected, number):
        return self.assertEqual(expected, self.g.list_numbers()[number - 1])

    def assertFizz(self, number):
        self.assertNumberEquals('Fizz', number)

    def assertBuzz(self, number):
        self.assertNumberEquals('Buzz', number)

    def assertFizzBuzz(self, number):
        self.assertNumberEquals('FizzBuzz', number)

    def test_plainNumbersShouldBeSequential(self):
        self.assertEqual([1, 2], self.g.list_numbers()[:2])

    def test_multiplesOfThreeShouldBeFizz(self):
        self.assertFizz(3)
        self.assertFizz(6)
        self.assertFizz(12)

    def test_mulitplesOfFiveShouldBeBuzz(self):
        self.assertBuzz(5)
        self.assertBuzz(10)
        self.assertBuzz(20)

    def test_mulitplesOfThreeAndFiveShouldBeFIzzBuzz(self):
        self.assertFizzBuzz(15)
        self.assertFizzBuzz(30)
        self.assertFizzBuzz(45)

    def test_numberWithAThreeInItShouldBeFizz(self):
        self.assertFizz(13)
        self.assertFizz(23)
        self.assertFizz(33)

    def test_numberWithAFiveInItShouldBeBuzz(self):
        self.assertBuzz(52)
        self.assertBuzz(53)
        self.assertBuzz(54)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNothing']
    unittest.main()
