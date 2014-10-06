#coding: UTF-8
#Consider the isosceles triangle with base length, b = 16,
#and legs, L = 17.
#
#By using the Pythagorean theorem it can be seen that the
#height of the triangle, h = √(172 − 82) = 15, which is
#one less than the base length.
#
#With b = 272 and L = 305, we get h = 273, which is one more
#than the base length, and this is the second smallest
#isosceles triangle with the property that h = b ± 1.
#
#Find ∑ L for the twelve smallest isosceles triangles for
#which h = b ± 1 and b, L are positive integers.

from utils import Utils

u = Utils()

def p138():
    a, b = 76, 17
    num_triangles = 1
    total = b
    while num_triangles < 12:
        a, b = 9 * a + 40 * b, 2 * a + 9 * b
        if a % 5 == 1 or a % 5 == 4:
            total += b
            num_triangles += 1
    print total

u.exec_time(p138)