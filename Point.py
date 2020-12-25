# To store matrix cell cordinates
from numpy import double


class Point:
    def __init__(self, x: double, y: double):
        self.x = x
        self.y = y

    def equal(p1, p2):
        return p1.x == p2.x and p1.y == p2.y

    def __str__(self):
        return "(%s,%s)" %(self.x, self.y)

    def __repr__(self):
        return "(%s,%s)" %(self.x, self.y)

