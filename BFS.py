
from collections import deque
from Point import Point
from queueNode import queueNode


# Check whether given cell(row,col) is a valid cell or not
def is_valid(row: int, col: int, ROW: int, COL: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# Function to find the shortest path between
# a given source cell to a destination cell.
def bfs(board, src: Point, dest: Point):
    ROW = COL = len(board)

    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]

    # Check source and destination cell
    # of the matrix have value -1 (obstacle)
    if board[src.x][src.y] == -1 or board[dest.x][dest.y] == -1:
        return -1

    # This boolean matrix for the visited cell
    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    queue = deque()

    # Distance of source cell is 0
    source_node = queueNode(src, 0, [])
    # Enqueue source cell
    queue.append(source_node)

    # Do a BFS starting from source cell
    while queue:
        # Dequeue the front cell
        current_node = queue.popleft()
        # Take the point of the current_node
        pt_current = current_node.pt
        # If we have reached the destination cell, we are done
        if Point.equal(pt_current, dest):
            # Add the Point to the path
            current_node.path.append(pt_current)
            return current_node

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt_current.x + row_num[i]
            col = pt_current.y + col_num[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (is_valid(row, col, ROW , COL) and
                    board[row][col] == 0 and
                    not visited[row][col]):
                # Mark has visited
                visited[row][col] = True
                # Create path to the new node and copy the path from current_node
                path = current_node.path.copy()
                # Add the current node to the path of is neighbours
                if current_node.pt != src:
                    path.append(current_node.pt)
                # Create the new neighbor with Point, distant and the path from the source
                Neighbor_cell = queueNode(Point(row, col), current_node.dist + 1, path)
                # Add the new neighbor to the queue
                queue.append(Neighbor_cell)

    # Return -1 if destination can not be reached
    return -1


def bfs_few_steps(board, src: Point, dest: Point):
    ROW = COL = len(board)

    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]

    # Check source and destination cell
    # of the matrix have value -1 (obstacle)
    if board[src.x][src.y] == -1 or board[dest.x][dest.y] == -1:
        return -1

    # This boolean matrix for the visited cell
    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    queue = deque()

    # Distance of source cell is 0
    source_node = queueNode(src, 0, [])
    # Enqueue source cell
    queue.append(source_node)

    # Do a BFS starting from source cell
    while queue:
        # Dequeue the front cell
        current_node = queue.popleft()
        # Take the point of the current_node
        pt_current = current_node.pt
        # If we have reached the destination cell, we are done
        if Point.equal(pt_current, dest):
            # Add the Point to the path
            current_node.path.append(pt_current)
            return current_node

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt_current.x + row_num[i]
            col = pt_current.y + col_num[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (is_valid(row, col, ROW, COL) and
                    board[row][col] != -1 and
                    not visited[row][col]):
                # Mark has visited
                visited[row][col] = True
                # Create path to the new node and copy the path from current_node
                path = current_node.path.copy()
                # Add the current node to the path of is neighbours
                if current_node.pt != src:
                    path.append(current_node.pt)
                # Create the new neighbor with Point, distant and the path from the source
                Neighbor_cell = queueNode(Point(row, col), current_node.dist + 1, path)
                # Add the new neighbor to the queue
                queue.append(Neighbor_cell)

    # Return -1 if destination can not be reached
    return -1

