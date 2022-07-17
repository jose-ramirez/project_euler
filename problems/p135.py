# Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:
#
# 34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27
#
# It turns out that n = 1155 is the least value which has exactly ten solutions.
#
# How many values of n less than one million have exactly ten distinct solutions?

from math import sqrt, floor


def p135():
    my_total = 0
    for n in range(1155, 1000000):
        total = 0
        max_b = int(floor(sqrt(3 * n)))
        for b in range(1, max_b):
            if n % b == 0:
                y, d = n / b, (b + n // b) >> 2
                if n == y*(4*d - y) and y > d:
                    total += 1
        if total == 10:
            my_total += 1
    return my_total

print(p135())
