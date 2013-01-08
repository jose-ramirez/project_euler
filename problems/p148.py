#We can easily verify that none of the entries in the first seven rows of
#Pascal's triangle are divisible by 7:
#
#1
#1 1
#1 2 1
#1 3 3  1
#1 4 6  4  1
#1 5 10 10 5  1
#1 6 15 20 15 6 1
#
#However, if we check the first one hundred rows, we will find that only 2361
#of the 5050 entries are not divisible by 7.
#
#Find the number of entries which are not divisible by 7 in the first one
#billion (109) rows of Pascal's triangle.

from operator import mul
from utils import Utils
u = Utils()

"""
    Returns the count of binomial coefficients
    not divisible by p.
"""
def nondivisor_count(m, p):
    return reduce(mul, [(r + 1) for r in expansion(m, p)])

def expansion(m, p):
    l = []
    start = m
    while start >= p:
        l.append(start % p)
        start /= p
    l.append(start)
    return l

#print expansion(12, 2)

#q = 7
#total = 0
#for m in xrange(7 ** 10, 10 ** 9):
#    print m
#    total += nondivisor_count(m, q)
#print total

"""
    Returns the total of binomial coefficients
    that are not divisible by p, for all m with
    k digits in their base p expansion.
"""
def find_total(k, p):
    return u.sum_up_to(p) ** k

#esta cuenta hasta 7^10:
print find_total(10, 7)