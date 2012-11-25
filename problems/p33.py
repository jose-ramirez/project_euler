#The fraction 49/98 is a curious fraction, as an inexperienced mathematician
#in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
#is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction, less
#than one in value, and containing two digits in the numerator and denominator.
#
#If the product of these four fractions is given in its lowest common terms,
#find the value of the denominator.

from fractions import gcd

def p33():
    num = 1
    den = 1
    for i in range(10, 100):
        for j in range(10, 100):
            if j % 10 != 0 and i % 10 != 0:
                a, b, c, d = i / 10, i % 10, j / 10, j % 10
                if b == c and a * j == i * d and i < j:
                    num *= a
                    den *= d
    return den / gcd(num, den)

print p33()
