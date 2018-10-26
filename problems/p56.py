# A googol (10^100) is a massive number: one followed by
# one-hundred zeros; 100^100 is almost unimaginably large:
# one followed by two-hundred zeros. Despite their size, the
# sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a^b, where
# a, b < 100, what is the maximum digital sum?

import functools as ft

def digit_sum(a, b):
    m = a ** b
    s = str(m)
    total = ft.reduce(lambda x, y: x + y, map(int, s))
    return total

def p56():
    max = -1
    max_a, max_b = 0, 0
    for a in range(100):
        for b in range(100):
            m = digit_sum(a, b)
            if m > max:
                max = m
                max_a = a
                max_b = b
    return m, max_a, max_b

print(p56())