
from BFS import bfs, bfs_few_steps
from Point import Point

from params import addRobotToDest, removeRobotToListNot_dest, FindRobotByNumber, addRobotToListNot_dest, \
    removeRobotToDest, getRobotToListNot_destSize, getRobotListDestSize, getRobotToListNot_dest, robot_list


row_num = [1, 0, 0, -1]
col_num = [0, 1, -1, 0]

def move_robot_all_path(board, robot, robot_queue_node ,boardgame1):
    # Run on robot's path to the destination

    for p in robot_queue_node.path:
        # Delete the robot from is old place in the board
        board[robot.current_place.x][robot.current_place.y] = 0
        boardgame1.robot[robot.current_place.x][robot.current_place.y] = 0
        # Update the new point of the robot
        robot.current_place = p
        # Update the board with the new point of the robot
        board[robot.current_place.x][robot.current_place.y] = robot.robot_number
        boardgame1.robot[robot.current_place.x][robot.current_place.y] = robot.robot_number
        # When the robot reach is destination
        #boardgame1.cratetable()
        if Point.equal(robot.current_place, robot.end_place):
            # Remove from robot list
            removeRobotToListNot_dest(robot)
            # Add to list of the robots who reach their destination
            addRobotToDest(robot)
    boardgame1.cratetable()
    # Just for checking the function (delete after)
    if not Point.equal(robot.current_place, robot.end_place):
        print("not reach the goal")


def move_robot_few_steps(board,robot, robot_queue_node, boardgame1):
    # Run on robot's path to the destination
    for p in robot_queue_node.path:
        if p == 0:
            # Delete the robot from is old place in the board
            board[robot.current_place.x][robot.current_place.y] = 0
            boardgame1.robot[robot.current_place.x][robot.current_place.y] = 0
            # Update the new point of the robot
            robot.current_place = p
            # Update the board with the new point of the robot
            board[robot.current_place.x][robot.current_place.y] = robot.robot_number
            boardgame1.robot[robot.current_place.x][robot.current_place.y] = robot.robot_number
            # When the robot reach is destination
            if Point.equal(robot.current_place, robot.end_place):
                # Remove from robot list
                removeRobotToListNot_dest(robot)
                # Add to list of the robots who reach their destination
                addRobotToDest(robot)

                return
        else:
            return
    boardgame1.cratetable()
    # Just for checking the function (delete after)
    if not Point.equal(robot.current_place, robot.end_place):
        print("not reach the goal")


def moveRobotStuck(board, robot, boardgame1):
    robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
    for p in robot_queue_node.path:
        if board[p.x][p.y] == 0:
            moveOneStep(board, robot, p, boardgame1)
        else:
            r = FindRobotByNumber(board[p.x][p.y])
            moveRobotElseOneStep(board, r, p, boardgame1)
            moveOneStep(board, robot, p, boardgame1)


def moveOneStep(board, robot, p, boardgame1):
    if board[p.x][p.y] == 0:
        # Delete the robot from is old place in the board
        board[robot.current_place.x][robot.current_place.y] = 0
        boardgame1.robot[robot.current_place.x][robot.current_place.y] = 0
        #boardgame11.robot[robot.current_place.x][robot.current_place.y] = 0
        # Update the new point of the robot
        robot.current_place = p
        # Update the board with the new point of the robot
        board[robot.current_place.x][robot.current_place.y] = robot.robot_number
        boardgame1.robot[robot.current_place.x][robot.current_place.y] = robot.robot_number
        # When the robot reach is
        boardgame1.cratetable()
        if robot.current_place.equal(robot.end_place):
            # Remove from robot list
            removeRobotToListNot_dest(robot)
            # Add to list of the robots who reach their destination
            addRobotToDest(robot)
            return
        else:
            return
    return

def moveRobotElseOneStep(board, robot, p, boardgame1):
    flag = False
    if robot.current_place.equal(robot.end_place):
        flag = True

    # for on adjacent cells
    for i in range(4):
        row = p.x + row_num[i]
        col = p.y + col_num[i]
        if board[row][col] == 0:
            p_move = Point(row,col)
            moveOneStep(board, robot, p_move, boardgame1)
            if not robot.current_place.equal(robot.end_place) and flag:
                addRobotToListNot_dest(robot)
                removeRobotToDest(robot)
            return
