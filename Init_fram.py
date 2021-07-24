from BFS import bfs, is_valid
from Move_Robot import move_robot, move_robot_to_dest
from Point import Point
from RobotPoint import RobotPoint
from params import robot_list, FindRobotByNumber, getRobotListSize


def frames(board,blank_spcae):
    # if we moved one robot - break from the for
    flag = False
    number_of_steps = 0
    # The loop ran up to 2, once for the rows up and on the left and the second time for the rows down and on the right
    for g in range(2):
        # Number of rows filled in as "Frame"
        for h in range(blank_spcae):
            l = h
            # Runs on the lines below
            if g == 1:
                l = len(board) - 1 - h
            for k in range(len(board) - (blank_spcae * 2)):
                k += blank_spcae
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
                                    num = move_robot(board, robot, robot_queue_node)
                                    number_of_steps += num
                                    flag = True
                                    break
                    flag = False
        # Number of rows filled in as "Frame"
        for h in range(blank_spcae):
            l = h
            # Runs on the right row
            if g == 1:
                l = len(board) - 1 - h
            for k in range(len(board) - (blank_spcae * 2)):
                k += blank_spcae
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
                                p = Point(k , l)
                                robot_queue_node = bfs(board, robot.current_place, p)
                                if robot_queue_node != -1:
                                    num = move_robot(board, robot, robot_queue_node)
                                    number_of_steps +=num
                                    flag = True
                                    break
                    flag = False
            print("-----------------------------------")

    return number_of_steps


def get_direction(p, n, blank_spcae):
    if p.x <=  blank_spcae and p.y >= blank_spcae and p.y <= n - blank_spcae:
        return "UP"

    if p.x >= blank_spcae and p.x <= n-blank_spcae and p.y <  blank_spcae:
        return "LEFT"

    if p.x >= n - blank_spcae and p.y >= blank_spcae and p.y <= n -blank_spcae:
        return "DOWN"

    if p.x >= blank_spcae and p.x <= n - blank_spcae and p.y >= n - blank_spcae:
        return "RIGHT"


def get_robot_out(board, robot, blank_spcae):
    p = robot.current_place
    n = len(board)
    direction = get_direction(p, n, blank_spcae)
    if direction == "UP":
        move_robots_up(board, robot, blank_spcae)
        print("UP")
    if direction == "RIGHT":
        move_robots_right(board, robot, blank_spcae)
        print("RIGHT")
    if direction == "DOWN":
        move_robots_down(board, robot, blank_spcae)
        print("DOWN")
    if direction == "LEFT":
        print("LEFT")
        move_robots_left(board, robot, blank_spcae)


def move_robots_up(board, robot, blank_spcae):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    x = p.x

    while (board[x][p.y] != 0) or (board[x][p.y] == 0 and board[x + 1][p.y] != 0):
    # while board[x][p.y] != 0:
        counter += 1
        x += 1
    if counter == 0:
        print("0")
    number_steps_out = counter
    if p.y < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x + counter][p.y])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x + number_steps_out + 1, p.y + counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            # if robot_queue_node == -1:
            #     point_temp = Point(p.x + number_steps_out + 2, p.y - counter)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)
            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x + number_steps_out + plus_steps, p.y + counter)
                if is_valid(p.x + number_steps_out + plus_steps, p.y + counter, len(board),  len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1

        # move robot to final place
        move_robot_to_final_place(board, robot)

        # reverse the robots -> return robots
        move_robots_back(board, robot_old_place)

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x + counter][p.y])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x + number_steps_out + 1, p.y - counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            # if robot_queue_node == -1:
            #     point_temp = Point(p.x + number_steps_out + 2, p.y - counter)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)
            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x + number_steps_out + plus_steps, p.y - counter)
                if is_valid(p.x + number_steps_out + plus_steps, p.y - counter, len(board),  len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break
            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  (move_robots_up 2) BFS")
                counter -= 1


        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num

    return number_of_steps


def move_robots_down(board, robot, blank_spcae):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    x = p.x

    while (board[x][p.y] != 0) or (board[x][p.y] == 0 and board[x - 1][p.y] != 0):
        counter += 1
        x -= 1
    if counter == 0:
        print("0 ---------------------------------------------------------------------")

    number_steps_out = counter
    if p.y < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x - counter][p.y])
            if r == -1:
                print("-1 --------------------------------------------------------------")
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - number_steps_out - counter - 1, p.y + counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            # if robot_queue_node == -1:
            #     point_temp = Point(p.x - number_steps_out - 2, p.y - counter)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)
            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x - number_steps_out - counter - plus_steps, p.y + counter)
                if is_valid(p.x - number_steps_out - counter - plus_steps, p.y + counter , len(board),  len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  BFS")
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x - counter][p.y])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - number_steps_out - 1, p.y - counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            # if robot_queue_node == -1:
            #     point_temp = Point(p.x - number_steps_out - 2, p.y - counter)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)

            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x - number_steps_out - plus_steps, p.y - counter)
                if is_valid(p.x - number_steps_out - plus_steps, p.y - counter, len(board),  len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1

            else:
                print("========================================================== -1  BFS")
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num


def move_robots_left(board, robot, blank_space):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    y = p.y

    while (board[p.x][y] != 0) or (board[p.x][y] == 0 and board[p.x][y + 1] != 0):
    # while board[p.x][y] != 0:
        counter += 1
        y += 1
    number_steps_out = counter
    if p.x < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y + counter])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x + counter, p.y + number_steps_out + 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x + counter, p.y + number_steps_out + plus_steps)
                if is_valid(p.x + counter, p.y + number_steps_out + plus_steps, len(board), len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break


            # if robot_queue_node == -1:
            #     if r.current_place.y < blank_space:
            #         point_temp = Point(p.x + counter, p.y + blank_space - r.current_place.y + 2)
            #     else:
            #         point_temp = Point(p.x + counter, p.y + number_steps_out + 2)

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  BFS")
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num


    if p.x >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y + counter])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - counter, p.y + number_steps_out + 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x - counter, p.y + number_steps_out + plus_steps)
                if is_valid(p.x - counter, p.y + number_steps_out + plus_steps, len(board), len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break


            # if robot_queue_node == -1:
            #     point_temp = Point(p.x + counter, p.y + number_steps_out + 2)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)

            if robot_queue_node != -1:
                dest = Point(r.current_place.x, r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  BFS")
                counter -= 1


        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num

def move_robots_right(board, robot, blank_spcae):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    y = p.y

    while (board[p.x][y] != 0) or (board[p.x][y] == 0 and board[p.x][y - 1] != 0):
    # while board[p.x][y] != 0:
        counter += 1
        y -= 1
    if counter == 0:
        print("0")
    number_steps_out = counter
    if p.x < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y - counter])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x + counter, p.y - number_steps_out - 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x + counter, p.y - number_steps_out - plus_steps)
                if is_valid(p.x + counter, p.y - number_steps_out - plus_steps, len(board), len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break

            # if robot_queue_node == -1:
            #     point_temp = Point(p.x + counter, p.y - number_steps_out - 2)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  BFS")
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y - counter])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - counter, p.y - number_steps_out - 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)

            # if robot_queue_node == -1:
            #     point_temp = Point(p.x + counter, p.y - number_steps_out - 2)
            #     robot_queue_node = bfs(board, r.current_place, point_temp)
            plus_steps = 1
            while robot_queue_node == -1:
                point_temp = Point(p.x - counter, p.y - number_steps_out - plus_steps)

                if is_valid(p.x - counter, p.y - number_steps_out - plus_steps, len(board),  len(board)):
                    robot_queue_node = bfs(board, r.current_place, point_temp)
                    plus_steps += 1
                else:
                    break
            if robot_queue_node != -1:
                dest = Point(r.current_place.x, r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  BFS")
                counter -= 1


        # move robot to final place
        num = move_robot_to_final_place(board, robot)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place)
        number_of_steps += num


def move_robot_to_final_place(board, robot):
    number_of_steps = 0
    # move robot to final place
    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
    if robot_queue_node != -1:
        num = move_robot_to_dest(board, robot, robot_queue_node)
        number_of_steps +=num
        return number_of_steps
    return number_of_steps


def move_robots_back(board, robot_old_place):
    number_of_steps = 0
    # reverse the robots -> return robots
    for r in reversed(robot_old_place):
        robot_queue_node = bfs(board, r.robot.current_place, r.dest)
        if robot_queue_node != -1:
            num = move_robot(board, r.robot, robot_queue_node)
            number_of_steps += num
        else:
            print("========================================================== -1  (move_robots_back) BFS")
    return number_of_steps