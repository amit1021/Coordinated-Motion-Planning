from BFS import bfs, is_valid
from Move_Robot import move_robot, move_robots_back
from Point import Point
from RobotPoint import RobotPoint
from get_robot_stack import move_robot_to_final_place
from params import FindRobotByNumber


def get_direction_fram(p, n, blank_spcae):
    if p.x <=  blank_spcae and p.y >= blank_spcae and p.y <= n - blank_spcae:
        return "UP"
    if p.x >= blank_spcae and p.x <= n-blank_spcae and p.y <  blank_spcae:
        return "LEFT"

    if p.x >= n - blank_spcae and p.y >= blank_spcae and p.y <= n -blank_spcae:
        return "DOWN"

    if p.x >= blank_spcae and p.x <= n - blank_spcae and p.y >= n - blank_spcae:
        return "RIGHT"


def get_robot_out(board, robot,boardgame2, blank_spcae):
    p = robot.current_place
    n = len(board)
    direction = get_direction_fram(p, n, blank_spcae)
    if direction == "UP":
        move_robots_up(board, robot,boardgame2,  blank_spcae)
        print("UP")
    if direction == "RIGHT":
        move_robots_right(board, robot,boardgame2,  blank_spcae)
        print("RIGHT")
    if direction == "DOWN":
        move_robots_down(board, robot,boardgame2,  blank_spcae)
        print("DOWN")
    if direction == "LEFT":
        print("LEFT")
        move_robots_left(board, robot, boardgame2, blank_spcae)


def move_robots_up(board, robot,boardgame2,  blank_space):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    x = p.x

    while (board[x][p.y] != 0) or (board[x][p.y] == 0 and board[x + 1][p.y] != 0):
        counter += 1
        x += 1
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
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  (move_robots_up 2) BFS")
                counter -= 1


        # move robot to final place
        move_robot_to_final_place(board, robot, blank_space,"UP", boardgame2)

        # reverse the robots -> return robots
        move_robots_back(board, robot_old_place, boardgame2)

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
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                print("========================================================== -1  (move_robots_up 2) BFS")
                counter -= 1


        # move robot to final place
        num = move_robot_to_final_place(board, robot,  blank_space,"UP",boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place, boardgame2)
        number_of_steps += num

    return number_of_steps


def move_robots_down(board, robot, boardgame2, blank_space):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    x = p.x

    while (board[x][p.y] != 0) or (board[x][p.y] == 0 and board[x - 1][p.y] != 0):
        counter += 1
        x -= 1
    number_steps_out = counter
    if p.y < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x - counter][p.y])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - number_steps_out - counter - 1, p.y + counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)

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
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, blank_space,"DOWN", boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place,boardgame2)
        number_of_steps += num

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x - counter][p.y])
            if r == -1:
                print(343)
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - number_steps_out - 1, p.y - counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)

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
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1

            else:
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, blank_space,"DOWN", boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place,boardgame2)
        number_of_steps += num


def move_robots_left(board, robot,boardgame2, blank_space):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    y = p.y

    while (board[p.x][y] != 0) or (board[p.x][y] == 0 and board[p.x][y + 1] != 0):
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

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, blank_space,"LEFT", boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place, boardgame2)
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

            if robot_queue_node != -1:
                dest = Point(r.current_place.x, r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot,  blank_space,"LEFT",boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place, boardgame2)
        number_of_steps += num


def move_robots_right(board, robot, boardgame2, blank_space):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = -1
    y = p.y

    while (board[p.x][y] != 0) or (board[p.x][y] == 0 and board[p.x][y - 1] != 0):
        counter += 1
        y -= 1
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

            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, blank_space,"RIGHT", boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place, boardgame2)
        number_of_steps += num

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y - counter])
            if r.robot_number == 0:
                counter -= 1
                continue
            point_temp = Point(p.x - counter, p.y - number_steps_out - 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)

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
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1
            else:
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, blank_space, "RIGHT", boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, robot_old_place, boardgame2)
        number_of_steps += num
