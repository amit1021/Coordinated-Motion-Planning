
# A data structure for queue used in BFS
import Point


class queueNode:
    def __init__(self, current_point: Point, dist: int, path: []):
        self.pt = current_point  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source to the dest
        self.path = path

    def __repr__(self):
        return str(self.path)

    def __str__(self):
        return str(self.path)
