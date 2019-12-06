# It is possible to write ten as the sum of primes in exactly five different ways:
#
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
#
# What is the first value which can be written as the sum of primes in over five
# thousand different ways?

from euler.utils import Utils
u = Utils()


def sopf(n, primes):
    """
        Returns the sum of the prime factors of n.
    """
    total = 0
    for p in primes:
        if n % p == 0:
            total += p
            while n // p == 0:
                n //= p
    return total

# print sopf(900)


def k(n):
    """
        This is the formula for the number of prime partitions of n, as
        given by http://programmingpraxis.com/2012/10/19/prime-partitions/
    """
    primes = u.sieve(n)
    l = [1, 0]
    for i in range(2, n + 1):
        l1 = [l[r] * sopf(i - r, primes) for r in range(1, i)]
        s = (sum(l1) + sopf(i, primes)) // i
        l.append(s)
    return l[n]


def p77():
    n = 2
    while k(n) <= 5000:
        n += 1
    return n


print(p77())
