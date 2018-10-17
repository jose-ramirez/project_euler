#coding: UTF-8
# Three distinct points are plotted at random on a Cartesian
# plane, for which -1000 ≤ x, y ≤ 1000, such that a
# triangle is formed.
#
# Consider the following two triangles:
#
# A(-340,495), B(-153,-910), C(835,-947)
#
# X(-175,41), Y(-421,-714), Z(574,-645)
#
# It can be verified that triangle ABC contains the origin,
# whereas triangle XYZ does not.
#
# Using triangles.txt (right click and 'Save Link/Target
# As...'), a 27K text file containing the co-ordinates of one
# thousand "random" triangles, find the number of triangles
# for which the interior contains the origin.
#
# NOTE: The first two examples in the file represent the
# triangles in the example given above.

from context import utils

u = utils.Utils()

def p102():
    total = 0
    P = [0, 0]
    triangles = []

    with open('data/p102_triangles.txt', 'r') as file:
        for line in file.readlines():
            points = map(int, line.split(','))
            a1, a2, b1, b2, c1, c2 = list(points)
            total += u.in_triangle(P, [(a1, a2), (b1, b2), (c1, c2)])
    return total

print(p102())