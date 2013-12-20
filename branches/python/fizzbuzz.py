'''
Created on Jul 25, 2013

@author: HP
'''


class FizzBuzzGame(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def hasThree(self, number):
        return '3' in str(number)

    def hasFive(self, number):
        return '5' in str(number)

    def isDivisableByThreeAndFive(self, number):
        return not number % 15

    def isDivisableByFive(self, number):
        return not number % 5

    def isDivisableByThree(self, number):
        return not number % 3

    def list_numbers(self):
        numbers = range(1, 100)
        for number in numbers:
            if self.isDivisableByThree(number) or self.hasThree(number):
                numbers[number - 1] = 'Fizz'
            if self.isDivisableByFive(number) or self.hasFive(number):
                numbers[number - 1] = 'Buzz'
            if self.isDivisableByThreeAndFive(number):
                numbers[number - 1] = 'FizzBuzz'
        return numbers
