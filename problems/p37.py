#The number 3797 has an interesting property. Being prime
#itself, it is possible to continuously remove digits from
#left to right, and remain prime at each stage: 3797, 797,
#97, and 7. Similarly we can work from right to left: 3797,
#379, 37, and 3.
#
#Find the sum of the only eleven primes that are both
#truncatable from left to right and right to left.
#
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable
#primes.

from utils import Utils

def is_right_truncatable(p, u, sieve):
    while p > 10:
        p /= 10
        if u.chop(p, sieve) == -1:
            return False
    return True

def is_left_truncatable(p, u, sieve):
    p_str = str(p)
    while len(p_str) > 1:
        p_str = p_str[1:]
        if u.chop(int(p_str), sieve) == -1:
            return False
    return True

def p37():
    u = Utils()
    primes = u.sieve(10 ** 6)
    total = 0
    for p in primes:
        a = is_right_truncatable(p, u, primes)
        b = is_left_truncatable(p, u, primes)
        if a and b:
            total += p
    #we have to ignore 2, 3, 5, and 7, which sum up to 17:
    print total - 17

u = Utils()
u.exec_time(p37)