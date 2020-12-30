from Point import Point

class Robot:
      def __init__(self, current_place:Point, end_place:Point):
            self.current_place = current_place
            self.end_place = end_place
            self.stuck = 0

      def __str__(self):
            return "Current Place: " + str(self.current_place) + "End Place: " + str(self.end_place)

      def __repr__(self):
            return "Robot"
            # return "Start Place: " + str(self.startPlace) + "     Current Place: " + str(self.currentPlace) + "     End Place: " + str(self.endPlace) + "\n"

