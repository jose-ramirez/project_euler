#If we list all the natural numbers below 10 that are multiples
#of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
#23. Find the sum of all the multiples of 3 or 5 below 1000.

import euler.numbers.functions as f

def p1():
    return 3 * f.sum_up_to(333) + \
    5 * f.sum_up_to(200) - \
    15 * f.sum_up_to(66) - 1000

print(p1())