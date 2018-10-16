# By counting carefully it can be seen that a rectangular grid
# measuring 3 by 2 contains eighteen rectangles.
#
# Although there exists no rectangular grid that contains
# exactly two million rectangles, find the area of the grid
# with the nearest solution.

from context import utils

u = utils.Utils()

def p85():
    MAX_W = 100
    MAX_H = 100
    min_w = 100
    min_h = 100
    min_d = 10 ** 9
    mat, val = u.binom(MAX_W, MAX_H)
    for w in range(MAX_W):
        for h in range(w, MAX_H):
            d = abs(2000000 - mat[w + 1][2] * mat[h + 1][2])
            if d < min_d:
                min_w, min_h, min_d = w, h, d

    return min_w, min_h, min_d, min_w * min_h

print(p85()[3])