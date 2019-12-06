# k defects are randomly distributed amongst n integrated-circuit chips produced
# by a factory (any number of defects may be found on a chip and each defect is
# independent of the other defects).
#
# Let p(k,n) represent the probability that there is a chip with at least 3
# defects. For instance p(3,7) ≈ 0.0204081633.
#
# Find p(20 000, 1 000 000) and give your answer rounded to 10 decimal places in
# the form 0.abcdefghij

from math import log, exp
from euler.utils import Utils
LOG2 = log(2)
u = Utils()


def log_count_x_pairs(n, k, x):
    return u.log_nPr(n, k - x) + u.log_nPr(k, 2 * x) - u.log_factorial(x) - (x * LOG2)


def p307():
    n, k = 1000000, 20000
    POW = k * log(n)
    total_prob = exp(u.log_nPr(n, k) - POW)
    x_max = k // 2
    for x in range(1, x_max + 1):
        val = exp(log_count_x_pairs(n, k, x) - POW)
        total_prob += val
    return 1 - total_prob


print(p307())
