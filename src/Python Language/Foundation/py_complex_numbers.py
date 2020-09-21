#!/bin/python3

"""
Complex Number
Format Print


Input:
2 1
5 6

Output:
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i

"""



import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        return Complex(self.real*no.real - self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)

    def __truediv__(self, no):
        no_mod2 = float(no.real*no.real + no.imaginary*no.imaginary)
        return Complex((self.real*no.real + self.imaginary*no.imaginary)/no_mod2, 
                       (self.imaginary*no.real - self.real*no.imaginary)/no_mod2);

    def mod(self):
        return Complex(math.sqrt(self.real*self.real+self.imaginary*self.imaginary), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

