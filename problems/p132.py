# A number consisting entirely of ones is called a repunit. We shall define R(k)
# to be a repunit of length k.
#
# For example, R(10) = 1111111111 = 11 * 41 * 271 * 9091, and the sum of these prime
# factors is 9414.
#
# Find the sum of the first forty prime factors of R(10^9).

from context import utils
u = utils.Utils()

def p132():
    primes = u.sieve(165000)
    total = 0
    count = 0
    for p in primes:
        if u.exp_mod(10, 10 ** 9, p) == 1:
            count += 1
            if count <= 41:
                total += p
            else:
                break
    return total - 3

print(p132())

