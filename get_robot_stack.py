from BFS import bfs, bfs_few_steps
from Move_Robot import move_robot, move_robot_to_dest
from Point import Point
from RobotPoint import RobotPoint
from params import FindRobotByNumber


row_num = [1, 0, 0, -1]
col_num = [0, 1, -1, 0]


def stack_robot(robot, board, robot_queue_node, blank_space, boardgame2):
    robot_to_move = []
    robot_back = []
    number_of_steps = 0
    for p in robot_queue_node.path:
        if board[p.x][p.y] != 0:
            r = FindRobotByNumber(board[p.x][p.y])
            robot_to_move.append(r)
    dir = get_direction(p, len(board))
    if dir == "UP":
        x = blank_space + 1
        y = robot.current_place.y
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x, y + number_of_robots )
            if y + number_of_robots >= len(board) - blank_space - 1:
                dest = Point(x, y - number_of_robots - 1)
            robot_queue_node_r = bfs(board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_back.append(robot_point)
                number_of_steps += move_robot(board, r, robot_queue_node_r, boardgame2)
                number_of_robots -= 1
    if dir == "DOWN":
        x = len(board) - blank_space - 1
        y = robot.current_place.y
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x, y + number_of_robots)
            if y + number_of_robots >= len(board) - blank_space - 1:
                dest = Point(x, y - number_of_robots - 1)
            robot_queue_node_r = bfs(board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_back.append(robot_point)
                number_of_steps += move_robot(board, r, robot_queue_node_r, boardgame2)
                number_of_robots -= 1
    if dir == "LEFT":
        x = robot.current_place.x
        y = blank_space + 1
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x + number_of_robots, y)
            if x + number_of_robots >= len(board) - blank_space - 1:
                dest = Point(x - number_of_robots - 1, y)
            robot_queue_node_r = bfs(board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_back.append(robot_point)
                number_of_steps += move_robot(board, r, robot_queue_node_r, boardgame2)
                number_of_robots -= 1
    if dir == "RIGHT":
        x = robot.current_place.x
        y = len(board) - blank_space - 1
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x + number_of_robots, y)
            if x + number_of_robots >= len(board) - blank_space - 1:
                dest = Point(x - number_of_robots - 1, y)
            robot_queue_node_r = bfs(board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_back.append(robot_point)
                number_of_steps += move_robot(board, r, robot_queue_node_r, boardgame2)
                number_of_robots -= 1
    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
    if robot_queue_node != -1:
        number_of_steps += move_robot(board,robot, robot_queue_node, boardgame2)
    number_of_steps += move_robots_back(board, robot_back, boardgame2)
    return number_of_steps


def move_robots_back(board, robot_old_place , boardgame2):
    number_of_steps = 0
    # reverse the robots -> return robots
    for r in reversed(robot_old_place):
        robot_queue_node = bfs(board, r.robot.current_place, r.robot.end_place)
        if robot_queue_node != -1:
            num = move_robot(board, r.robot, robot_queue_node, boardgame2)
            number_of_steps += num
        else:
            print("========================================================== move_robots_back")
    return number_of_steps


def get_direction(p, n):
    if p.x < n/2 and p.y > n/4 and p.y < (3 * (n/4)):
        return "UP"
    if p.x >= n/2 and p.y > n/4 and p.y < (3 * (n/4)):
        return "DOWN"
    if p.y < n/2 and p.x > n/4 and p.x < (3 * (n/4)):
        return "LEFT"
    if p.y >= n/2 and p.x > n/4 and p.x < (3 * (n/4)):
        return "RIGHT"


def move_robot_to_final_place(board, robot ,blank_space,direc, boardgame2):
    number_of_steps = 0
    # move robot to final place
    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
    if robot_queue_node != -1:
        num = move_robot_to_dest(board, robot, robot_queue_node , boardgame2)
        number_of_steps +=num
        return number_of_steps
    else:
        dest = 0
        if direc == "LEFT":
            dest = Point( robot.current_place.x,robot.current_place.y + blank_space + 1)
        if direc == "RIGHT":
            dest = Point(robot.current_place.x, robot.current_place.y - blank_space - 1)
        if direc == "UP":
            dest = Point(robot.current_place.x+ blank_space + 1, robot.current_place.y)
        if direc == "DOWN":
            dest = Point(robot.current_place.x - blank_space - 1, robot.current_place.y )

        robot_queue_node = bfs(board, robot.current_place, dest)
        if robot_queue_node != -1:
            number_of_steps += move_robot(board, robot, robot_queue_node , boardgame2)

        robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
        number_of_steps += stack_robot(robot, board, robot_queue_node,blank_space, boardgame2)
        # robot_queue_node = bfs(board, robot.current_place, dest)
        # if robot_queue_node != -1:
        #     number_of_steps += move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
    return number_of_steps


