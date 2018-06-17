# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

def full_sum(m):
    a =[1, 3]
    for i in range(3, m + 2):
        a.append((2 * i - 3) ** 2 + 2 * (i - 1))
    b = [5]
    for j in range(2, m + 1):
        b.append(a[j] + 2 * j)
    c = [7]
    for k in range(2, m):
        c.append(b[k - 1] + 2 * k)
    d = [9] + [(2 * l + 1) ** 2 for l in range(2, m)]
    return sum([sum(s) for s in [a[:-1], b[:-1], c, d]])

def p28():
    print(full_sum(501))