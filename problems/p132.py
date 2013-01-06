#A number consisting entirely of ones is called a repunit. We shall define R(k)
#to be a repunit of length k.
#
#For example, R(10) = 1111111111 = 11412719091, and the sum of these prime
#factors is 9414.
#
#Find the sum of the first forty prime factors of R(10^9).

import sys
sys.path.append('../utils')
from utils import sieve

"""
    Returns the value of a ** b (mod n), when m
    is a fucking huge number, like 10 ** (10 ** 9).
"""
def exp_mod(x, y, n):
    if y == 0:
        return 1
    z = exp_mod(x, y / 2, n)
    if y % 2 == 0:
        return (z ** 2) % n
    else:
        return (x * (z ** 2)) % n

l = sieve(2 * (10 ** 5))
count = 0
total = 0
for p in l:
    if exp_mod(10, 10 ** 9, p) == 1:
        count += 1
        if count <= 41 and p != 3:
            total += p
            if count == 41:
                print total