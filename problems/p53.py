# coding: UTF-8
# There are exactly ten ways of selecting three from five,
# 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345.
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#
# nCr= n!/(r!(n−r)!), where r <= n, n! =
# n x (n−1) x ... x 3 x 2 x 1, and 0! = 1. It is not until
# n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of nCr, for
# 1 <= n <= 100, are greater than one-million?

import euler.numbers.functions as f

def p53():
    mat, val = f.binom(100, 100)
    total = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] > 10 ** 6:
                total += 1
    return total

print(p53())