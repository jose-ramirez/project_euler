# The binomial coefficient 10C3=120.
#
# 120=2^3×3×5=2×2×2×3×5, and 2+2+2+3+5=14.
#
# So the sum of the terms in the prime factorisation of 10C3 is 14.
#
# Find the sum of the terms in the prime factorisation of 20000000C15000000.

import euler.numbers.functions as f
from euler.utils import Utils

def p231():
    u = Utils()
    primes = u.sieve(20000000)
    total = 0
    for p in primes:
        total += p * (f.v(20000000, p) - (f.v(5000000, p) + f.v(15000000, p)))
    return total

print(p231())