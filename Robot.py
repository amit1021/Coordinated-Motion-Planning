from Point import Point

class Robot:
      def __init__(self, current_place:Point, end_place:Point, robot_number):
            self.current_place = current_place
            self.end_place = end_place
            self.robot_number = robot_number


      def __str__(self):
            return "Current Place: " + str(self.current_place) + "End Place: " + str(self.end_place)

      def __repr__(self):
            return "R" + str(self.robot_number) + " end place " + str(self.end_place)












# from Point import Point
#
# class Robot:
#       def __init__(self, current_place:Point, end_place:Point, num):
#             self.current_place = current_place
#             self.end_place = end_place
#             self.stuck = 0
#             self.num = num
#
#
#       def __str__(self):
#             return "Current Place: " + str(self.current_place) + "End Place: " + str(self.end_place)
#
#       def __repr__(self):
#             return "R" + str(self.num)
