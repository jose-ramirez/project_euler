# Consider quadratic Diophantine equations of the form:
#
# x^2 – D*y^2 = 1
#
# For example, when D=13, the minimal solution in x is 649^2 – 13*180^2 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is
# square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
# following:
#
# 3^2 – 2*2^2 = 1
# 2^2 – 3*1^2 = 1
# 9^2 – 5*4^2 = 1
# 5^2 – 6*2^2 = 1
# 8^2 – 7*3^2 = 1
#
# Hence, by considering minimal solutions in x for D \leq 7, the largest x is
# obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained.

from euler.numbers import pell

def p66():
    solutions = [(D, pell.min_sol(D)[0]) for D in range(2, 1001) if not pell.is_square(D)]
    sorted_solutions = sorted(solutions, key=lambda p: p[1])
    return sorted_solutions[-1]

print(p66())