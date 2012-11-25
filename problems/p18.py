#By starting at the top of the triangle below and moving to adjacent
#numbers on the row below, the maximum total from top to bottom is 23.
#
#3
#7 4
#2 4 6
#8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
#Find the maximum total from top to bottom of the triangle below:
#
#75
#95 64
#17 47 82
#18 35 87 10
#20 04 82 47 65
#19 01 23 75 03 34
#88 02 77 73 07 63 67
#99 65 04 28 06 16 70 92
#41 41 26 56 83 40 80 70 33
#41 48 72 33 47 32 37 16 94 29
#53 71 44 65 25 43 91 52 97 51 14
#70 11 33 28 77 73 17 78 39 68 17 57
#91 71 52 38 17 14 91 43 58 50 27 29 48
#63 66 04 68 89 53 67 30 73 16 69 87 40 31
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

import sys
sys.path.append('../utils')
from utils import to_matrix, show

def p18(filename):
    t = to_matrix(filename)
    sums = [t[0], [t[0][0] + x for x in t[1]]]
    for i in range(2, len(t)):
        m = len(t[i])
        l = [t[i][j] + max(sums[i - 1][j], sums[i - 1][j - 1]) \
                 for j in range(1, m - 1)]

        l.insert(0, sums[i - 1][0] + t[i][0])
        l.append(sums[i - 1][-1] + t[i][-1])
        sums.append(l)
    return max(sums[-1])

print p18('../data/triangle.in')
