from BFS import bfs
from MoveRobots import move_robot_all_path
from Move_Robot import move_robot, move_robot_to_dest
from Point import Point
from RobotPoint import RobotPoint
from params import robot_list, FindRobotByNumber, getRobotListSize


def frames(board, boardgame2,blank_spcae):
    flag = False
    number_of_robot = len(robot_list)
    print("Numb of robots: ", number_of_robot)
    number_of_steps = 0
    for g in range(2):
        for h in range(blank_spcae):
            l = h
            if g == 1:
                l = len(board) - 1 - h
            for k in range(len(board) - (blank_spcae * 2)):
                k += blank_spcae
                if board[l][k] == 0:
                    for i in range(len(board) - 10):
                        if flag:
                            flag = False
                            break
                        for j in range(len(board) - 10):
                            if board[i + 5][j + 5] != 0 and board[i + 5][j + 5] != -1:
                                robot = FindRobotByNumber(board[i + 5][j + 5])
                                p = Point(l, k)
                                robot_queue_node = bfs(board, robot.current_place, p)
                                if robot_queue_node != -1:
                                    num = move_robot(board, robot, robot_queue_node, boardgame2)
                                    number_of_steps +=num
                                    number_of_robot = number_of_robot - 1
                                    if number_of_robot == 0:
                                        return number_of_steps
                                    flag = True
                                    break

        for h in range(blank_spcae):
            l = h
            if g == 1:
                l = len(board) - 1 - h
            for k in range(len(board) - (blank_spcae * 2)):
                k += blank_spcae
                if board[k][l] == 0:
                    for i in range(len(board) - 10):
                        if flag:
                            flag = False
                            break
                        for j in range(len(board) - 10):
                            if board[i + 5][j + 5] != 0 and board[i + 5][j + 5] != -1:
                                robot = FindRobotByNumber(board[i + 5][j + 5])
                                p = Point(k , l)
                                robot_queue_node = bfs(board, robot.current_place, p)
                                if robot_queue_node != -1:
                                    num = move_robot(board, robot, robot_queue_node, boardgame2)
                                    number_of_steps +=num
                                    number_of_robot = number_of_robot - 1
                                    if number_of_robot == 0:
                                        return number_of_steps
                                    flag = True
                                    break
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


def get_robot_out(board, robot, boardgame2, blank_spcae):
    p = robot.current_place
    n = len(board)
    direction = get_direction(p, n, blank_spcae)
    if direction == "UP":
        move_robots_up(board, robot, boardgame2)
        print("UP")
    if direction == "RIGHT":
        move_robots_right(board, robot, boardgame2)
        print("RIGHT")
    if direction == "DOWN":
        move_robots_down(board, robot, boardgame2)
        print("DOWN")
    if direction == "LEFT":
        print("LEFT")
        move_robots_left(board, robot, boardgame2)


def move_robots_up(board, robot, boardgame2):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = 0
    x = p.x
    while board[x][p.y] != 0:
        counter += 1
        x += 1
    if p.y < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x + counter][p.y])
            point_temp = Point(p.x + counter + 1, p.y + counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)
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
                print("========================================================== -1 BFS")

        # move robot to final place
        move_robot_to_final_place(board, robot, boardgame2)

        # reverse the robots -> return robots
        move_robots_back(board, boardgame2, robot_old_place)

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x + counter][p.y])
            point_temp = Point(p.x + counter + 1, p.y - counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)
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
                print("========================================================== -1  (2) BFS")

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num

    return number_of_steps

def move_robots_down(board, robot, boardgame2):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = 0
    x = p.x

    while board[x][p.y] != 0:
        counter += 1
        x -= 1
    if p.y < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x - counter][p.y])
            point_temp = Point(p.x - counter - 1, p.y + counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x - counter][p.y])
            point_temp = Point(p.x - counter - 1, p.y - counter)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num

                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num


def move_robots_left(board, robot, boardgame2):
    number_of_steps =0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = 0
    y = p.y

    while board[p.x][y] != 0:
        counter += 1
        y += 1
    if p.x < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y + counter])
            point_temp = Point(p.x + counter, p.y + counter + 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num

    if p.x >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y + counter])
            point_temp = Point(p.x - counter, p.y + counter + 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            if robot_queue_node != -1:
                dest = Point(r.current_place.x, r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num


def move_robots_right(board, robot, boardgame2):
    number_of_steps = 0
    robot_old_place = []
    p = robot.current_place
    n = len(board)
    counter = 0
    y = p.y

    while board[p.x][y] != 0:
        counter += 1
        y -= 1
    if p.x < n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y - counter])
            point_temp = Point(p.x + counter, p.y - counter - 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            if robot_queue_node != -1:
                dest = Point(r.current_place.x , r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num

    if p.y >= n / 2:
        while counter > 0:
            r = FindRobotByNumber(board[p.x][p.y - counter])
            point_temp = Point(p.x - counter, p.y - counter - 1)
            robot_queue_node = bfs(board, r.current_place, point_temp)
            if robot_queue_node != -1:
                dest = Point(r.current_place.x, r.current_place.y)
                # add to back list
                robot_point = RobotPoint(r, dest)
                robot_old_place.append(robot_point)
                # move robot to new place
                num = move_robot(board, r, robot_queue_node, boardgame2)
                number_of_steps += num
                counter -= 1

        # move robot to final place
        num = move_robot_to_final_place(board, robot, boardgame2)
        number_of_steps += num

        # reverse the robots -> return robots
        num = move_robots_back(board, boardgame2, robot_old_place)
        number_of_steps += num


def move_robot_to_final_place(board, robot, boardgame2):
    number_of_steps = 0
    # move robot to final place
    robot_queue_node = bfs(board, robot.current_place, robot.end_place)
    if robot_queue_node != -1:
        num = move_robot_to_dest(board, robot, robot_queue_node, boardgame2)
        number_of_steps +=num
        return number_of_steps


def move_robots_back(board, boardgame2, robot_old_place):
    number_of_steps = 0
    # reverse the robots -> return robots
    for r in reversed(robot_old_place):
        robot_queue_node = bfs(board, r.robot.current_place, r.dest)
        if robot_queue_node != -1:
            num = move_robot(board, r.robot, robot_queue_node, boardgame2)
            number_of_steps += num
    return number_of_steps