

# Check whether given cell(row,col)
# is a valid cell or not
from collections import deque

from Point import Point
from queueNode import queueNode


def isValid(row: int, col: int ,ROW: int, COL: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point):

    ROW = COL = len(mat)

    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]


    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y] == 13 or mat[dest.x][dest.y] == -1:
        return -1

    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    q = deque()

    # Distance of source cell is 0
    s = queueNode(src, 0, [])
    q.append(s)  # Enqueue source cell

    # Do a BFS starting from source cell
    while q:

        curr = q.popleft()  # Dequeue the front cell

        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            curr.path.append(curr.pt)
            return curr

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row, col,ROW , COL) and
                    mat[row][col] == 0 and
                    not visited[row][col]):
                visited[row][col] = True
                p = []
                for point in curr.path:
                    # if it's not the start place
                    if point != src:
                        p.append(point)
                p.append(curr.pt)
                Adjcell = queueNode(Point(row, col), curr.dist + 1, p)
                q.append(Adjcell)

    # Return -1 if destination cannot be reached
    return -1

