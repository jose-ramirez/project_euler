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
#How many numbers below a googol (10 ** 100) are not bouncy?

import sys
sys.path.append('../utils')
from utils import show

"""
    Kronecker delta.
"""
def delta(i, j):
    if i == j:
        return 1
    else:
        return 0

"""
    Returns true only if lower <= m <= upper.
"""
def in_range(m, lower, upper):
    return m >= lower and m <= upper

"""
    Returns the number of n-digit inc_nums ending in k.
"""
def inc(n, k):
    m = [[0] * (k + 1) for i in range(n + 1)]
    for j in range(k + 1):
        m[1][j] = 1 - delta(j, 0)
    for n1 in range(2, n + 1):
        for k1 in range(k + 1):
            m[n1][k1] = sum([m[n1 - 1][x] for x in range(k1 + 1)])
    return m[n][k]

"""
    Returns the number of n-digit inc_nums.
"""
def inc_(n):
    return sum([inc(n, k) for k in range(10)])

"""
    Returns the matrix containing all the
    k digit dec_nums, k <= n.
"""
def dec_mat(n):
    m = [[0] * 10 for i in range(n + 1)]
    for j in range(10):
        m[1][j] = 1 - delta(j, 0)
    for n1 in range(2, n + 1):
        for k1 in range(10):
            m[n1][k1] = sum(m[n1 - 1][k1:10])
    return m

"""
    Returns the number of n-digit dec_nums given
    the matrix used to calculate them.
"""
def dec_(n, d_m):
    return sum([d_m[n][k] for k in range(10)])

m = dec_mat(100)

total = 0
for i in range(1, 101):
    total += inc_(i)
    total += dec_(i, m)
# el 900 es para restar los que son contados 2 veces:
# los numeros de la forma kkkkk...k salen tanto en la
#cuenta de dec_nums como en la de inc_nums.
print total - 9 * 100
