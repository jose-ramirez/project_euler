#coding: UTF-8
# It is possible to show that the square root of two can be
# expressed as an infinite continued fraction.
#
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408,
# but the eighth expansion, 1393/985, is the first example
# where the number of digits in the numerator exceeds the
# number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions
# contain a numerator with more digits than denominator?

def p57():
    total = 0
    a = [1, 3]
    b = [1, 2]
    for i in range(1000):
        a_ = 2 * a[-1] + a[-2]
        b_ = 2 * b[-1] + b[-2]
        a.append(a_)
        b.append(b_)
        if len(str(a_)) > len(str(b_)):
            total += 1
    return total

print(p57())