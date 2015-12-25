#encoding:UTF-8
#Euler discovered the remarkable quadratic formula:
#
#n^2 + n + 41
#
#It turns out that the formula will produce 40 primes for the consecutive values
#n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
#by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
#The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 primes
#for the consecutive values n = 0 to 79. The product of the coefficients, −79 and
#1601, is −126479.
#
#Considering quadratics of the form:
#
#n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |−4| = 4
#Find the product of the coefficients, a and b, for the quadratic expression that
#produces the maximum number of primes for consecutive values of n, starting with
#n = 0.

from math import fabs
def a(r):
  return 1 - (2 * r)

def b(r):
  return r ** 2 - r + 41

def f(r):
  return (fabs(a(r)) < 1000) and (fabs(b(r)) < 1000)

def p27():
  s = 0
  p = 0
  while f(s):
      p = a(s) * b(s)
      s += 1
  return p

print p27()
