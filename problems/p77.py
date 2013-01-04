#It is possible to write ten as the sum of primes in exactly five different ways:
#
#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2
#
#What is the first value which can be written as the sum of primes in over five
#thousand different ways?

import sys
sys.path.append('../utils')
from utils import sieve

"""
    Returns the number of partitions of n with prime elements,
    the inefficient way. Although not yet there, :p
"""
def partitions(m, s):
    if m < 4:
        return 0
    elif m < 7:
        return 1
    else:
        return sum([partitions(m - p, s) for p in s if p < m])

def f(x, p, l):
    print x, p, x - p
    return l[x - p]

"""
    Returns the number of partitions of n with prime elements,
    the efficient way. Although not yet there, :p
"""
def parts(m):
    s = sieve(m)
    l = [0,0,0,0,1,1,2]
    if m < len(l) and l[m] != 0:
        return l[m]
    else:
        for x in range(7, m + 1):
            a = [f(x, p, l) for p in s if p <= x]
            l.append(sum(a))
            print a
    print l
    return l[m]


#print partitions(20, s)
#print parts(10)

"""
    Returns the sum of the prime factors of n.
"""
def sopf(n, primes):
    total = 0
    for p in primes:
        if n % p == 0:
            total += p
            while n / p == 0:
                n /= p
    return total

#print sopf(900)

"""
    This is the formula for the number of prime partitions of n, as
    given by http://programmingpraxis.com/2012/10/19/prime-partitions/
"""
def k(n):
    primes = sieve(n)
    l =[1, 0]
    for i in range(2, n + 1):
        l1 =[l[r] * sopf(i - r, primes) for r in range(1, i)]
        s = (sum(l1) + sopf(i, primes)) / i
        l.append(s)
    return l[n]

print k(71)

