#!/bin/python3

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        Sum = 0
        for i in range(1, n + 1):
            if (n%i) == 0:
                Sum += i
        return Sum

if __name__ == '__main__':
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)