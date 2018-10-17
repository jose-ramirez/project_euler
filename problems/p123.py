#coding: UTF-8
# Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r
# be the remainder when (p_n − 1)^n + (p_n + 1)^n is divided
# by p_n^2.
#
# For example, when n = 3, p_3 = 5, and 4^3 + 6^3 = 280
# ≡ 5 mod 25.
#
# The least value of n for which the remainder first exceeds
# 10^9 is 7037.
#
# Find the least value of n for which the remainder first
# exceeds 10^10.

from context import utils

u = utils.Utils()

p = u.sieve(4 * (10 ** 5))

def p123():
    i = 0
    a = 0
    while a < 10 ** 10 and i < len(p):
        i += 1
        a = (2 * p[i] * (i + 1)) % (p[i] ** 2)
    # sum 2 because i is the index of the number just below
    # 10 ** 10, and array indices start by 0:
    return i + 2

print(p123())