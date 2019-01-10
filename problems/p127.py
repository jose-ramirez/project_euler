# The radical of n, rad(n), is the product of distinct prime factors of n. For
# example, 504 = 2^3 x 3^2 x 7, so rad(504) = 2 x 3 x 7 = 42.
#
# We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

# GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
# a < b
# a + b = c
# rad(abc) < c
# For example, (5, 27, 32) is an abc-hit, because:

# GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
# 5 < 27
# 5 + 27 = 32
# rad(4320) = 30 < 32
# It turns out that abc-hits are quite rare and there are only thirty-one abc
# hits for c < 1000, with sum(c) = 12523.
#
# Find sum(c) for c < 120000.

from fractions import gcd
from euler.utils import Utils
u = Utils()

def hit(a, b, c, rad):
    cond_1 = gcd(b, c) == 1
    cond_2 = rad[a] * rad[b] * rad[c] < c
    return cond_1 and cond_2

def rad(n, primes):
    """
        creates an array of rad(n) for all values < n using dp
        and a precalculated set of primes.
    """
    l = [0, 1]
    i = 2
    while i < n:
        n_ = i
        if n_ in primes:
            l.append(n_)
        else:
            for p in primes:
                if n_ % p != 0:
                    continue
                while n_ % p == 0:
                    n_ /= p
                if n_ < len(l):
                    l.append(p * l[int(n_)])
                    break
        i += 1
    return l

def p127(max_c, exp):
    primes = u.sieve(max_c)
    radicals = rad(int(max_c), primes)
    possible_ys = [i for i in range(1, max_c) if radicals[i] <= int(max_c ** exp)]
    possible_rads = [radicals[i] for i in possible_ys]
    print("len(radicals):", len(radicals))
    print("len(possible_ys):", len(possible_ys))
    print(possible_ys)
    print(possible_rads)
    total = 0
    for a in possible_ys:
        for b in possible_ys:
            c = a + b
            if a < b and c < max_c and hit(a, b, c, radicals):
                print(a,b,c)
                total += c
    return total

print(p127(120000, 0.8))