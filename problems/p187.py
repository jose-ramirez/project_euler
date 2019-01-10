#coding: UTF-8
# A composite is a number containing at least two prime
# factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2
# × 3.
#
# There are ten composites below thirty containing precisely
# two, not necessarily distinct, prime factors: 4, 6, 9, 10,
# 14, 15, 21, 22, 25, 26.
#
# How many composite integers, n < 10^8, have precisely two,
# not necessarily distinct, prime factors?

from euler.utils import Utils
from math import sqrt
from bisect import bisect

u = Utils()

#One of the accepted solutions from the forum (by
#logopetria, @Sat, 22 Mar 2008, 08:45):
primes = u.sieve(5 * (10 ** 7))

def p187():
    N=10**8
    total=0
    for x in range(bisect(primes, sqrt(N))):
        p = primes[x]
        total += bisect(primes, N/p) - x
    return total

print(p187())