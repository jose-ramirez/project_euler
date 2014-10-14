#coding: UTF-8
#The Fibonacci sequence is defined by the recurrence
#relation:
#
#F_n = F_{n − 1} + F_{n − 2}, where F_1 = 1 and F_2 = 1. It
#turns out that F_541, which contains 113 digits, is the
#first Fibonacci number for which the last nine digits are
#1-9 pandigital (contain all the digits 1 to 9, but not
#necessarily in order). And F_2749, which contains 575
#digits, is the first Fibonacci number for which the first
#nine digits are 1-9 pandigital.
#
#Given that F_k is the first Fibonacci number for which the
#first nine digits AND the last nine digits are 1-9
#pandigital, find k.

from utils import Utils
from math import sqrt
from decimal import Decimal

u = Utils()

def is_pandigital(n):
    return ''.join(sorted(str(n))) == '123456789'

def p104():
    phi = (1 + sqrt(5)) / 2.
    c = sqrt(5)
    i = 2
    f = Decimal((phi ** 2) / c)
    m = str(f)[:10].replace('.', '')
    a, b = 1, 1
    while not (is_pandigital(m) and is_pandigital(a)):
        a, b = (a + b) % (10 ** 9), a % (10 ** 9)
        f *= Decimal(phi)
        m = str(f)[:10].replace('.', '')
        mantissa = float(m)
        i += 1
    print i

u.exec_time(p104)

