# An irrational decimal fraction is created by concatenating
# the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is
# 1.
#
# If dn represents the nth digit of the fractional part, find
# the value of the following expression:
#
# d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
import functools as ft

def digits_of(n):
    if n < 10:
        return 1
    else:
        return 1 + digits_of(n // 10)

def digits_of_(n):
    return len(str(n))

def chegar_ate(n):
    i = 1
    total = 0
    val = n
    while total <= val:
        d = digits_of_(i)
        total += d
        n -= d
        i += 1
    return int(str(i - 1)[n - 1])

def p40():
    l = [chegar_ate(10 ** k) for k in range(1, 7)]
    return ft.reduce(lambda x, y: x * y, l)

print(p40())