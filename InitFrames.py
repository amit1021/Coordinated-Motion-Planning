from BFS import bfs
from MoveRobot import move_robot
from Point import Point
from RobotDetails import find_robot_by_number


def init_frames(eb):
    flag = False
    number_of_steps = 0
    lines = int((eb.n - eb.n_original) / 2)
    # for on the top frame
    for i_frame in range(eb.row_space):
        for j_frame in range(eb.n - (2 * eb.row_space)):
            if eb.board[i_frame][j_frame + eb.row_space] == 0:
                # for on the board without extension
                for i_board in range(eb.n_original):
                    if flag:
                        break
                    for j_board in range(eb.n_original):
                        if eb.board[i_board + lines][j_board + lines] != 0 and eb.board[i_board + lines][j_board + lines] != -1:
                            robot = find_robot_by_number(eb.board[i_board + lines][j_board + lines])
                            # The point to which the robot goes
                            p = Point(i_frame, j_frame + eb.row_space)
                            robot_queue_node = bfs(eb.board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(eb, robot, robot_queue_node)
                                number_of_steps += num
                                flag = True
                                break
                flag = False

    # for on the left frame
    for j_frame in range(eb.row_space):
        for i_frame in range(eb.n - (2 * eb.row_space)):
            if eb.board[i_frame + eb.row_space][j_frame] == 0:
                # for on the board without extension
                for j_board in range(eb.n_original):
                    if flag:
                        break
                    for i_board in range(eb.n_original):
                        if eb.board[i_board + lines][j_board + lines] != 0 and eb.board[i_board + lines][j_board + lines] != -1:
                            robot = find_robot_by_number(eb.board[i_board + lines][j_board + lines])
                            # The point to which the robot goes
                            p = Point(i_frame + eb.row_space, j_frame)
                            robot_queue_node = bfs(eb.board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(eb, robot, robot_queue_node)
                                number_of_steps += num
                                flag = True
                                break
                flag = False

    # for on the down frame
    for i_frame in range(eb.row_space):
        for j_frame in range(eb.n - (2 * eb.row_space)):
            i_down = eb.n - i_frame - 1
            if eb.board[i_down][j_frame + eb.row_space] == 0:
                # for on the board without extension
                for i_board in range(eb.n_original):
                    i_down_board = eb.n_original - 1 - i_board
                    if flag:
                        break
                    for j_board in range(eb.n_original):
                        if eb.board[i_down_board + lines][j_board + lines] != 0 and eb.board[i_down_board + lines][j_board + lines] != -1:
                            robot = find_robot_by_number(eb.board[i_down_board + lines][j_board + lines])
                            # The point to which the robot goes
                            p = Point(i_down, j_frame + eb.row_space)
                            robot_queue_node = bfs(eb.board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(eb, robot, robot_queue_node)
                                number_of_steps += num
                                flag = True
                                break
                flag = False
    # for on the right frame
    for j_frame in range(eb.row_space):
        for i_frame in range(eb.n - (2 * eb.row_space)):
            j_down = eb.n - j_frame - 1
            if eb.board[i_frame + eb.row_space][j_down] == 0:
                # for on the board without extension
                for j_board in range(eb.n_original):
                    j_down_board = eb.n_original - 1 - j_board
                    if flag:
                        break
                    for i_board in range(eb.n_original):
                        if eb.board[i_board + lines][j_down_board + lines] != 0 and eb.board[i_board + lines][j_down_board + lines] != -1:
                            robot = find_robot_by_number(eb.board[i_board + lines][j_down_board + lines])
                            # The point to which the robot goes
                            p = Point(i_frame + eb.row_space, j_down)
                            robot_queue_node = bfs(eb.board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(eb, robot, robot_queue_node)
                                number_of_steps += num
                                flag = True
                                break
                flag = False
    print("----------------------------number_of_steps after frame -----------------------------------------: ",
          number_of_steps)
    return number_of_steps
