from Point import Point
from Robot import Robot


class RobotPoint:
    def __init__(self, robot: Robot, prev: Point):
        self.prev = prev
        self.robot = robot
