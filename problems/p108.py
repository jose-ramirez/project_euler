# In the following equation x, y, and n are positive integers.
#
# \frac{1}{x} + \frac{1}{y} = \frac{1}{n}
#
# For n = 4 there are exactly three distinct solutions:
#
# \frac{1}{5} + \frac{1}{20} = \frac{1}{4}
# \frac{1}{4} + \frac{1}{6} = \frac{1}{4}
# \frac{1}{8} + \frac{1}{8} = \frac{1}{4}
#
# What is the least value of n for which the number of
# distinct solutions exceeds one-thousand?
#
# NOTE: This problem is an easier version of Problem 110; it
# is strongly advised that you solve this one first.

from context import Utils

u = Utils()

MAX = 200000

def get_exp(n, p):
    i = 0
    while n % p == 0:
        i += 1
        n = n / p
    return i

prime_list = u.sieve(MAX)

# calculating the desired number using memoization, stopping
# as soon as we find it:
def p108():
    i = 2
    l = [0, 1]
    while i < MAX:
        for p in prime_list:
            if i % p == 0:
                val = l[i // p] + \
                    2 * l[i // (p ** get_exp(i, p))] - 1
                if val >= 1000:
                    return i
                else:
                    l.append(val)
                    break
        i += 1

print(p108())