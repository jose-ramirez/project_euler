#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

from euler.utils import Utils
u = Utils()

def p10():
    return sum(u.sieve(2000000))

print(p10())