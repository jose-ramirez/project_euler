#coding: UTF-8
#Consider the infinite polynomial series AF(x) = xF_1 +
#x^2F_2 + x_3F_3 + \cdots, where F_k is the kth term in the
#Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is,
#F_k = F_{k − 1} + F_{k − 2}, F_1 = 1 and F_2 = 1.
#
#For this problem we shall be interested in values of x for
#which AF(x) is a positive integer.
#
#Surprisingly AF(1/2) = (1/2).1 + (1/2)^2.1 + (1/2)^3.2 +
#(1/2)^4.3 + (1/2)^5.5 + ... = 1/2 + 1/4 + 2/8 + 3/16 +
#5/32 + \cdots = 2. The corresponding values of x for the
#first five natural numbers are shown below.
#
#x        AF(x)
#√2−1      1
#1/2       2
#(√13−2)/3 3
#(√89−5)/8 4
#(√34−3)/5 5
#We shall call AF(x) a golden nugget if x is rational,
#because they become increasingly rarer; for example, the
#10th golden nugget is 74049690.
#
#Find the 15th golden nugget.

from utils import Utils
from math import sqrt

u = Utils()

def p137():
    """
        Since AF(x) has to be an integer, we have
        \frac{x}{1 - x - x^2} = n for some n. So, this
        leads to solving the equation nx^2 + (n + 1)x -
        n = 0, whose solution in x are
        x = \frac{-(n - 1 \pm sqrt(5n^2 + 2n + 1))}{2n}.
    
        Now, since x has to be rational, it follows that
        5n^2 + 2n + 1 = y^2 for some integer y, which leads
        us to the following Pell equation:
    
        (5n + 1)^2 - 5y^2 = -4.
    
        It is known (and somehow easy enough to prove) that
        this equation has infinitely many integer solutions
        (x_k, y_k), and that y_k = F_{2k + 1}
        \forall k \geq 0, the Fibonacci numbers of odd
        index.
    
        So we just have to find which of the odd indexed
        Fibonacci numbers generates an x congruent to 1
        modulo 5 to get n out of it:
    """
    a, b, i, j, n = 1, 1, 2, 0, 0
    while j < 15:
        a, b = a + b, a
        i += 1
        if i % 2 == 1:
            x = int(sqrt(5 * (a ** 2) - 4))
            if x % 5 == 1:
                j += 1
                if j == 15:
                    n = (x - 1) / 5
                    print n

u.exec_time(p137)