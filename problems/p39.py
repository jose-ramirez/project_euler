#If p is the perimeter of a right angle triangle with
#integral length sides, {a,b,c}, there are exactly three
#solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p <= 1000, is the number of solutions
#maximised?

from utils import Utils

def count_solutions(p):
    total = 0
    for a in xrange(1, p):
        for b in range(a, p):
            c = p - a - b
            if 0 < a <= b < c:
                if c ** 2 == a ** 2 + b ** 2:
                    total += 1
    return total

def p39():
    max_count = -1
    perimeter = -1
    for p in range(3, 1001):
        m = count_solutions(p)
        if m > max_count:
            max_count = m
            perimeter = p
    print max_count, perimeter

u = Utils()
u.exec_time(p39)