#coding: UTF-8
#Consider the isosceles triangle with base length, b = 16,
#and legs, L = 17.
#
#By using the Pythagorean theorem it can be seen that the
#height of the triangle, h = √(17^2 − 8^2) = 15, which is
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
    """
        Here the problem was reduced to the following Pell
        equation:

        (5b ± 4)^2 - 20L^2 = -4,
        
        with solutions given by the following recurrences:
        (a_0, L_0) = (16, 17),
        (a_{k + 1}, L_{k + 1}) =
            (9 * a_k + 40 * L_k, 2 * a_k + 9 * L_k),
        with a_k = 5b_k ± 4 \forall k \geq 0.
    """
    a, L = 76, 17
    num_triangles = 1
    total = b
    while num_triangles < 12:
        a, L = 9 * a + 40 * L, 2 * a + 9 * L
        if a % 5 == 1 or a % 5 == 4:
            total += L
            num_triangles += 1
    print total

u.exec_time(p138)