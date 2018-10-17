# There are some prime values, p, for which there exists a
# positive integer, n, such that the expression n^3 + n^2p is
# a perfect cube.
#
# For example, when p = 19, 8^3 + 8^2×19 = 12^3.
#
# What is perhaps most surprising is that for each prime with
# this property the value of n is unique, and there are only
# four such primes below one-hundred.
#
# How many primes below one million have this remarkable
# property?

from context import utils

cube_list = [x ** 3 for x in range(578)]
u = utils.Utils()
prime_list = u.sieve(10 ** 6)

def p131():
    """
        As taken from the forum:
        Since x^3 = n^2(n + p), and p is a prime, it turns
        out that n must be a cube, as well as n + p, i.e.,
        we must have p = a^3 - b^3 for some a, b.

        But, for a^3 - b^3 = (a - b)(a^2 + ab + b^2) to be
        prime we must have a - b = 1, so p must be a
        difference of consecutive cubes.
    """
    total = 0
    for i in range(len(cube_list) - 1):
        p_ = cube_list[i + 1] - cube_list[i]
        total += (u.chop(p_, prime_list) != -1)
    return total

print(p131())