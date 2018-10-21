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

from context import utils, point, line, ellipse
from math import atan, fabs

u = utils.Utils()
e = ellipse.Ellipse(5.0, 10.0)

def get_line(p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    m = (y2 - y1) / (x2 - x1)
    return line.Line(m, y1 - m * x1)

# Now, to the problem at hand:
def next_point(p, pt):
    laser_ray = get_line(p, pt)
    tangent_line = e.tangent(pt)
    axis = tangent_line.perpendicular(pt)
    reflected_ray = laser_ray.reflect(axis)
    pa, pb = list(e.intersect(reflected_ray))
    return pa if pb.close_enough(pt) else pb

def p144():
    i = 0
    p = point.Point([0.0, 10.1])
    pt = point.Point([1.4, -9.6])
    while (not fabs(pt.x) <= 0.01) or pt.y < 0:
        p, pt = pt, next_point(p, pt)
        i += 1
    return i

print(p144())