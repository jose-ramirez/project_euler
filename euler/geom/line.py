from point import Point

class Line:
    def __init__(self, m, b):
        """
            Our base eq. here will be y = mx + b.
        """
        self.m = m
        self.b = b

    def reflect_from_axis(self, axis):
        """
            Returns the reflected line of this one
            with respect to the given axis.
        """
        return Line(1.0, 0.0)

    def perpendicular_at_point(self, point):
        """
            Returns the perpendicular to this line'
            with respect to the given point.
        """
        return Line(1.0, 0.0)