from BFS import bfs
from MoveRobot import move_robot
from RobotDetails import find_robot_by_number
from MoveRobotByDirection import get_robot_out


def insert_in_spiral(eb):
    a = int(eb.n / 2)
    b = int(eb.n / 2)
    r = c = eb.n
    low_row = 0 if (0 > a) else a
    low_column = 0 if (0 > b) else b - 1
    high_row = r - 1 if ((a + 1) >= r) else a + 1
    high_column = c - 1 if ((b + 1) >= c) else b + 1
    number_of_steps = 0

    while low_row > 0 - r and low_column > 0 - c:
        i = low_column + 1
        while (i <= high_column and
               i < c and low_row >= 0):
            if eb.board_final_state[low_row][i] >= 1:
                robot = find_robot_by_number(eb.board_final_state[low_row][i])
                if robot.robot_number == 0:
                    print("---------------------------------------------------------------")
                if robot != -1:
                    robot_queue_node = bfs(eb.board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        number_of_steps += move_robot(eb, robot, robot_queue_node)
                    else:
                        get_robot_out(eb, robot)
            i += 1
        low_row -= 1

        i = low_row + 2
        while (i <= high_row and
               i < r and high_column < c):
            if eb.board_final_state[i][high_column] >= 1:
                robot = find_robot_by_number(eb.board_final_state[i][high_column])
                if robot.robot_number == 0:
                    print("---------------------------------------------------------------")
                if robot != -1:
                    robot_queue_node = bfs(eb.board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        num = move_robot(eb, robot, robot_queue_node)
                        number_of_steps += num
                    else:
                        get_robot_out(eb, robot)
            i += 1
        high_column += 1

        i = high_column - 2
        while (i >= low_column and
               i >= 0 and high_row < r):
            if eb.board_final_state[high_row][i] >= 1:
                robot = find_robot_by_number(eb.board_final_state[high_row][i])
                if robot.robot_number == 0:
                    print("---------------------------------------------------------------")
                if robot != -1:
                    robot_queue_node = bfs(eb.board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        num = move_robot(eb, robot, robot_queue_node)
                        number_of_steps += num
                    else:
                        get_robot_out(eb, robot)
            i -= 1
        high_row += 1

        i = high_row - 2
        while (i > low_row and
               i >= 0 and low_column >= 0):
            if eb.board_final_state[i][low_column] >= 1:
                robot = find_robot_by_number(eb.board_final_state[i][low_column])
                if robot.robot_number == 0:
                    print("---------------------------------------------------------------")
                if robot != -1:
                    robot_queue_node = bfs(eb.board, robot.current_place, robot.end_place)
                    if robot_queue_node != -1:
                        number_of_steps += move_robot(eb, robot, robot_queue_node)
                    else:
                        get_robot_out(eb, robot)
            i -= 1
        low_column -= 1
    return number_of_steps
