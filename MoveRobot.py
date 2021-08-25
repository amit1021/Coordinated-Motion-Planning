from BFS import bfs, bfs_few_steps
from Point import Point
from RobotDetails import find_robot_by_number
from RobotPoint import RobotPoint
from Test import test

ROW_NUM = [1, 0, 0, -1]
COL_NUM = [0, 1, -1, 0]


def move_robot(eb, robot, robot_queue_node):
    number_of_steps = 0
    # run on robot's path to the destination
    for p in robot_queue_node.path:
        # delete the robot from is old place in the board
        eb.board[robot.current_place.x][robot.current_place.y] = 0
        eb.board_ui.src[robot.current_place.x][robot.current_place.y] = 0
        # update the new point of the robot
        robot.current_place = p
        # update the board with the new point of the robot
        eb.board[robot.current_place.x][robot.current_place.y] = robot.robot_number
        eb.board_ui.src[robot.current_place.x][robot.current_place.y] = robot.robot_number
        # add step
        number_of_steps += 1
    eb.board_ui.cratetable()
    # print("robot moved : ", robot.robot_number)
    return number_of_steps


def move_robot_one_step(eb, dest, robot):
    # delete the robot from is old place in the board
    eb.board[robot.current_place.x][robot.current_place.y] = 0
    eb.board_ui.src[robot.current_place.x][robot.current_place.y] = 0
    # update the new point of the robot
    robot.current_place = dest
    # update the board with the new point of the robot
    eb.board[robot.current_place.x][robot.current_place.y] = robot.robot_number
    eb.board_ui.src[robot.current_place.x][robot.current_place.y] = robot.robot_number
    eb.board_ui.cratetable()
    return


def move_robots_back(eb, robot_prev_place):
    number_of_steps = 0
    # reverse the robots -> return robots
    for r in reversed(robot_prev_place):
        robot_queue_node = bfs(eb.board, r.robot.current_place, r.prev)
        if robot_queue_node != -1:
            number_of_steps += move_robot(eb, r.robot, robot_queue_node)
    return number_of_steps


def move_robots_back_test(eb, robot_prev_place):
    number_of_steps = 0
    # reverse the robots -> return robots
    for r in reversed(robot_prev_place):
        robot_queue_node = bfs(eb.board, r.robot.current_place, r.robot.end_place)
        if robot_queue_node != -1:
            num = move_robot(eb, r.robot, robot_queue_node)
            number_of_steps += num
    return number_of_steps


def move_robot_stack(eb, robot, robot_queue_node):
    robot_to_move = []
    robot_to_move_back = []
    number_of_steps = 0
    for p in robot_queue_node.path:
        if eb.board[p.x][p.y] != 0:
            r = find_robot_by_number(eb.board[p.x][p.y])
            robot_to_move.append(r)
    direction = get_direction(p, eb.n)
    if direction == "UP":
        x = eb.row_space + 1
        y = robot.current_place.y
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x, y + number_of_robots)
            if y + number_of_robots >= eb.n - eb.row_space - 1:
                dest = Point(x, y - number_of_robots - 1)
            robot_queue_node_r = bfs(eb.board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_to_move_back.append(robot_point)
                number_of_steps += move_robot(eb, r, robot_queue_node_r)
                number_of_robots -= 1
    if direction == "DOWN":
        x = eb.n - eb.row_space - 1
        y = robot.current_place.y
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x, y + number_of_robots)
            if y + number_of_robots >= eb.n - eb.row_space - 1:
                dest = Point(x, y - number_of_robots - 1)
            robot_queue_node_r = bfs(eb.board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_to_move_back.append(robot_point)
                number_of_steps += move_robot(eb, r, robot_queue_node_r)
                number_of_robots -= 1
    if direction == "LEFT":
        x = robot.current_place.x
        y = eb.row_space + 1
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x + number_of_robots, y)
            if x + number_of_robots >= eb.n - eb.row_space - 1:
                dest = Point(x - number_of_robots - 1, y)
            robot_queue_node_r = bfs(eb.board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_to_move_back.append(robot_point)
                number_of_steps += move_robot(eb, r, robot_queue_node_r)
                number_of_robots -= 1
    if direction == "RIGHT":
        x = robot.current_place.x
        y = eb.n - eb.row_space - 1
        number_of_robots = len(robot_to_move)
        for r in robot_to_move:
            dest = Point(x + number_of_robots, y)
            if x + number_of_robots >= eb.n - eb.row_space - 1:
                dest = Point(x - number_of_robots - 1, y)
            robot_queue_node_r = bfs(eb.board, r.current_place, dest)
            if robot_queue_node_r != -1:
                robot_point = RobotPoint(r, dest)
                robot_to_move_back.append(robot_point)
                number_of_steps += move_robot(eb, r, robot_queue_node_r)
                number_of_robots -= 1

    robot_queue_node = bfs(eb.board, robot.current_place, robot.end_place)
    if robot_queue_node != -1:
        number_of_steps += move_robot(eb, robot, robot_queue_node)
    number_of_steps += move_robots_back_test(eb, robot_to_move_back)
    return number_of_steps


def get_direction(p, n):
    if p.x < n / 2 and n / 4 < p.y < (3 * (n / 4)):
        return "UP"
    if p.x >= n / 2 and n / 4 < p.y < (3 * (n / 4)):
        return "DOWN"
    if p.y < n / 2 and n / 4 < p.x < (3 * (n / 4)):
        return "LEFT"
    if p.y >= n / 2 and n / 4 < p.x < (3 * (n / 4)):
        return "RIGHT"


def move_robot_to_final_place(eb, robot, direction):
    number_of_steps = 0
    # move robot to final place
    robot_queue_node = bfs(eb.board, robot.current_place, robot.end_place)
    if robot_queue_node != -1:
        num = move_robot(eb, robot, robot_queue_node)
        number_of_steps += num
        return number_of_steps
    else:
        dest = 0
        if direction == "LEFT":
            dest = Point(robot.current_place.x, robot.current_place.y + eb.row_space + 1)
        if direction == "RIGHT":
            dest = Point(robot.current_place.x, robot.current_place.y - eb.row_space - 1)
        if direction == "UP":
            dest = Point(robot.current_place.x + eb.row_space + 1, robot.current_place.y)
        if direction == "DOWN":
            dest = Point(robot.current_place.x - eb.row_space - 1, robot.current_place.y)

        robot_queue_node = bfs(eb.board, robot.current_place, dest)
        if robot_queue_node != -1:
            number_of_steps += move_robot(eb, robot, robot_queue_node)

        robot_queue_node = bfs_few_steps(eb.board, robot.current_place, robot.end_place)
        number_of_steps += move_robot_stack(eb, robot, robot_queue_node)

    return number_of_steps


def move_robot_after_finish(eb):
    test(eb, 0)
    number_of_steps = 0
    for i in range(eb.n):
        for j in range(eb.n):
            if eb.board_final_state[i][j] != eb.board[i][j]:
                if eb.board_final_state[i][j] != 0:
                    robot = find_robot_by_number(eb.board_final_state[i][j])
                    if robot != -1:
                        robot_queue_node = bfs_few_steps(eb.board, robot.current_place, robot.end_place)
                        if robot_queue_node != -1:
                            number_of_steps += move_robot_stack(eb, robot, robot_queue_node)
    return number_of_steps
