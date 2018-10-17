#coding: UTF-8
# In laser physics, a "white cell" is a mirror system that
# acts as a delay line for the laser beam. The beam enters
# the cell, bounces around on the mirrors, and eventually
# works its way back out.
#
# The specific white cell we will be considering is an
# ellipse with the equation 4x^2 + y^2 = 100.
#
# The section corresponding to −0.01 ≤ x ≤ +0.01 at the
# top is missing, allowing the light to enter and exit
# through the hole.
#
# The light beam in this problem starts at the point
# (0.0,10.1) just outside the white cell, and the beam first
# impacts the mirror at (1.4,-9.6).
#
# Each time the laser beam hits the surface of the ellipse,
# it follows the usual law of reflection "angle of incidence
# equals angle of reflection." That is, both the incident and
# reflected beams make the same angle with the normal line at
# the point of incidence.
#
# The slope m of the tangent line at any point (x,y) of the
# given ellipse is: m = −4x/y.
#
# The normal line is perpendicular to this tangent line at
# the point of incidence.
#
# How many times does the beam hit the internal surface of
# the white cell before exiting?

from context import utils
from math import atan

u = utils.Utils()

def get_tangent_equation(p0):
    """
        Return tangent equation:
    """
    mt = [1, -(4 * p0[0]) / p0[1]]
    bt = [0, 100. / p0[1]]
    return mt, bt

def close_enough(p1, p2):
    s = u.sub(p1, p2)
    return abs(s[0]) < 1e-5 and abs(s[1]) < 1e-5

# Now, to the problem at hand:

def next_point(p, pt):
    # light ray:
    mr, br = u.get_line_equation(p, pt)

    # tangent at intersection of ray and ellipse:
    mt, bt = get_tangent_equation(pt)

    # angle between these lines:
    theta0 = atan((mr[1] - mt[1]) / (1 + (mr[1] * mt[1])))
    #print 'theta = {0} rad'.format(theta0)

    # get reflected ray equation:
    mr_, br_ = u.rotate_line(mt, bt, pt, -theta0)

    # Solve equation given its coefficients. This solves
    # for the parameter t!!!
    a = (4 * mr_[0] * mr_[0]) + (mr_[1] * mr_[1])
    b = (8 * mr_[0] * br_[0]) + (2 * mr_[1] * br_[1])
    c = (4 * br_[0] * br_[0]) + (br_[1] * br_[1]) - 100
    t = u.solve_quadratic(a, b, c)

    # get right coordinate:
    ps = [u.get_point(mr_, br_, t[0]),
          u.get_point(mr_, br_, t[1])]
    return ps[1 if close_enough(ps[0], pt) else 0]

def p144():
    i = 0
    p, pt = [0.0, 10.1], [1.4, -9.6]
    while  (-0.01 > pt[0] or pt[0] > 0.01) or pt[1] < 0:
        p, pt = pt, next_point(p, pt)
        i += 1
    return i

print(p144())