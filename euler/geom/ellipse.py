from point import Point
from line import Line

class Ellipse:
    def __init__(self, a, b):
        """
            The equation for the ellipse we'll
            be using is (x/a)^2 + (y/b)^2 = 1.
        """
        self.a = a
        self.b = b

    def intersect(self, line):
        """
            Should return the points of intersection
            of the line and this ellipse, if any,
            or an empty list if none is found.
        """
        return [Point([0.0, 0.0]), Point([0.0, 0.0])]

    def tangent(self, point):
        """
            Returns the taangent line to this ellipse
            at the given point. For now, I'll assume
            the point always lies on the ellipse, so it
            should always return an actual tangent line.
        """
        x, y = point.x, point.y
        m = (- b ** 2 / a ** 2) * (x / y)
        return Line(m, y - m * x)
