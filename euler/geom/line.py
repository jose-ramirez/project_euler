from point import Point

class Line:
    def __init__(self, m, b):
        """
            Our base eq. here will be y = mx + b.
        """
        self.m = m
        self.b = b

    def reflect(self, axis):
        """
            Returns the reflected line of this one
            with respect to the given axis.
        """
        p = self.intersect(axis)
        return Line(1.0, 0.0)

    def perpendicular(self, point):
        """
            Returns the perpendicular to this line
            with respect to the given point.
        """
        m_p = -1.0 / self.m
        x, y = point.x, point.y
        b_p = y - m_p * x
        return Line(m_p, b_p)

    def angle(self, other_line):
        """
            Returns the angle between this line
            and another one.
            Should it be 0 if they are parallel/the same?
        """
        pass

    def intersect(self, line):
        """
            Returns the intersection point of this
            line and the ons passed as parameter,
            or None if the lines are parallel enough.
        """
        m1, m2 = this.m, other_line.m
        b1, b2 = this.b, other_line.b
        if m1 == m2: # lines are parallel, or equal
            return None
        else:
            p_x = (b1 - b2) / (m2 - m1)
            p_y = (m2 * b1 - m1 * b2) / (m2 - m1)
            return Point([p_x, p_y])

    def rotate(self, p, theta):
        """
            Returns the result of rotating this line
            theta radians with respect to p.
        """
        pass