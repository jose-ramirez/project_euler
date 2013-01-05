#The prime 41, can be written as the sum of six consecutive primes:
#
#41 = 2 + 3 + 5 + 7 + 11 + 13
#
#This is the longest sum of consecutive primes that adds to a prime below
#one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime,
#contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most
#consecutive primes?

import sys
sys.path.append('../utils')
from utils import sieve

from bisect import bisect_left

"""
    Returns a list of all k-consecutive-prime sums given a
    prime list, which are less or equal than limit.
"""
def k_consecutive_prime_sums(primes, k, limit):
    l = []
    for i in range(len(primes) - k + 1):
        m = sum(primes[i : i + k])
        if m <= limit:
            l.append(m)
    return l

"""
    Efficient `item in lst` for sorted lists.
"""
def bi_contains(lst, item):
    # if item is larger than the last its not in the list, but the bisect would
    # find `len(lst)` as the index to insert, so check that first. Else, if the
    # item is in the list then it has to be at index bisect_left(lst, item)
    return (item <= lst[-1]) and (lst[bisect_left(lst, item)] == item)


#initial values:
k = 2
p1 = sieve(10 ** 6)
pl = k_consecutive_prime_sums(p1, k, 10 ** 6)
m = len(pl)
max_k = -1

#creating the k-prime sums given the (k - 1)-prime sums:
while m > 0:
    m = len(pl) - 1
    pl = [pl[i] + p1[i + k] for i in range(m) if pl[i] + p1[i + k] < 10 ** 6]
    k += 1
    for prime in pl:
        if bi_contains(p1, prime) and k > max_k:
            max_k = k
            print prime, k

print max_k
