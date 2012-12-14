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
    Returns the number of n-digit inc_nums ending in k.
"""
def n_digit_inc_num(n, k):
    m = [[0] * (k + 1) for i in range(n + 1)]
    for j in range(k + 1):
        m[1][j] = 1
        m[2][j] = j
    for n1 in range(3, n + 1):
        for k1 in range(k + 1):
            m[n1][k1] = sum([m[n1 - 1][x] for x in range(k1 + 1)])
    return m[n][k]

"""
    Returns the number of n-digit inc_nums.
"""
def inc_num_count(n):
    return sum([f1(n, k) for k in range(10)])

#print sum([inc_num(k) for k in range(2, 7)])


"""
    Returns the count of non-bouncy numbers below m.
    it is assumed that m > 100.
"""
def count_non_bouncy(m):
    count = 0
    for n in range(100, limit):
        s = [int(d) for d in str(n)]
        s.insert(0, [True, s[0]])
        l1 = reduce(lambda x, y: [x[0] & (x[1] <= y), y], s)
        if l1[0]:
            count += 1
            continue
        l2 = reduce(lambda x, y: [x[0] & (x[1] >= y), y], s)
        if l2[0]:
            count += 1
    return count + 99

#print count_non_bouncy(1000)

