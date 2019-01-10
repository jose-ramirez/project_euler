# Susan has a prime frog.
# Her frog is jumping around over 500 squares numbered 1 to 500. He can only jump
# one square to the left or to the right, with equal probability, and he cannot
# jump outside the range [1;500].
# (if it lands at either end, it automatically jumps to the only available square
# on the next move.)
#
# When he is on a square with a prime number on it, he croaks 'P' (PRIME) with
# probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before jumping to
# the next square.
# When he is on a square with a number on it that is not a prime he croaks 'P'
# with probability 1/3 or 'N' with probability 2/3 just before jumping to the next
# square.
#
# Given that the frog's starting position is random with the same probability for
# every square, and given that she listens to his first 15 croaks, what is the
# probability that she hears the sequence PPPPNNPPPNPPNPN?
#
# Give your answer as a fraction p/q in reduced form.

from fractions import Fraction
from euler.utils import Utils

u = Utils()

d = {}

primes = u.sieve(500)

for i in range(1, 501):
  if i in primes:
    d[("P", i)] = Fraction(2, 3)
    d[("N", i)] = Fraction(1, 3)
  else:
    d[("N", i)] = Fraction(2, 3)
    d[("P", i)] = Fraction(1, 3)

def p(s, i):
  if (s, i) in d.keys():
    return d[(s, i)]
  else:
    if i == 1:
      d[(s, 1)] = p(s[0], 1) * p(s[1:], 2)
    elif i == 500:
      d[(s, 500)] = p(s[0], 500) * p(s[1:], 499)
    else:
      d[(s, i)] = Fraction(1, 2) * (p(s[0], i) * p(s[1:], i + 1) + p(s[0], i) * p(s[1:], i - 1))
  return d[(s, i)]

def p329():
  a = sum([p("PPPPNNPPPNPPNPN", i) for i in range(1, 501)]) / 500
  return a

print(p329())