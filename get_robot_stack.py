from BFS import bfs, is_valid
from Move_Robot import move_robot, move_robot_to_dest, move_robot_one_step
from Point import Point
from RobotPoint import RobotPoint
from params import FindRobotByNumber


row_num = [1, 0, 0, -1]
col_num = [0, 1, -1, 0]


def stack_robot(robot, board, robot_queue_node, boardgame2):
    robot_old_place = []
    for p in robot_queue_node.path:
        if board[p.x][p.y] == 0:
            move_robot_one_step(p, board, robot, boardgame2)
        else:
            r = FindRobotByNumber( board[p.x][p.y])
            for i in range(4):
                row = p.x + row_num[i]
                col = p.y + col_num[i]
                dest = Point(row, col)
                if is_valid(row, col, len(board), len(board)) and board[row][col] == 0 and dest not in robot_queue_node.path :
                    # add to back list
                    robot_point = RobotPoint(r, dest)
                    robot_old_place.append(robot_point)
                    # move robot to new place
                    move_robot_one_step(dest,board, r, boardgame2)
                    move_robot_one_step(p, board, robot, boardgame2)
                    break
    robot_back(board, robot_old_place, boardgame2)


def robot_back(board, robot_old_place, boardgame2):
    for r in robot_old_place:
        p = r.robot.end_place
        if board[p.x][p.y] == 0:
            move_robot_one_step(p, board, r.robot, boardgame2)
        else:
            print("========================================================== ", board[p.x][p.y])
    return





