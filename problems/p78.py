#Let p(n) represent the number of different ways in which n
#coins can be separated into piles. For example, five coins
#can separated into piles in exactly seven different ways, so
#p(5)=7.
#
#OOOOO
#OOOO O
#OOO OO 
#OOO O O
#OO OO O
#OO O O O
#O O O O O
#
#Find the least value of n for which p(n) is divisible by
#one million.

from utils import Utils

u = Utils()

p = [1, 1]

def part2(n):
    sum, k, a, b, sgn = 0, 4, 2, 1, 1
    while n >= a:
        sum += sgn * (p[n - a] + p[n - b])
        a += k + 1
        b += k
        sgn *= -1
        k += 3
    if n >= b:
        sum += sgn * p[n - b]
    return sum % (10 ** 6)

def p78():
    i = 1
    while p[i] != 0:
        i += 1
        d = part2(i)
        p.append(d)
    print i

u.exec_time(p78)