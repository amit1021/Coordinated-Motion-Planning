from BFS import bfs
from Move_Robot import move_robot
from Point import Point
from params import FindRobotByNumber


def frames(board, blank_space, boardgame2):
    # if we moved one robot - break from the for
    flag = False
    number_of_steps = 0
    # The loop ran up to 2, once for the rows up and on the left and the second time for the rows down and on the right
    for g in range(2):
        # Number of rows filled in as "Frame"
        for h in range(blank_space):
            l = h
            # Runs on the lines below
            if g == 1:
                l = len(board) - 1 - h
            for k in range(len(board) - (blank_space * 2)):
                k += blank_space
                if board[l][k] == 0:
                    for i in range(len(board) - 10):
                        if flag:
                            # flag = False
                            break
                        for j in range(len(board) - 10):
                            # Checks if there is a robot on this board
                            if board[i + 5][j + 5] != 0 and board[i + 5][j + 5] != -1:
                                robot = FindRobotByNumber(board[i + 5][j + 5])
                                # The point to which the robot goes
                                p = Point(l, k)
                                robot_queue_node = bfs(board, robot.current_place, p)
                                if robot_queue_node != -1:
                                    num = move_robot(board, robot, robot_queue_node, boardgame2)
                                    number_of_steps += num
                                    flag = True
                                    break
                    flag = False
        # Number of rows filled in as "Frame"
        for h in range(blank_space):
            l = h
            # Runs on the right row
            if g == 1:
                l = len(board) - 1 - h
            for k in range(len(board) - (blank_space * 2)):
                k += blank_space
                if board[k][l] == 0:
                    for i in range(len(board) - 10):
                        if flag:
                            # flag = False
                            break
                        for j in range(len(board) - 10):
                            # Checks if there is a robot on this board
                            if board[i + 5][j + 5] != 0 and board[i + 5][j + 5] != -1:
                                robot = FindRobotByNumber(board[i + 5][j + 5])
                                # The point to which the robot goes
                                p = Point(k, l)
                                robot_queue_node = bfs(board, robot.current_place, p)
                                if robot_queue_node != -1:
                                    num = move_robot(board, robot, robot_queue_node, boardgame2)
                                    number_of_steps += num
                                    flag = True
                                    break
                    flag = False

    print("----------------------------number_of_steps after frame -----------------------------------------: ",number_of_steps)
    return number_of_steps


def frames__(board, blank_space, board_length,  boardgame2):
    flag = False
    number_of_steps = 0
    length = len(board)
    lines = int((length - board_length)/2)
    #for on the top frame
    for i_frame in range(blank_space):
        for j_frame in range(length - (2 * blank_space)):
            if board[i_frame][j_frame + blank_space] == 0:
                # for on the board without extension
                for i_board in range(board_length):
                    if flag:
                        break
                    for j_board in range(board_length):
                        if board[i_board + lines][j_board + lines] != 0 and board[i_board + lines][j_board + lines] != -1:
                            robot = FindRobotByNumber(board[i_board + lines][j_board + lines])
                            # The point to which the robot goes
                            p = Point(i_frame, j_frame + blank_space)
                            robot_queue_node = bfs(board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(board, robot, robot_queue_node, boardgame2)
                                number_of_steps += num
                                flag = True
                                break
                flag = False

    # for on the left frame
    for j_frame in range(blank_space):
        for i_frame in range(length - (2 * blank_space)):
            if board[i_frame + blank_space][j_frame] == 0:
                # for on the board without extension
                for j_board in range(board_length):
                    if flag:
                        break
                    for i_board in range(board_length):
                        if board[i_board + lines][j_board + lines] != 0 and board[i_board + lines][j_board + lines] != -1:
                            robot = FindRobotByNumber(board[i_board + lines][j_board + lines])
                            # The point to which the robot goes
                            p = Point(i_frame+ blank_space, j_frame)
                            robot_queue_node = bfs(board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(board, robot, robot_queue_node, boardgame2)
                                number_of_steps += num
                                flag = True
                                break
                flag = False

    # for on the down frame
    for i_frame in range(blank_space):
        for j_frame in range(length - (2 * blank_space)):
            i_down = length - i_frame - 1
            if board[i_down][j_frame + blank_space] == 0:
                # for on the board without extension
                for i_board in range(board_length):
                    i_down_board = board_length - 1 - i_board
                    if flag:
                        break
                    for j_board in range(board_length):
                        if board[i_down_board + lines][j_board + lines] != 0 and board[i_down_board + lines][j_board + lines] != -1:
                            robot = FindRobotByNumber(board[i_down_board + lines][j_board + lines])
                            # The point to which the robot goes
                            p = Point(i_down, j_frame + blank_space)
                            robot_queue_node = bfs(board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(board, robot, robot_queue_node, boardgame2)
                                number_of_steps += num
                                flag = True
                                break
                flag = False
    # for on the right frame
    for j_frame in range(blank_space):
        for i_frame in range(length - (2 * blank_space)):
            j_down = length - j_frame - 1
            if board[i_frame + blank_space][j_down] == 0:
                # for on the board without extension
                for j_board in range(board_length):
                    j_down_board = board_length - 1 - j_board
                    if flag:
                        break
                    for i_board in range(board_length):
                        if board[i_board + lines][j_down_board + lines] != 0 and board[i_board + lines][j_down_board + lines] != -1:
                            robot = FindRobotByNumber(board[i_board + lines][j_down_board + lines])
                            # The point to which the robot goes
                            p = Point(i_frame+ blank_space, j_down)
                            robot_queue_node = bfs(board, robot.current_place, p)
                            if robot_queue_node != -1:
                                num = move_robot(board, robot, robot_queue_node, boardgame2)
                                number_of_steps += num
                                flag = True
                                break
                flag = False
    print("----------------------------number_of_steps after frame -----------------------------------------: ",number_of_steps)
    return number_of_steps

# def get_direction_fram(p, n, blank_spcae):
#     if p.x <=  blank_spcae and p.y >= blank_spcae and p.y <= n - blank_spcae:
#         return "UP"
#
#     if p.x >= blank_spcae and p.x <= n-blank_spcae and p.y <  blank_spcae:
#         return "LEFT"
#
#     if p.x >= n - blank_spcae and p.y >= blank_spcae and p.y <= n -blank_spcae:
#         return "DOWN"
#
#     if p.x >= blank_spcae and p.x <= n - blank_spcae and p.y >= n - blank_spcae:
#         return "RIGHT"
#
#
# def get_robot_out(board, robot,boardgame2, blank_spcae):
#     p = robot.current_place
#     n = len(board)
#     direction = get_direction_fram(p, n, blank_spcae)
#     if direction == "UP":
#         move_robots_up(board, robot,boardgame2,  blank_spcae)
#         print("UP")
#     if direction == "RIGHT":
#         move_robots_right(board, robot,boardgame2,  blank_spcae)
#         print("RIGHT")
#     if direction == "DOWN":
#         move_robots_down(board, robot,boardgame2,  blank_spcae)
#         print("DOWN")
#     if direction == "LEFT":
#         print("LEFT")
#         move_robots_left(board, robot, boardgame2, blank_spcae)

#
# def move_robots_up(board, robot,boardgame2,  blank_space):
#     number_of_steps = 0
#     robot_old_place = []
#     p = robot.current_place
#     n = len(board)
#     counter = -1
#     x = p.x
#
#     while (board[x][p.y] != 0) or (board[x][p.y] == 0 and board[x + 1][p.y] != 0):
#         counter += 1
#         x += 1
#     number_steps_out = counter
#     if p.y < n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x + counter][p.y])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x + number_steps_out + 1, p.y + counter)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             # if robot_queue_node == -1:
#             #     point_temp = Point(p.x + number_steps_out + 2, p.y - counter)
#             #     robot_queue_node = bfs(board, r.current_place, point_temp)
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x + number_steps_out + plus_steps, p.y + counter)
#                 if is_valid(p.x + number_steps_out + plus_steps, p.y + counter, len(board),  len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x , r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 print("========================================================== -1  (move_robots_up 2) BFS")
#                 counter -= 1
#
#
#         # move robot to final place
#         move_robot_to_final_place(board, robot, blank_space,"UP", boardgame2)
#
#         # reverse the robots -> return robots
#         move_robots_back(board, robot_old_place, boardgame2)
#
#     if p.y >= n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x + counter][p.y])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x + number_steps_out + 1, p.y - counter)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             # if robot_queue_node == -1:
#             #     point_temp = Point(p.x + number_steps_out + 2, p.y - counter)
#             #     robot_queue_node = bfs(board, r.current_place, point_temp)
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x + number_steps_out + plus_steps, p.y - counter)
#                 if is_valid(p.x + number_steps_out + plus_steps, p.y - counter, len(board),  len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x , r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 print("========================================================== -1  (move_robots_up 2) BFS")
#                 counter -= 1
#
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot,  blank_space,"UP",boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place, boardgame2)
#         number_of_steps += num
#
#     return number_of_steps
#
#
# def move_robots_down(board, robot, boardgame2, blank_space):
#     number_of_steps = 0
#     robot_old_place = []
#     p = robot.current_place
#     n = len(board)
#     counter = -1
#     x = p.x
#
#     while (board[x][p.y] != 0) or (board[x][p.y] == 0 and board[x - 1][p.y] != 0):
#         counter += 1
#         x -= 1
#     number_steps_out = counter
#     if p.y < n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x - counter][p.y])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x - number_steps_out - counter - 1, p.y + counter)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x - number_steps_out - counter - plus_steps, p.y + counter)
#                 if is_valid(p.x - number_steps_out - counter - plus_steps, p.y + counter , len(board),  len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x , r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 counter -= 1
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot, blank_space,"DOWN", boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place,boardgame2)
#         number_of_steps += num
#
#     if p.y >= n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x - counter][p.y])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x - number_steps_out - 1, p.y - counter)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x - number_steps_out - plus_steps, p.y - counter)
#                 if is_valid(p.x - number_steps_out - plus_steps, p.y - counter, len(board),  len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x , r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#
#             else:
#                 counter -= 1
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot, blank_space,"DOWN", boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place,boardgame2)
#         number_of_steps += num
#
#
# def move_robots_left(board, robot,boardgame2, blank_space):
#     number_of_steps = 0
#     robot_old_place = []
#     p = robot.current_place
#     n = len(board)
#     counter = -1
#     y = p.y
#
#     while (board[p.x][y] != 0) or (board[p.x][y] == 0 and board[p.x][y + 1] != 0):
#         counter += 1
#         y += 1
#     number_steps_out = counter
#     if p.x < n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x][p.y + counter])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x + counter, p.y + number_steps_out + 1)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x + counter, p.y + number_steps_out + plus_steps)
#                 if is_valid(p.x + counter, p.y + number_steps_out + plus_steps, len(board), len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x , r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 counter -= 1
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot, blank_space,"LEFT", boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place, boardgame2)
#         number_of_steps += num
#
#
#     if p.x >= n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x][p.y + counter])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x - counter, p.y + number_steps_out + 1)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x - counter, p.y + number_steps_out + plus_steps)
#                 if is_valid(p.x - counter, p.y + number_steps_out + plus_steps, len(board), len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x, r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 counter -= 1
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot,  blank_space,"LEFT",boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place, boardgame2)
#         number_of_steps += num
#
# def move_robots_right(board, robot, boardgame2, blank_space):
#     number_of_steps = 0
#     robot_old_place = []
#     p = robot.current_place
#     n = len(board)
#     counter = -1
#     y = p.y
#
#     while (board[p.x][y] != 0) or (board[p.x][y] == 0 and board[p.x][y - 1] != 0):
#         counter += 1
#         y -= 1
#     number_steps_out = counter
#     if p.x < n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x][p.y - counter])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x + counter, p.y - number_steps_out - 1)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x + counter, p.y - number_steps_out - plus_steps)
#                 if is_valid(p.x + counter, p.y - number_steps_out - plus_steps, len(board), len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x , r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 counter -= 1
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot, blank_space,"RIGHT", boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place, boardgame2)
#         number_of_steps += num
#
#     if p.y >= n / 2:
#         while counter > 0:
#             r = FindRobotByNumber(board[p.x][p.y - counter])
#             if r.robot_number == 0:
#                 counter -= 1
#                 continue
#             point_temp = Point(p.x - counter, p.y - number_steps_out - 1)
#             robot_queue_node = bfs(board, r.current_place, point_temp)
#
#             plus_steps = 1
#             while robot_queue_node == -1:
#                 point_temp = Point(p.x - counter, p.y - number_steps_out - plus_steps)
#
#                 if is_valid(p.x - counter, p.y - number_steps_out - plus_steps, len(board),  len(board)):
#                     robot_queue_node = bfs(board, r.current_place, point_temp)
#                     plus_steps += 1
#                 else:
#                     break
#             if robot_queue_node != -1:
#                 dest = Point(r.current_place.x, r.current_place.y)
#                 # add to back list
#                 robot_point = RobotPoint(r, dest)
#                 robot_old_place.append(robot_point)
#                 # move robot to new place
#                 num = move_robot(board, r, robot_queue_node, boardgame2)
#                 number_of_steps += num
#                 counter -= 1
#             else:
#                 counter -= 1
#
#         # move robot to final place
#         num = move_robot_to_final_place(board, robot, blank_space, "RIGHT", boardgame2)
#         number_of_steps += num
#
#         # reverse the robots -> return robots
#         num = move_robots_back(board, robot_old_place, boardgame2)
#         number_of_steps += num


# def move_robot_to_final_place(board, robot ,blank_space,direc, boardgame2):
#     number_of_steps = 0
#     # move robot to final place
#     robot_queue_node = bfs(board, robot.current_place, robot.end_place)
#     if robot_queue_node != -1:
#         num = move_robot_to_dest(board, robot, robot_queue_node , boardgame2)
#         number_of_steps +=num
#         return number_of_steps
#     else:
#
#         print("-------------------------------------------")
#         dest = 0
#         if direc == "LEFT":
#             dest = Point( robot.current_place.x,robot.current_place.y + blank_space + 1)
#         if direc == "RIGHT":
#             dest = Point(robot.current_place.x, robot.current_place.y - blank_space - 1)
#         if direc == "UP":
#             dest = Point(robot.current_place.x+ blank_space + 1, robot.current_place.y)
#         if direc == "DOWN":
#             dest = Point(robot.current_place.x - blank_space - 1, robot.current_place.y )
#
#         robot_queue_node = bfs(board, robot.current_place, dest)
#         if robot_queue_node != -1:
#             number_of_steps += move_robot(board, robot, robot_queue_node , boardgame2)
#
#         robot_queue_node = bfs_few_steps(board, robot.current_place, robot.end_place)
#         number_of_steps += stack_robot(robot, board, robot_queue_node,blank_space, boardgame2)
#         # robot_queue_node = bfs(board, robot.current_place, dest)
#         # if robot_queue_node != -1:
#         #     number_of_steps += move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
#     return number_of_steps
#
#
# def move_robots_back(board, robot_old_place , boardgame2):
#     number_of_steps = 0
#     # reverse the robots -> return robots
#     for r in reversed(robot_old_place):
#         robot_queue_node = bfs(board, r.robot.current_place, r.dest)
#         if robot_queue_node != -1:
#             num = move_robot(board, r.robot, robot_queue_node, boardgame2)
#             number_of_steps += num
#         else:
#             print("========================================================== move_robots_back")
#     return number_of_steps