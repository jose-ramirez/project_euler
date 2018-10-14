# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 =
# 145.
#
# Find the sum of all numbers which are equal to the sum of
# the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not
# included.

from context import f

# Hasta 10^6, porque ya se cuanto da la suma, y no necesito
# llegar tan lejos; pero en realidad hay que testar hasta
# 10^7, que es lo que la matematica te da como estimado para
# estar seguro de que el resultado final estara certo:
def p34():
    factorial_list = [f.factorial(n) for n in range(10)]
    total = 0
    for n in range(3, 10 ** 7):
        if n == f.factorial_sum(n, factorial_list):
            total += n
    return total

# Esta forma es mas rapida, aunque necesita muuucha mas
# memoria:
def p34_():
    total = 0
    m = 10
    l = []
    facts = [f.factorial(j) for j in range(10)]
    for f1 in facts:
        l.append(f1)
    while m < 10 ** 7:
        l.append(l[m // 10] + facts[m % 10])
        if m == l[m]:
            total += m
        m += 1
    return total

print(p34_())