#A palindromic number reads the same both ways. The largest
#palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

import sys
sys.path.append('../utils')
from utils import palindrome

def p4():
    max = -1
    a = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            a = i * j
            if palindrome(str(a)) and a > max:
                max = a
    return max

print(p4())
