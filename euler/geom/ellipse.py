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

    def intersects(self, line):
        """
            Should return the points of intersection
            of the line and this ellipse, if any.
            Should never return None
        """
        return [Point(0.0, 0.0), Point(0.0, 0.0)]

    def tangent(self, point):
        """
            Returns the taangent line to this ellipse
            at the given point. For now, I'll assume
            the point always lies on the ellipse, so it
            should always return a valid line.
        """
        return Line(1.0, 0.0)
