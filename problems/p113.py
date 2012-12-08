#Working from left-to-right if no digit is exceeded by the digit to its left
#it is called an increasing number; for example, 134468.
#
#Similarly if no digit is exceeded by the digit to its right it is called a
#decreasing number; for example, 66420.
#
#We shall call a positive integer that is neither increasing nor decreasing
#a "bouncy" number; for example, 155349.
#
#As n increases, the proportion of bouncy numbers below n increases such that
#there are only 12951 numbers below one-million that are not bouncy and only 
#277032 non-bouncy numbers below 1010.
#
#How many numbers below a googol (10100) are not bouncy?

import sys
sys.path.append('../utils')
from utils import show

def f1(n, k):
    m = [[0] * (k + 1) for i in range(n + 1)]
    for j in range(k + 1):
        m[1][j] = 1
        m[2][j] = j
    for n1 in range(3, n + 1):
        for k1 in range(k + 1):
            m[n1][k1] = sum([m[n1 - 1][x] for x in range(k1 + 1)])
    return m[n][k]

def inc_num(n):
    return sum([f1(n, k) for k in range(10)])

print sum([inc_num(k) for k in range(2, 7)])

#print f1(10)
#def f_test():
#    contador = 0
#    for n in range(10 ** 4, 10 ** 5):
#        a, b, c, d, e = n / 10000, (n / 1000) % 10, (n / 100) % 10, (n / 10) % 10, n % 10
#        if a <= b and b <= c and c <= d and d <= e:
#            print n
#           contador += 1
#    return contador

#print f1(5), f_test()
