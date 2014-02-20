#Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
#1219 is the smallest number such that the last digits are formed by p1 whilst
#also being divisible by p2.
#
#In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive
#primes, p2 > p1, there exist values of n for which the last digits are formed by
#p1 and n is divisible by p2. Let S be the smallest of these values of n.
#
#Find  S for every pair of consecutive primes with 5 <= p1 <= 1000000.

from utils import Utils
u = Utils()

a = u.sieve(1100000)

"""
    It is assumed that n is a power of 10.
"""
def phi(n):
    return (2 * n) / 5

def f1(p1, p2):
    m = len(str(p1))
    r = 10 ** m
    q = phi(r) - 1
    s = pow(p2, q, r)
    return ((((p1 * p2 * s) / r) % p2) * r) + p1

l = [f1(a[i], a[i + 1]) for i in range(2, len(a) - 1) if a[i] < 10 ** 6]

print sum(l)
#print l
#print [l[i] % a[i + 3] for i in range(len(l))]
