#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,\
#we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

from euler.utils import Utils
u = Utils()

def p7():
    return u.sieve(1000000)[10000]

print(p7())